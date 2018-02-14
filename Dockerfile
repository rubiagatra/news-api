FROM python:3.6-alpine

LABEL Doni Rubiagatra <rubiagatra@gmail.com>

RUN mkdir -p /news-api
WORKDIR /news-api

COPY . .

RUN pip install -r requirements.txt
EXPOSE 5000

CMD gunicorn -b 0.0.0.0:5000  --access-logfile - "newsapi.app:create_app()"


