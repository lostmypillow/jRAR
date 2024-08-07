FROM python:3-slim-buster

# FROM python:3-slim-buster

EXPOSE 8001

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ARG SECRET_KEY
ENV SECRET_KEY = ${SECRET_KEY}

COPY requirements.txt .
RUN python -m pip install -r requirements.txt


WORKDIR /app


COPY . /app


RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser


CMD ["gunicorn", "--bind", "0.0.0.0:8001", "jrar.wsgi"]
