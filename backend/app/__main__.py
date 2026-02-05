import uvicorn

from app.server import create_app
from app.setting.app import app_settings

app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "app.__main__:app",
        host=app_settings.host,
        port=app_settings.port,
        reload=False,
    )
