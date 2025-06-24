from menu.authentication_menu import AuthenticationMenu

if __name__ == "__main__":
    auth_menu = AuthenticationMenu()
    role_menu = auth_menu.api_request()
    role_menu.api_request()
