FROM python:3.8-buster

LABEL maintainer="kirryx2@gmail.com"
LABEL version="1.0"
LABEL description="python-fastapi(sqlalcemy(MySQL):Vue.js)"

RUN apt-get update && apt-get install -y \
tzdata \
&& rm -rf var/lib/apt/lists/*

WORKDIR /tmp/work

ENV TZ=Asia/Tokyo
ENV USER=user1


RUN useradd -m ${USER} --uid 1000
RUN gpasswd -a ${USER} sudo
RUN echo "${USER}:password" | chpasswd

USER ${USER}
WORKDIR /home/${USER}/dev/backend
COPY requirements.txt ${PWD}
ARG VENV="myenv"
RUN python3 -m venv $VENV && \
. ./$VENV/bin/activate && \
pip install -r requirements.txt
