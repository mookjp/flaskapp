FROM ubuntu:14.04
MAINTAINER mookjp

WORKDIR /tmp

# Install required packages
RUN apt-get install -y git
RUN apt-get install -y python
RUN apt-get install -y pip
RUN apt-get install -y curl

RUN pip install -y Flask

RUN mkdir /app
WORKDIR /app
RUN git clone https://github.com/mookjp/flaskapp
WORKDIR /app/flaskapp

EXPOSE 5000

ENTRYPOINT ["/usr/local/bin/python", "app.py"]
