FROM python:3.8.5-slim
WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip install poetry &&  poetry config virtualenvs.create false

COPY python_docker_sample /app/python_docker_sample

RUN cd /app/python_docker_sample \
    &&  poetry install --no-dev && cd /app

EXPOSE 8080

CMD ["uvicorn", "python_docker_sample.app:app", "--host", "0.0.0.0", "--port", "8080"]