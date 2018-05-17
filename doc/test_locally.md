```
sudo mount shore.engin.umich.edu:/volume2/UMFORDAVDATA /mnt/ngv
```
## Cityscapes
### transfer
```
container-fn tensorflow-deeplab-datatransfer \
      --dataset cityscapes \
      --dataset-path /mnt/data/dataset/exp1/cityscapes-segmentation \
      --output-path /mnt/data/dataset/exp1/cityscapes
```

### train
```
container-fn tensorflow-deeplab-train \
      --pretrained-path /mnt/ngv/pretrained-networks/deeplabv3/deeplabv3_xception_65_cityscapes_train \
      --dataset-path /mnt/data/dataset/exp1/cityscapes/tfrecord \
      --output-path /mnt/data/dataset/exp1/cityscapes/train_on_train_set
```

### evaluate
```
container-fn tensorflow-deeplab-eval \
      --dataset-path /mnt/data/dataset/exp1/cityscapes/tfrecord \
      --trained-path /mnt/data/dataset/exp1/cityscapes/train_on_train_set/train \
      --output-path /mnt/data/dataset/exp1/cityscapes/train_on_train_set
```

### visualize
```
container-fn tensorflow-deeplab-vis \
      --dataset-path /mnt/data/dataset/exp1/cityscapes/tfrecord \
      --trained-path /mnt/data/dataset/exp1/cityscapes/train_on_train_set/train \
      --output-path /mnt/data/dataset/exp1/cityscapes/train_on_train_set
```
## ADE20K
### transfer
```
container-fn tensorflow-deeplab-datatransfer \
      --dataset ade20k \
      --dataset-path None \
      --output-path /mnt/data/dataset/exp1/ade20k
```

### train
```
container-fn tensorflow-deeplab-train \
      --train-split train \
      --dataset ade20k \
      --training-steps 1000 \
      --train-crop-size-height 513 \
      --train-crop-size-width 513 \
      --resize-factor 16 \
      --min-resize-value 350 \
      --max-resize-value 500 \
      --initialize-last-layer False \
      --last-layers-contain-logits-only True \
      --pretrained-path /mnt/ngv/pretrained-networks/deeplabv3/deeplabv3_pascal_train_aug \
      --dataset-path /mnt/data/dataset/exp1/ade20k/tfrecord \
      --output-path /mnt/data/dataset/exp1/ade20k/train_on_train_set
```

### evaluate
```
container-fn tensorflow-deeplab-eval \
      --dataset ade20k \
      --eval-crop-size-height 545 \
      --eval-crop-size-width 684 \
      --resize-factor 16 \
      --min-resize-value 350 \
      --max-resize-value 700 \
      --dataset-path /mnt/data/dataset/exp1/ade20k/tfrecord \
      --trained-path /mnt/data/dataset/exp1/ade20k/train_on_train_set/train \
      --output-path /mnt/data/dataset/exp1/ade20k/train_on_train_set

      container-fn tensorflow-deeplab-eval \
            --dataset ade20k \
            --eval-crop-size-height 2113 \
            --eval-crop-size-width 2113 \
            --dataset-path /mnt/data/dataset/exp1/ade20k/tfrecord \
            --trained-path /mnt/data/dataset/exp1/ade20k/train_on_train_set/train \
            --output-path /mnt/data/dataset/exp1/ade20k/train_on_train_set
```

### visualization



## PASCAL VOC 2012
### transfer
```
container-fn tensorflow-deeplab-datatransfer \
      --dataset pascal_voc_seg \
      --dataset-path /mnt/data/dataset/exp1/VOCdevkit \
      --output-path /mnt/data/dataset/exp1/pascal
```

### train

```
container-fn tensorflow-deeplab-train \
      --train-split trainval \
      --dataset pascal_voc_seg \
      --training-steps 1000 \
      --train-crop-size-height 513 \
      --train-crop-size-width 513 \
      --pretrained-path /mnt/ngv/pretrained-networks/deeplabv3/deeplabv3_xception_65_pascal_voc_seg_trainval \
      --dataset-path /mnt/data/dataset/exp1/pascal/tfrecord \
      --output-path /mnt/data/dataset/exp1/pascal/train_on_train_set
```

### evaluate
```
container-fn tensorflow-deeplab-eval \
      --dataset pascal_voc_seg \
      --eval-crop-size-height 513 \
      --eval-crop-size-width 513 \
      --dataset-path /mnt/data/dataset/exp1/pascal/tfrecord \
      --trained-path /mnt/data/dataset/exp1/pascal/train_on_train_set/train \
      --output-path /mnt/data/dataset/exp1/pascal/train_on_train_set
```
### visualize

```
container-fn tensorflow-deeplab-vis \
      --dataset pascal_voc_seg \
      --vis-crop-size-height 513 \
      --vis-crop-size-width 513 \
      --colormap-type pascal \
      --dataset-path /mnt/data/dataset/exp1/pascal/tfrecord \
      --trained-path /mnt/data/dataset/exp1/pascal/train_on_train_set/train \
      --output-path /mnt/data/dataset/exp1/pascal/train_on_train_set

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
      --output-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/ade20k
```

If `dataset-path` is set as `None`, the container-fn will automatically download ADE20K dataset to the `output-path` and convert it to tfrecord format. If `dataset-path` is set as `some/path/to/ADEChallengeData2016`, then container-fn will only convert it to tfrecord format.

### Use container-fn to train

```
container-fn tensorflow-deeplab-train \
      --train-split train \
      --dataset ade20k \
      --training-steps 1000 \
      --train-crop-size-height 513 \
      --train-crop-size-width 513 \
      --resize-factor 16 \
      --min-resize-value 350 \
      --max-resize-value 500 \
      --initialize-last-layer False \
      --last-layers-contain-logits-only True \
      --pretrained-path ${PATH_TO_PRETRAINED_MODEL} \
      --dataset-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/ade20k/tfrecord \
      --output-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/ade20k/train_on_train_set
```

For now, Deeplab does not have a pretrained model for ADE20K. So it is supposed to set ${PATH_TO_PRETRAINED_MODEL} as the directory where a pretraind model (`some/path/to/model.ckpt`) for ADE20K dataset resides.

### Use container-fn to evaluate
```
container-fn tensorflow-deeplab-eval \
      --dataset-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/ade20k/tfrecord \
      --trained-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/ade20k/train_on_train_set/train \
      --output-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/ade20k/train_on_train_set
```

### Use container-fn to visualize
```
container-fn tensorflow-deeplab-vis \
      --dataset-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/ade20k/tfrecord \
      --trained-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/ade20k/train_on_train_set/train \
      --output-path /mnt/ngv/training-runs/2018-05-09-tensorflow-deeplab-test/ade20k/train_on_train_set
```
