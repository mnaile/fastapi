from gino.ext.starlette import Gino
from core.settings.app_factory import settings

db = Gino(dsn=settings.DATABASE_DNS)