from fastapi import APIRouter, Body
from server.controllers.authentication_controller import AuthenticationController
from server.dtos.requests.user_login_request_dto import UserSignInRequest
from server.dtos.requests.user_register_request_dto import UserRegisterRequest


router = APIRouter(prefix="/api/auth")
authenticate_controller = AuthenticationController()

@router.post("/register")
async def register(body: UserRegisterRequest = Body(...)):
        return authenticate_controller.register(body)

@router.post("/login")
async def login(body: UserSignInRequest = Body(...)):
        return authenticate_controller.login(body)