FROM python:3.9-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

VOLUME /usr/src/app/tmp

COPY ./main.py .
COPY ./start.sh .
RUN chmod +x ./start.sh

CMD ["./start.sh"]
