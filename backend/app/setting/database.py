from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    dsn: str
    name: str
    user: str
    password: str
    port: int

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="db_",
        case_sensitive=False,
        extra="ignore",
    )


database_settings = DatabaseSettings()  # type: ignore
