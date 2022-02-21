#FROM python:alpine3.7
FROM ubuntu:latest
RUN apt update && apt install python3-pip -y
RUN mkdir /apps
COPY server-app/ /apps/
WORKDIR /apps
RUN pip install -r /apps/requirements.txt
EXPOSE 8000
CMD /bin/python3 load-generator.py
