FROM python:3.8

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY . .

EXPOSE 8000
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:$PORT ryosai.wsgi"]
