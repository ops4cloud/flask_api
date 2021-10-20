[![Docker Image CI](https://github.com/ops4cloud/flask_api/actions/workflows/docker-image.yml/badge.svg)](https://github.com/ops4cloud/flask_api/actions/workflows/docker-image.yml)

# Flask_api

- Made for myself to create simple and protected backend with mongo and JWT token Auth

## Pré-requis 

 - Python3
 - virtualenv
 - nvm
 - npm
 - pm2
 - docker
 - docker-compose

## Dépedencies

 - mongodb/docker

## Installing API Venv

```bash
~# cd flask_api
~# virtualenv -p python3 venv
~# source venv/bin/activate
~# pip install -r requierements.txt
~# python setup.py develop
```

## Docker

```bash
docker build --pull --rm -f "Dockerfile" -t flaskapi:latest "."
```

## Docker-Compose

```bash
sudo echo "127.0.0.1     apiv1" >> /etc/hosts
docker build --pull --rm -f "Dockerfile" -t flaskapi:latest "."
docker-compose up
```
