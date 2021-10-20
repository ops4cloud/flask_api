FROM keymetrics/pm2
RUN apk add --no-cache --update python3 py3-pip gcc python3-dev musl-dev g++
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN python3 setup.py develop
CMD pm2-runtime ecosystem.config.js
EXPOSE 8888