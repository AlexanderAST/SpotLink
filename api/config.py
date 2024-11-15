from typing import NamedTuple
from environs import Env


class DB(NamedTuple):
    URL: str
    POOL_SIZE: int
    POOL_ECHO: bool


class Config(NamedTuple):
    DB:DB

def load_config() -> Config:
    def db_url(user:str, pwd:str, host:str, port:str, db:str) -> str:
        return f"postgresql+asyncpg://{user}:{pwd}@{host}:{port}/{db}"
    
    def api_url(url:str ,api_key: str) -> str:
        return f"{url}/{api_key}"
    
    env = Env()
    env.read_env(override=True)

    return Config(
        DB(
            db_url(
            env.str("DB_USER"),
            env.str("DB_PWD"),
            env.str("DB_HOST"),
            env.str("DB_PORT"),
            env.str("DB_NAME")
            ),
            env.int("DB_POOL_SIZE"),
            env.bool("DB_POOL_ECHO")
        )
    )