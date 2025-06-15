from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    mongo_uri: str = "mongodb://localhost:27017/"
    mongo_db: str = "auth"
    env: str = "development"
    secret_key: str = "KuKod124df3545asd123"

    class Config:
        env_file = ".env"

settings = Settings()
