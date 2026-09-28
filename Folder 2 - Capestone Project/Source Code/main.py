# main.py - run this file:  python main.py
# reusable jobs (browser start, screenshots, alerts, report) from helpers.py.

import time
from datetime import datetime

from selenium.webdriver.common.by import By

import settings
from helpers import (
    close_banner,
    handle_alert_if_present,
    log_result,
    price_to_number,
    read_test_data,
    start_browser,
    take_screenshot,
    write_report,
)


def main():
    driver = None
    current_step = "start"      # tells the except block which step broke

    try:
        # -------------------------------------------------------------
        # TASK 8 - read test data (runs first, every step below uses it)
        # -------------------------------------------------------------
        current_step = "8. Read test data"
        data = read_test_data()

        # the demo site rejects an email that is already registered,
        # so every run gets a new one built from the current time
        stamp = datetime.now().strftime("%Y%m%d%H%M%S")
        email = data["email_template"].format(stamp=stamp)
        password = data["password"]
        product_name = data["product_name"]
        new_quantity = data["new_quantity"]

        log_result(current_step, "PASS",
                   f"source: {settings.DATA_SOURCE}, product: {product_name}, new quantity: {new_quantity}")

        # -------------------------------------------------------------
        # TASK 1 - launch browser
        # -------------------------------------------------------------
        current_step = "1. Launch browser"
        driver = start_browser()

        driver.get(settings.BASE_URL)
        time.sleep(settings.PAUSE)
        assert "Your Store" in driver.title, "unexpected title: " + driver.title
        take_screenshot(driver, "01_home_page")
        log_result(current_step, "PASS", "title: " + driver.title)

        # -------------------------------------------------------------
        # SETUP - register a new customer
        # The demo site has no ready-made user, so we create one, log
        # out, and then do a proper login in the next step.
        # -------------------------------------------------------------
        current_step = "Setup. Register new customer"

        driver.get(settings.BASE_URL + "index.php?route=account/register")
        driver.find_element(By.ID, "input-firstname").send_keys(data["first_name"])
        driver.find_element(By.ID, "input-lastname").send_keys(data["last_name"])
        driver.find_element(By.ID, "input-email").send_keys(email)
        driver.find_element(By.ID, "input-telephone").send_keys(data["telephone"])
        driver.find_element(By.ID, "input-password").send_keys(password)
        driver.find_element(By.ID, "input-confirm").send_keys(password)
        driver.find_element(By.NAME, "agree").click()
        take_screenshot(driver, "02_registration_form")

        driver.find_element(By.CSS_SELECTOR, "input[value='Continue']").click()
        time.sleep(settings.PAUSE)
        heading = driver.find_element(By.CSS_SELECTOR, "#content h1").text
        assert heading == "Your Account Has Been Created!", "registration failed, page says: " + heading
        take_screenshot(driver, "03_account_created")

        # registering already logs us in, so sign out first
        driver.get(settings.BASE_URL + "index.php?route=account/logout")
        log_result(current_step, "PASS", email)

        # -------------------------------------------------------------
        # TASK 2 - login
        # -------------------------------------------------------------
        current_step = "2. Login"

        driver.get(settings.BASE_URL + "index.php?route=account/login")
        driver.find_element(By.ID, "input-email").send_keys(email)
        driver.find_element(By.ID, "input-password").send_keys(password)
        take_screenshot(driver, "04_login_page")

        driver.find_element(By.CSS_SELECTOR, "input[value='Login']").click()
        time.sleep(settings.PAUSE)

        # a successful login lands on the account page with a "My Account" heading
        logged_in = driver.find_elements(By.XPATH, "//h2[normalize-space()='My Account']")
        assert len(logged_in) > 0, "login failed, no 'My Account' heading found"
        take_screenshot(driver, "05_logged_in")
        log_result(current_step, "PASS")

        # -------------------------------------------------------------
        # TASK 3 - search product
        # -------------------------------------------------------------
        current_step = "3. Search product"

        driver.get(settings.BASE_URL)
        driver.find_element(By.NAME, "search").send_keys(data["search_keyword"])
        driver.find_element(By.CSS_SELECTOR, "#search button").click()
        time.sleep(settings.PAUSE)

        found = driver.find_elements(By.LINK_TEXT, product_name)
        assert len(found) > 0, f"'{product_name}' not found in search results"
        take_screenshot(driver, "06_search_results")
        log_result(current_step, "PASS", "searched for: " + data["search_keyword"])

        # -------------------------------------------------------------
        # TASK 4 - add product to cart   (+ TASK 9, popup handling)
        # -------------------------------------------------------------
        current_step = "4. Add product to cart"

        # a search can return several products, so pick the button that
        # belongs to the card with our product's name
        add_button = driver.find_element(
            By.XPATH,
            f"//div[contains(@class,'product-thumb')][.//h4/a[normalize-space()='{product_name}']]"
            "//button[contains(@onclick,'cart.add')]",
        )
        add_button.click()

        # if the site ever throws a real browser alert here, accept it
        alert_seen = handle_alert_if_present(driver)
        time.sleep(settings.PAUSE)

        banner = driver.find_element(By.CSS_SELECTOR, ".alert-success").text
        assert "Success" in banner and product_name in banner, "no success banner, got: " + banner
        take_screenshot(driver, "07_added_to_cart")
        log_result(current_step, "PASS", "success banner shown")

        log_result("9. Handle popup/alert", "PASS",
                   "browser alert accepted" if alert_seen else "no browser alert appeared, banner only")

        # clear the banner so it does not cover the page in later screenshots
        close_banner(driver)

        # -------------------------------------------------------------
        # TASK 5 - update quantity
        # -------------------------------------------------------------
        current_step = "5. Update quantity"

        driver.get(settings.BASE_URL + "index.php?route=checkout/cart")
        quantity_box = driver.find_element(By.CSS_SELECTOR, "input[name^='quantity']")
        quantity_box.clear()
        quantity_box.send_keys(str(new_quantity))

        # the blue refresh button sits right next to the quantity box
        driver.find_element(
            By.XPATH,
            "//input[starts-with(@name,'quantity')]/following-sibling::span//button[contains(@class,'btn-primary')]",
        ).click()
        handle_alert_if_present(driver)
        time.sleep(settings.PAUSE)

        banner = driver.find_element(By.CSS_SELECTOR, ".alert-success").text
        assert "modified" in banner.lower(), "cart update banner missing, got: " + banner
        take_screenshot(driver, "08_quantity_updated")
        log_result(current_step, "PASS", f"quantity set to {new_quantity}")

        # -------------------------------------------------------------
        # TASK 6 - verify cart details
        # Reload the cart first, so we check what the server saved and
        # not just what the page showed after the click.
        # -------------------------------------------------------------
        current_step = "6. Verify cart details"

        driver.get(settings.BASE_URL + "index.php?route=checkout/cart")
        rows = driver.find_elements(By.CSS_SELECTOR, "#content form table tbody tr")
        assert len(rows) == 1, f"expected 1 product in the cart, found {len(rows)}"

        # columns: image | name | model | quantity | unit price | total
        cells = rows[0].find_elements(By.TAG_NAME, "td")
        cart_name = cells[1].find_element(By.TAG_NAME, "a").text.strip()
        cart_quantity = int(cells[3].find_element(By.TAG_NAME, "input").get_attribute("value"))
        unit_price = price_to_number(cells[4].text)
        line_total = price_to_number(cells[5].text)
        sub_total = price_to_number(driver.find_element(
            By.XPATH,
            "//table[contains(@class,'table') and .//strong[normalize-space()='Sub-Total:']]"
            "//strong[normalize-space()='Sub-Total:']/ancestor::tr[1]/td[last()]",
        ).text)
        cart_total = price_to_number(driver.find_element(
            By.XPATH,
            "//table[contains(@class,'table') and .//strong[normalize-space()='Total:']]"
            "//strong[normalize-space()='Total:']/ancestor::tr[1]/td[last()]",
        ).text)

        print("   cart shows:", cart_name, cart_quantity, unit_price, line_total, sub_total)

        assert cart_name == product_name, f"cart has '{cart_name}', expected '{product_name}'"
        assert cart_quantity == new_quantity, f"cart quantity is {cart_quantity}, expected {new_quantity}"
        assert round(unit_price * cart_quantity, 2) == round(line_total, 2), "unit price x quantity != total"
        assert round(line_total, 2) == round(cart_total, 2), "line total != cart total"
        assert sub_total > 0 and sub_total <= line_total, "invalid pre-tax sub-total"

        take_screenshot(driver, "09_cart_verified")
        log_result(current_step, "PASS", f"{cart_name} x {cart_quantity}, total ${line_total:.2f}")

    except Exception as error:
        # whatever broke: note which step it was, grab a screenshot, and
        # carry on to the report so we can see what happened
        message = str(error).strip().splitlines()[0] if str(error).strip() else type(error).__name__
        log_result(current_step, "FAIL", message)
        if driver is not None:
            try:
                take_screenshot(driver, "FAILED")
            except Exception:
                print("   could not take a failure screenshot (browser may have closed)")

    finally:
        # runs on success and on failure, so there is always a report
        if driver is not None:
            time.sleep(settings.PAUSE)
            driver.quit()
        write_report()


if __name__ == "__main__":
    main()
