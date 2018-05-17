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

### Use container-fn to train

```
container-fn tensorflow-deeplab-train \
      --pretrained-path /mnt/ngv/pretrained-networks/deeplabv3/deeplabv3_xception_65_cityscapes_train \
      --dataset-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/cityscapes/tfrecord \
      --output-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/cityscapes/train_on_train_set
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

### Use container-fn to train

```
container-fn tensorflow-deeplab-train \
      --train-split trainval \
      --dataset pascal_voc_seg \
      --training-steps 1000 \
      --train-crop-size-height 513 \
      --train-crop-size-width 513 \
      --pretrained-path /mnt/ngv/pretrained-networks/deeplabv3/deeplabv3_xception_65_pascal_voc_seg_trainval \
      --dataset-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/pascal/tfrecord \
      --output-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/pascal/train_on_train_set
```
