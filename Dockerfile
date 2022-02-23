FROM python:3.9-alpine3.13

RUN pip install --upgrade pip
ADD ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP "app.py"
ENV FLASK_DEBUG True
ENV FLASK_RUN_PORT 5000
ENV PYTHONPATH /app

ADD ./ /app
WORKDIR /app
EXPOSE 5000

CMD flask run --host=0.0.0.0
