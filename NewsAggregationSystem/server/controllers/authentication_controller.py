from NewsAggregationSystem.server.services.authentication_service import AuthenticationService


class AuthenticationController:

    def __init__(self):
        self.authentication_service = AuthenticationService()

    def register(self, body):
       is_register =  self.authentication_service.register(body.name, body.email, body.password)
       return is_register

    def login(self, body):
       is_login = self.authentication_service.login(body.email, body.password)
       return is_login
