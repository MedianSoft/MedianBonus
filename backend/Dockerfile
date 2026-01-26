FROM python:3.13-slim

WORKDIR /app

COPY ../pyproject.toml uv.lock ./
RUN pip install --upgrade pip
RUN pip install uv
RUN uv pip install --system --no-cache -r pyproject.toml

COPY . .

CMD ["python", "-m", "app"]
