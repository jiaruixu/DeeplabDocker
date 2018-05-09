FROM tensorflow/tensorflow:1.8.0-devel-gpu-py3

RUN apt-get update && \
    apt-get install -y python3-pip git
RUN pip3 install pillow jupyter matplotlib
WORKDIR /
RUN git clone https://github.com/tensorflow/models.git && \
    cd models && \
    git checkout 4b8fe70416fe4826a3bad622e56780a7c2eb330c
WORKDIR /models/research/deeplab
ENV PYTHONPATH /models/research/:/models/research/slim:$PYTHONPATH
