FROM python:3.12.3-slim-bookworm

RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

RUN apt-get update \
	&& apt-get install --yes --show-progress --verbose-versions vim

COPY . /usr/local/src
WORKDIR /usr/local/src

RUN pip install --upgrade pip \
	&& pip install --requirement requirements.txt
