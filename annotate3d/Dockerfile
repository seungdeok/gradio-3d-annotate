FROM node:20.5.0

WORKDIR /app


RUN apt-get update && \
    apt-get install -y python3-pip

RUN rm /usr/lib/python3.11/EXTERNALLY-MANAGED

RUN python3 -m pip install --no-cache-dir gradio==5 numpy