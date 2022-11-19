from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "SKY-DNE API"
    user_name: str
    password: str

    class Config:
        env_file = ".env"