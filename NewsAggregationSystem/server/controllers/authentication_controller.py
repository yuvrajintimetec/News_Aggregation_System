from NewsAggregationSystem.server.services.authentication_service import AuthenticationService


class AuthenticationController:

    def __init__(self):
        self.authentication_service = AuthenticationService()

    def register(self, body):
       register_response =  self.authentication_service.register(body.name, body.email, body.password)
       return register_response

    def login(self, body):
       login_response = self.authentication_service.login(body.email, body.password)
       return login_response
