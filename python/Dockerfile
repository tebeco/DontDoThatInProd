FROM python:3.7-slim-stretch

RUN pip install flask
COPY . .

ENV FLASK_APP=hello.py

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]
