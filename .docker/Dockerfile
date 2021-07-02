FROM python:3.9.6-slim

WORKDIR /app

COPY requirements/prod.txt requirements.txt

RUN pip install --requirement requirements.txt

COPY . .

CMD [ ".docker/entrypoint.sh" ]
