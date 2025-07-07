from jose import JWTError, jwt, ExpiredSignatureError
from datetime import datetime, timedelta
from fastapi import HTTPException, status
from NewsAggregationSystem.server.utilities.logger import logger


SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

class JWTUtils:

    @staticmethod
    def create_access_token(data: dict, expires_delta: timedelta = None):
        to_encode = data.copy()
        expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        logger.info(f"JWT access token created for data: {data}")
        return encoded_jwt

    @staticmethod
    def decode_access_token(token: str):
        if not token:
            logger.warning("Token missing during decode attempt.")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token missing")

        try:
            logger.info("Decoding JWT access token.")
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except ExpiredSignatureError:
            logger.warning("JWT token expired during decode.")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
        except JWTError:
            logger.warning("Invalid JWT token during decode.")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

