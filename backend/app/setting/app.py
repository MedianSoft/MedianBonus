from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    host: str
    port: int
    env: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="be_",
        case_sensitive=False,
        extra="ignore",
    )

    @property
    def url(self) -> str:
        return f"{self.host}:{self.port}"


app_settings = AppSettings()  # type: ignore
