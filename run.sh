nvidia-docker run -it --rm \
	-v /mnt/data/dataset/cityscapes:/mnt/data/dataset/cityscapes:ro \
	-v /mnt/data/dataset/exp:/mnt/data/dataset/exp \
	deeplab
