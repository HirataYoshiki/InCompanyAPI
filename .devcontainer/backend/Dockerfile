FROM python:3.8-slim

RUN apt-get update && apt-get install -y \
tzdata \
&& rm -rf var/lib/apt/lists/*

WORKDIR /tmp/work

ENV TZ=Asia/Tokyo
ENV PIPENV_VENV_IN_PROJECT true
ENV USER user1

RUN pip install pipenv 


RUN useradd -m ${USER} --uid 1000
RUN gpasswd -a ${USER} sudo
RUN echo "${USER}:password" | chpasswd

USER ${USER}
WORKDIR /home/${USER}/dev

