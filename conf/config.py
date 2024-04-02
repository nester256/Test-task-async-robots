''' Defines application settings using Pydantic's BaseSettings. '''

from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    """
    A Pydantic BaseSettings subclass to manage application settings.

    Attributes:
    - BIND_IP (str): The IP address to bind the server to.
    - BIND_PORT (int): The port number to bind the server to.
    - DB_URL (str): The URL of the database.
    - PAGE_SIZE (int, optional): The default page size for pagination. Defaults to 2.
    """

    BIND_IP: str
    BIND_PORT: int
    DB_URL: str
    PAGE_SIZE: int = 2


settings = Settings()
