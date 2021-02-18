from core.settings.settings import Base, app_config, config
from starlette.datastructures import Secret


class DevSettings(Base):
    
    DEBUG = config('DEBUG', cast=bool, default=True)
    INCLUDE_SCHEMA=config("INCLUDE_SCHEMA", cast=bool, default=False)

    DB_NAME = config("DB_NAME", cast=str, default='fastapi_user')
    DB_PORT = config("DB_PORT", cast=int, default=5432)
    DB_HOST  = config("DB_HOST", cast=str, default='localhost')
    DB_PASSWORD = config("DB_PASSWORD", cast=Secret, default='')
    DB_USER = config("DB_USER", cast=str, default="naile")


    DATABASE_DNS = f"asyncpg:///{DB_NAME}"