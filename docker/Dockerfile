FROM tensorflow/tensorflow:1.8.0-devel-gpu-py3

RUN apt-get update && \
    apt-get install -y python3-pip git
RUN pip3 install pillow jupyter matplotlib

RUN cd /root && git clone https://github.com/tensorflow/models.git && \
    cd models && \
    git checkout 4b8fe70416fe4826a3bad622e56780a7c2eb330c

WORKDIR /root/models/research/deeplab

RUN git clone https://github.com/mcordts/cityscapesScripts.git && \
    cd cityscapesScripts && \
    git checkout 4031404ae3dffe901f45a91f7bb0253389284d6f && \
    cd -

ENV PYTHONPATH /root/models/research/:/root/models/research/slim:$PYTHONPATH
