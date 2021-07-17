FROM python:3.9.6-slim

RUN apt-get update \
    && apt-get install --assume-yes libpq-dev=11.12-0+deb10u1 gcc=4:8.3.0-1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements/prod.txt requirements.txt

RUN pip install --no-cache-dir --requirement requirements.txt \
    && useradd -u 1234 app_user

USER app_user

COPY --chown=app_user:app_user . .

CMD [ ".docker/entrypoint.sh" ]
