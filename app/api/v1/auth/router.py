from fastapi import APIRouter, Depends, Request
from app.api.v1.auth.service import AuthService
from app.api.v1.auth.schemas import LoginRequest, RefreshRequest, RegisterRequest
from app.core.deps import get_current_user
from sqlalchemy.orm import Session
from app.db.engine import get_db

router = APIRouter(prefix='/auth', tags=["Authentication"])

def get_auth_service(
    db: Session = Depends(get_db),
) -> AuthService:
    return AuthService(db)

@router.post('/register')
async def register(request: RegisterRequest, auth_service: AuthService = Depends(get_auth_service)):
    return await auth_service.register(request=request)


@router.post('/login')
async def login(request: LoginRequest, auth_service: AuthService = Depends(get_auth_service)):
    return await auth_service.login(request=request)

@router.post('/refresh')
async def refresh(request: RefreshRequest,get_current_user = Depends(get_current_user), auth_service:AuthService = Depends(get_auth_service)):
    print(f"is authtokenvalid f{request.refresh_token}")
    return await auth_service.refresh(request=request)

@router.get('/me')
async def me(get_current_user = Depends(get_current_user)):
    return get_current_user