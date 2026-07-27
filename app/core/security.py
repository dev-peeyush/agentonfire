import jwt
from pydantic import BaseModel
from fastapi.security import HTTPBearer
from datetime import timedelta, datetime, timezone
from app.api.v1.auth.schemas import  RegisterRequest
from app.core.config import settings
from pwdlib import PasswordHash

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
password_hash = PasswordHash.recommended()

def create_access_token(data:TokenData)->Token:
    expire = datetime.now(timezone.utc) + timedelta(seconds=settings.ACCESS_TOKEN_EXPIRY_SECONDS)
    data.exp = expire
    access_token = jwt.encode(data.model_dump(), key=settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    refresh_token = create_refresh_token(
        RefreshTokenData(
            id = data.id,
            type = "refresh"
        )
    )
    return Token(
        access_token=access_token, refresh_token=refresh_token
    )
    
def create_refresh_token(data:RefreshTokenData):
    expire = datetime.now(timezone.utc) + timedelta(seconds=settings.REFRESH_TOKEN_EXPIRY_SECONDS)
    data.exp = expire
    return jwt.encode(data.model_dump(), key=settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    
def decode_access_token(jwt_token: str)->RegisterRequest:
    return jwt.decode(
        jwt_token, key=settings.JWT_SECRET_KEY, algorithms=settings.JWT_ALGORITHM
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
    
    

def hash_password(password: str) -> str:
    return password_hash.hash(password)

def verify_password(password: str, password_hash_str: str) -> bool:
    return password_hash.verify(password, password_hash_str)
    
