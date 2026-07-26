import jwt
from pydantic import BaseModel
from fastapi.security import HTTPBearer
from datetime import timedelta, datetime, timezone
from app.api.v1.auth.schemas import  RegisterRequest

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30
ACCESS_TOKEN_EXPIRY_SECONDS = 180
REFRESH_TOKEN_EXPIRY_SECONDS = 1800


class Token(BaseModel):
    access_token: str
    refresh_token:str
    

class TokenData(BaseModel):
    first_name: str
    last_name: str
    email: str
    id:str
    type: str
    exp: datetime = None
    
class RefreshTokenData(BaseModel):
    id: str
    type: str
    exp: datetime = None
    
    
authSchema = HTTPBearer()


def create_access_token(data:TokenData)->Token:
    expire = datetime.now(timezone.utc) + timedelta(seconds=ACCESS_TOKEN_EXPIRY_SECONDS)
    data.exp = expire
    access_token = jwt.encode(data.model_dump(), key=SECRET_KEY, algorithm=ALGORITHM)
    refresh_token = create_refresh_token(
        RefreshTokenData(
            id="123",
            type="refresh"
        )
    )
    return Token(
        access_token=access_token, refresh_token=refresh_token
    )
    
def create_refresh_token(data:RefreshTokenData):
    expire = datetime.now(timezone.utc) + timedelta(seconds=REFRESH_TOKEN_EXPIRY_SECONDS)
    data.exp = expire
    return jwt.encode(data.model_dump(), key=SECRET_KEY, algorithm=ALGORITHM)
    
def decode_access_token(jwt_token: str)->RegisterRequest:
    return jwt.decode(
        jwt_token, key=SECRET_KEY, algorithms=ALGORITHM
    )

def validate_access_token(access_token: str):
    try:
        payload = decode_access_token(access_token)

        if payload.get("type") != "access":
            raise ValueError("Invalid token type")

        return payload

    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")

    except jwt.InvalidTokenError:
        raise ValueError("Invalid token")
    
    



