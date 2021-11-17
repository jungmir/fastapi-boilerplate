from typing import List, Optional, Any, Dict
from pydantic import BaseSettings
from functools import lru_cache
from os import path, environ
from pathlib import Path

# base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))
base_dir = Path(__file__).parent.parent.parent

class Settings(BaseSettings):
    # basic config
    DEVELOP: bool
    API_ENV: str
    
    # database config
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    
    # secret config
    SECRET_KEY: str
    
    # logging config
    LOG_EXPIRE: int # unit: days
    LOG_MAX_SIZE: int # unit: MB
    
    class Config:
        env_file = str(base_dir / '.env')
        env_file_encoding = 'utf-8'

        @classmethod
        def customise_sources(
            cls,
            init_settings,
            env_settings,
            file_secret_settings,
        ):
            return (
                init_settings,
                env_settings,
                file_secret_settings,
            )
            
@lru_cache()
def get_settings() -> Any:
    return Settings()