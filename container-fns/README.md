## Cityscapes
For Cityscapes, the recommended directory structure is

```
dataset-path: some/path/to/cityscapes
+ cityscapes
    + leftImg8bit
    + gtFine
```

The output directory structure is

```
output-path: some/path/to/output
+ output
    + tfrecord
    + train_on_train_set
        + train
        + eval
        + vis
```

### Use container-fn to convert dataset into tfrecord

Note:these examples assume you have mounted shore at `/mnt/ngv` per instructions [here](https://gitlab.eecs.umich.edu/umfordav/ngv-wiki/wikis/home).
```
container-fn tensorflow-deeplab-datatransfer \
      --dataset cityscapes \
      --dataset-path /mnt/ngv/datasets/cityscapes-segmentation \
      --output-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test
```

### Use container-fn to train

```
container-fn tensorflow-deeplab-train \
      --dataset-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/tfrecord \
      --output-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/train_on_train_set
```

### Use container-fn to evaluate
```
container-fn tensorflow-deeplab-eval \
      --dataset-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/tfrecord \
      --trained-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/train_on_train_set/train \
      --output-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/train_on_train_set
```

### Use container-fn to visualize
```
container-fn tensorflow-deeplab-vis \
      --dataset-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/tfrecord \
      --trained-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/train_on_train_set/train \
      --output-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/train_on_train_set
```

## PASCAL VOC 2012
For PASCAL VOC 2012, the recommended directory structure is

```
dataset-path: some/path/to/VOCdevkit
+ VOCdevkit
    + VOC2012
      + JPEGImages
      + SegmentationClass
```

The output directory structure is

```
output-path: some/path/to/output
+ output
    + SegmentationClassRaw
    + tfrecord
    + train_on_train_set
        + train
        + eval
        + vis
```
### Use container-fn to convert dataset into tfrecord

Note:these examples assume you have mounted shore at `/mnt/ngv` per instructions [here](https://gitlab.eecs.umich.edu/umfordav/ngv-wiki/wikis/home).
```
container-fn tensorflow-deeplab-datatransfer \
      --dataset pascal_voc_seg \
      --dataset-path None \
      --output-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test
```

If `dataset-path` is set as `None`, the container-fn will automatically download PASCAL VOC 2012 dataset to the `output-path` and convert it to tfrecord format. If `dataset-path` is set as `some/path/to/VOCdevkit`, then container-fn will only convert it to tfrecord format.

### Use container-fn to train

```
container-fn tensorflow-deeplab-train \
      --dataset-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/tfrecord \
      --output-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/train_on_train_set
```

### Use container-fn to evaluate
```
container-fn tensorflow-deeplab-eval \
      --dataset-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/tfrecord \
      --trained-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/train_on_train_set/train \
      --output-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/train_on_train_set
```

### Use container-fn to visualize
```
container-fn tensorflow-deeplab-vis \
      --dataset-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/tfrecord \
      --trained-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/train_on_train_set/train \
      --output-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/train_on_train_set
```

## ADE20K
For ADE20K, the recommended directory structure is

```
dataset-path: some/path/to/ADEChallengeData2016
+ ADEChallengeData2016
    + annotations
      + training
      + validation
    + images
      + training
      + validation
```

The output directory structure is

```
output-path: some/path/to/output
+ output
    + tfrecord
    + train_on_train_set
        + train
        + eval
        + vis
```

### Use container-fn to convert dataset into tfrecord

Note:these examples assume you have mounted shore at `/mnt/ngv` per instructions [here](https://gitlab.eecs.umich.edu/umfordav/ngv-wiki/wikis/home).
```
container-fn tensorflow-deeplab-datatransfer \
      --dataset ade20k\
      --dataset-path None \
      --output-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test
```

If `dataset-path` is set as `None`, the container-fn will automatically download ADE20K dataset to the `output-path` and convert it to tfrecord format. If `dataset-path` is set as `some/path/to/ADEChallengeData2016`, then container-fn will only convert it to tfrecord format.

### Use container-fn to train

```
container-fn tensorflow-deeplab-train \
      --dataset-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/tfrecord \
      --output-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/train_on_train_set \
      --pretrained-path ${PATH_TO_PRETRAINED_MODEL}
```

For now, Deeplab does not have a pretrained model for ADE20K. So it is supposed to set ${PATH_TO_PRETRAINED_MODEL} as the directory where a pretraind model for ADE20K dataset resides.

### Use container-fn to evaluate
```
container-fn tensorflow-deeplab-eval \
      --dataset-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/tfrecord \
      --trained-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/train_on_train_set/train \
      --output-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/train_on_train_set
```

### Use container-fn to visualize
```
container-fn tensorflow-deeplab-vis \
      --dataset-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/tfrecord \
      --trained-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/train_on_train_set/train \
      --output-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/train_on_train_set
```
