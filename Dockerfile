FROM python:3.8.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ADD . /app
WORKDIR /app
RUN ["pip", "install", "--no-cache-dir", "--upgrade", "pip"]
RUN ["pip", "install", "--no-cache-dir", "--disable-pip-version-check", "-r", "requirements.txt"]

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]

EXPOSE 8080
