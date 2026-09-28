class Application:

    def __init__(self):
        self.username = ""
        self.password = ""
        self.current_page = "login"
        self.error_message = ""
        self.running = False

    def start(self):
        self.running = True
        self.current_page = "login"
        self.error_message = ""

    def enter_username(self, username):
        self.username = username

    def enter_password(self, password):
        self.password = password

    def login(self):
        if self.username == "admin" and self.password == "admin123":
            self.current_page = "dashboard"
            self.error_message = ""
        else:
            self.current_page = "login"
            self.error_message = "Invalid username or password"

    def stop(self):
        self.running = False
