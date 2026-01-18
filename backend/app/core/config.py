from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    github_client_id: str
    github_client_secret: str
    yandex_client_id: str
    yandex_client_secret: str
    auth_service_url: str
    secret_key: str


settings = Settings()
