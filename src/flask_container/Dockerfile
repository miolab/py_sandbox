FROM python:3.11.0-slim

WORKDIR /usr/src/app
ENV FLASK_APP=index

COPY . ./

RUN pip install --upgrade pip
RUN pip install flask

CMD [ "flask", "run", "--host=0.0.0.0" ]
