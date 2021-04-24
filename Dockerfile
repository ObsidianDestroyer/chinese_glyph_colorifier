FROM python:3.8-slim

WORKDIR usr/src/app
COPY Pipfile* ./

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc python-dev build-essential pipenv && \
    pipenv install --deploy --system && \
    apt-get remove -y gcc python-dev && \
    apt-get autoremove -y

COPY . /usr/src/app

EXPOSE 2731

CMD ["uvicorn", "main:make_application", "--host", "glypher", "--factory", "--port", "2731", "--forwarded-allow-ips='*'"]
