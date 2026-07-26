from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_Name: str = "Agent on Fire"
    DEBUG: bool = False
    HOST: str
    PORT: int
    OPENAI_API_KEY:str
    DATABASE_URI:str
    
    model_config = SettingsConfigDict(
        env_file= '.env',
        extra='ignore'
    )
    
    
settings = Settings()