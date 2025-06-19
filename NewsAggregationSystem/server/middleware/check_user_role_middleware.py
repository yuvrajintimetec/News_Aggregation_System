from fastapi import Depends, HTTPException
from server.middleware.authentication_middleware import get_current_user

def admin_required(user_info=Depends(get_current_user)):
    if user_info["role"] == "admin":
        raise HTTPException(status_code=403, detail="Admins only")
    return user_info
