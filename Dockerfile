FROM python:3

WORKDIR /usr/src/app

COPY app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


COPY app/ .
COPY .models/ .

CMD [ "python", "./main.py" ]
