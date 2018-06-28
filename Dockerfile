FROM python:3.6.0-slim
WORKDIR /app

ENV PYTHONUNBUFFERED=1

ADD requirements.txt /app/
RUN pip install -r /app/requirements.txt --no-cache-dir

RUN useradd myproject
RUN chown -R myproject /app
USER myproject
COPY . /app
RUN ./manage.py collectstatic --no-input

