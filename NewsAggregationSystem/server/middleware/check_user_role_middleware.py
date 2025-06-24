from fastapi import Depends, HTTPException
from NewsAggregationSystem.server.middleware.authentication_middleware import get_current_user

def admin_required(user_info=Depends(get_current_user)):
    if user_info["user_role"] == "user":
        raise HTTPException(status_code=403, detail="Admins only")
    return user_info
