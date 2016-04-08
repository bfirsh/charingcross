FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
RUN SECRET_KEY=unset ./manage.py collectstatic --no-input
CMD gunicorn charingcross.wsgi -b 0.0.0.0:8000 --log-file - --access-logfile -
