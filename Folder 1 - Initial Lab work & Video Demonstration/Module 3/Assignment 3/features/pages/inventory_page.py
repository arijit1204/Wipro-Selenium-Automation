class InventoryPage:

    def __init__(self, driver):
        self.driver = driver

    def is_open(self):
        return "/inventory.html" in self.driver.current_url
