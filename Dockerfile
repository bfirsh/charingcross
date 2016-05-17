FROM python:2.7-alpine
ENV PYTHONUNBUFFERED 1
RUN apk add --no-cache ca-certificates libpq
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN apk add --no-cache musl-dev gcc postgresql postgresql-dev && \
    pip install -r requirements.txt && \
    apk del --purge musl-dev gcc postgresql postgresql-dev
ADD . /code/
RUN SECRET_KEY=unset ./manage.py collectstatic --no-input
CMD gunicorn charingcross.wsgi -b 0.0.0.0:8000 --log-file - --access-logfile - -k eventlet --workers 4 --worker-connections 5
