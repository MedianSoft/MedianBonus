FROM python:3.13-slim

WORKDIR /

COPY ../pyproject.toml ./
RUN pip install --upgrade pip
RUN pip install uv
RUN uv sync
RUN uv pip install --system --no-cache -r pyproject.toml

COPY backend .

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
