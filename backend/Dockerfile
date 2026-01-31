FROM python:3.13-slim

WORKDIR /app

COPY ../pyproject.toml ./
RUN pip install --upgrade pip
RUN pip install uv
RUN uv sync
RUN uv pip install --system --no-cache -r pyproject.toml

COPY backend .
COPY backend/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
