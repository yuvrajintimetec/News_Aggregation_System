from menu.authentication_menu import AuthenticationMenu

if __name__ == "__main__":
    while True:
        auth_menu = AuthenticationMenu()
        role_menu = auth_menu.api_request()
        result = role_menu.api_request()
        if result == "logout":
            continue
        else:
            break
