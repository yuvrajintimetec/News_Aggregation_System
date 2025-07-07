from fastapi import APIRouter, Body
from NewsAggregationSystem.server.controllers.authentication_controller import AuthenticationController
from NewsAggregationSystem.server.dtos.requests.user_login_request import UserSignInRequest
from NewsAggregationSystem.server.dtos.requests.user_register_request import UserRegisterRequest
from NewsAggregationSystem.server.dtos.responses.login_response import LoginResponse
from NewsAggregationSystem.server.dtos.responses.register_response import RegisterResponse


router = APIRouter(prefix="/api/auth")
authenticate_controller = AuthenticationController()

@router.post("/register", response_model=RegisterResponse)
async def register(body: UserRegisterRequest = Body(...)):
        return authenticate_controller.register(body)

@router.post("/login", response_model=LoginResponse)
async def login(body: UserSignInRequest = Body(...)):
        return authenticate_controller.login(body)