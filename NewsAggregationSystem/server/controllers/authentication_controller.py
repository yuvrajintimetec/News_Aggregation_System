from NewsAggregationSystem.server.exceptions.invalid_credential_exception import InvalidCredentialsException
from NewsAggregationSystem.server.exceptions.user_already_exist_exception import UserAlreadyExistsException
from NewsAggregationSystem.server.services.authentication_service import AuthenticationService
from fastapi import HTTPException, status


class AuthenticationController:

    def __init__(self):
        self.authentication_service = AuthenticationService()

    def register(self, body):
       try:
           is_register =  self.authentication_service.register(body.name, body.email, body.password)
           return is_register
       except UserAlreadyExistsException as e:
           raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))


    def login(self, body):
       try:
           is_login = self.authentication_service.login(body.email, body.password)
           return is_login
       except InvalidCredentialsException as e:
           raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
