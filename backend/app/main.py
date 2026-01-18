from app.api import oauth
from app.core.config import settings
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
app.add_middleware(SessionMiddleware, settings.secret_key)

app.include_router(oauth.router)
