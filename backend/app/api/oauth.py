from app.core.config import settings
from authlib.integrations.starlette_client import OAuth
from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse

router = APIRouter()
oauth = OAuth()

oauth.register(
    name="github",
    client_id=settings.github_client_id,
    client_secret=settings.github_client_secret,
    access_token_url="https://github.com/login/oauth/access_token",
    authorize_url="https://github.com/login/oauth/authorize",
    client_kwargs={"scope": "user:email"},
)

oauth.register(
    name="yandex",
    client_id=settings.yandex_client_id,
    client_secret=settings.yandex_client_secret,
    authorize_url="https://oauth.yandex.com/authorize",
    access_token_url="https://oauth.yandex.com/token",
    client_kwargs={"scope": "login:email login:info"},
)


@router.get("/auth/github/login")
async def github_login(request: Request):
    redirect_uri = "http://localhost:8000/auth/github/callback"
    return await oauth.github.authorize_redirect(request, redirect_uri)


@router.get("/auth/github/callback")
async def github_callback(request: Request):
    token = await oauth.github.authorize_access_token(request)
    user = None
    if token:
        resp = await oauth.github.get("https://api.github.com/user", token=token)
        user = resp.json()
    return {"token": token, "user": user}


@router.get("/auth/yandex/login")
async def yandex_login(request: Request):
    redirect_uri = "http://localhost:8000/auth/yandex/callback"
    return await oauth.yandex.authorize_redirect(request, redirect_uri)


@router.get("/auth/yandex/callback")
async def yandex_callback(request: Request):
    token = await oauth.yandex.authorize_access_token(request)
    user = None
    if token:
        resp = await oauth.yandex.get("https://login.yandex.ru/info", token=token)
        user = resp.json()
    return {"token": token, "user": user}
