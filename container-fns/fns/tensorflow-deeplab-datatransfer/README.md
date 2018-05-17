## Use Cityscapes dataset
For Cityscapes, the recommended directory structure is

```
dataset-path: some/path/to/cityscapes
+ cityscapes
    + leftImg8bit
    + gtFine
```

The output directory structure will be

```
output-path: some/path/to/output
+ output
    + tfrecord
    + train_on_train_set
        + train
        + eval
        + vis
```

For example, the output path here would be

```
output-path: /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/cityscapes
+ 2018-05-09-tensorflow-deeplab-test/cityscapes
    + tfrecord
    + train_on_train_set
        + train
        + eval
        + vis
```

### Use container-fn to convert dataset into tfrecord

Note: these examples assume you have mounted shore at `/mnt/fcav` refering to instructions [here](https://gitlab.eecs.umich.edu/umfordav/ngv-wiki/wikis/home).
```
container-fn tensorflow-deeplab-datatransfer \
      --dataset cityscapes \
      --dataset-path /mnt/fcav/datasets/cityscapes \
      --output-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/cityscapes
```

## Use PASCAL VOC 2012 dataset
For PASCAL VOC 2012, the recommended directory structure is

```
dataset-path: some/path/to/VOCdevkit
+ VOCdevkit
    + VOC2012
      + JPEGImages
      + SegmentationClass
```

The output directory structure will be

```
output-path: some/path/to/output
+ output
    + VOC2012
        + SegmentationClassRaw
    + tfrecord
    + train_on_train_set
        + train
        + eval
        + vis
```
### Use container-fn to convert dataset into tfrecord

Note: these examples assume you have mounted shore at `/mnt/ngv` per instructions [here](https://gitlab.eecs.umich.edu/umfordav/ngv-wiki/wikis/home).
```
container-fn tensorflow-deeplab-datatransfer \
      --dataset pascal_voc_seg \
      --dataset-path /mnt/ngv/datasets/VOC/VOCdevkit \
      --output-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/pascal
```

If `dataset-path` is set as `None`, the container-fn will automatically download PASCAL VOC 2012 dataset to the `output-path` and convert it to tfrecord format. If `dataset-path` is set as `some/path/to/VOCdevkit`, then container-fn will only convert it to tfrecord format.
