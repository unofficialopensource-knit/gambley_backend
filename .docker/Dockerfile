FROM python:3.9.6-slim

WORKDIR /app

COPY requirements/prod.txt requirements.txt

RUN pip install --requirement requirements.txt \
    && useradd -u 1234 app_user

USER app_user

COPY --chown=app_user:app_user . .

CMD [ ".docker/entrypoint.sh" ]
