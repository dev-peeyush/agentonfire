from app.api.v1.auth.schemas import LoginRequest, RefreshRequest, RegisterRequest
from fastapi import Request, HTTPException
from app.core.security import create_access_token, TokenData, decode_access_token
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.db.models.user import User

class AuthService:
    def __init__(self, db: Session):
        self.db = db
        
    async def login(self, request:LoginRequest):
        
        user = self.db.scalar(select(User).where(User.email == request.email))
        if user == None: 
            raise HTTPException(
                status_code=401,detail="Incorrect email or password"
            )

        return create_access_token(TokenData(
                    first_name=user.first_name,
                    last_name=user.last_name,
                    email=user.email,
                    id =user.id,
                    type='access'
                ))
    
    async def register(self, request: RegisterRequest):
        
        print(f"New Registration User {request}")
        user = User(
            first_name = request.first_name,
            last_name = request.last_name,
            email = request.email
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    async def refresh(self, request: RefreshRequest):
        return request
    
    async def me(self, request:Request):
        return decode_access_token()