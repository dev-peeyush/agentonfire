from pydantic import BaseModel

class LoginRequest(BaseModel):
    email: str
    password: str
    
class RegisterRequest(BaseModel):
    first_name:str
    last_name:str
    email: str
    password: str
    
    
class RegisterResposne(BaseModel):
    id:str
    email:str
    first_name:str
    last_name: str
    
class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str
    
class RefreshRequest(BaseModel):
    access_token: str
    refresh_token: str

class RefreshResponse(BaseModel):
    access_token: str
    refresh_token: str
