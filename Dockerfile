FROM ubuntu:trusty

ENV DEBIAN_FRONTEND noninteractive

RUN echo "Asia/Tehran" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

RUN chsh -s /bin/bash

RUN echo "deb http://ir.archive.ubuntu.com/ubuntu/ trusty main restricted universe" > /etc/apt/sources.list
RUN echo "deb http://ir.archive.ubuntu.com/ubuntu/ trusty-updates main restricted universe" >> /etc/apt/sources.list
RUN echo "deb http://security.ubuntu.com/ubuntu trusty-security main restricted universe" >> /etc/apt/sources.list

RUN dpkg --add-architecture i386
RUN apt-get -qq update && apt-get -qq upgrade

RUN apt-get -qq install default-jre build-essential python3 python3-pip

WORKDIR /home/library
ADD . /home/library
RUN pip3 install -r /home/library/requirements.txt

CMD ["./docker-entrypoint.sh"]
