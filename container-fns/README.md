## Cityscapes
For Cityscapes, the recommended directory structure is

```
dataset-path: some/path/to/cityscapes
+ cityscapes
    + leftImg8bit
    + gtFine
```

The output path will have

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
$ container-fn tensorflow-deeplab-datatransfer \
      --dataset cityscapes \
      --dataset-path /mnt/ngv/datasets/cityscapes-segmentation \
      --output-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test
```

### Use container-fn to train

```
container-fn tensorflow-deeplab-train \
      --dataset-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/tfrecord \
      --output-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test
```

### PASCAL VOC 2012
For PASCAL VOC 2012, the recommended directory structure is

```
dataset-path: some/path/to/VOCdevkit
+ VOCdevkit
    + VOC2012
      + JPEGImages
      + SegmentationClass
```

The output path will have

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

### ADE20K
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

The output path will have

```
output-path: some/path/to/output
+ output
    + tfrecord
    + train_on_train_set
        + train
        + eval
        + vis
```
