from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    BIND_IP: str
    BIND_PORT: int
    DB_URL: str


settings = Settings()
