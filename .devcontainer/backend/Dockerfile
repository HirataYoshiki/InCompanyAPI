FROM python:3.8-buster

LABEL maintainer="kirryx2@gmail.com"
LABEL version="1.0"
LABEL description="python-fastapi(sqlalcemy(MySQL):Vue.js)"

RUN apt-get update && apt-get install -y \
tzdata \
&& rm -rf var/lib/apt/lists/*

ENV TZ=Asia/Tokyo

WORKDIR /tmp/dev/backend
COPY requirements.txt ${PWD}
RUN pip install -r requirements.txt
