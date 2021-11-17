import uvicorn

from fastapi import FastAPI
from sqlalchemy.orm import scoped_session
from server.database.connection import db, Base
from server.common.const import get_settings
from server.router import index
from server.database.models.mixin.base import BaseMixin

settings = get_settings()

def create_db_table() -> None:
    try:
        session = next(db.session())
        Base.metadata.create_all(db._engine)
    finally:
        session.close()

def app_generator() -> FastAPI:
    app = FastAPI()
    database_url = f'postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}'
    db.init_app(app, DB_URL=database_url)
    session = next(db.get_db()) if not db._session else scoped_session(db._session)
    BaseMixin.set_session(session)
    create_db_table()

    app.include_router(index.router, prefix="/api")

    return app