FROM tensorflow/tensorflow:1.8.0-devel-gpu-py3

RUN apt-get update && \
    apt-get install -y python3-pip git && \
    apt-get install nano

RUN pip3 install pillow jupyter matplotlib

WORKDIR /root

