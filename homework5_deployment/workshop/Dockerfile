# FROM python:3.13.9
FROM python:3.13.9-slim-bookworm


# RUN pip install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin

WORKDIR /app

COPY ".python-version" "pyproject.toml" "uv.lock" ./

RUN uv sync --locked

COPY "initial_predict.py" "model.bin" ./

EXPOSE 9696

ENTRYPOINT ["uv", "run", "uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "9696"]