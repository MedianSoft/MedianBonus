from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    host: str
    port: int
    name: str
    user: str
    password: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="db_",
        case_sensitive=False,
        extra="ignore",
    )

    @property
    def dsn(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{self.user}:{self.password}"
            f"@{self.host}:{self.port}/{self.name}"
        )


database_settings = DatabaseSettings()  # type: ignore
