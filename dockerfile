FROM python:3

WORKDIR /usr/src/app



ADD app.py .

CMD [ "python", "./app.py" ]
