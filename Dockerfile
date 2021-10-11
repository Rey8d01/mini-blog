FROM python:3.9-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

VOLUME /usr/src/app/tmp

COPY ./api ./api
COPY ./config ./config
COPY ./core ./core
COPY ./main.py .
COPY ./startup.py .
COPY ./start.sh .
RUN chmod +x ./start.sh

CMD ["./start.sh"]
