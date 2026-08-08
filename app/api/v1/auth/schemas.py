from pydantic import BaseModel, Field

class LoginRequest(BaseModel):
    email: str = Field(default='hello@hello.com', description="The email address of the user.")
    password: str = Field(default='hello', description="The password of the user.")

class RegisterRequest(BaseModel):
    first_name:str = Field(default='John', description="The first name of the user.")
    last_name:str = Field(default='Doe', description="The last name of the user.")
    email: str = Field(default='hello@hello.com', description="The email address of the user.")
    password: str = Field(default='hello', description="The password of the user.")


class RegisterResponse(BaseModel):
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
