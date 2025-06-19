from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from server.utilities.jwt_utils import JWTUtils

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    payload = JWTUtils.decode_access_token(token)
    user_info = {
        "user_id": payload.get("user_id"),
        "user_role": payload.get("user_role")
    }
    return user_info
