## Build the docker image

```
$ docker build -t deeplab ./docker
```
## Symlink the following directories
```
$ ln -s /mnt/data/dataset/exp/train
$ ln -s /mnt/data/dataset/exp/eval
$ ln -s /mnt/data/dataset/exp/vis
```

Dataset directory structure:

```
+ dataset
  + cityscapes
    + leftImg8bit
    + gtFine
    + tfrecord
  + exp
    + train
    + eval
    + vis
```
## Start container
```
$ . run.sh
```
## Download the initial model

```
# From /models/research/deeplab/
$ mkdir -p init_models
$ cd init_models
$ wget http://download.tensorflow.org/models/deeplabv3_cityscapes_train_2018_02_06.tar.gz
$ tar zxf deeplabv3_cityscapes_train_2018_02_06.tar.gz
$ cd ..
```

## To train
```
# From /models/research/deeplab/
$ python train.py \
    --logtostderr \
    --training_number_of_steps=30000 \
    --train_split="train" \
    --model_variant="xception_65" \
    --atrous_rates=6 \
    --atrous_rates=12 \
    --atrous_rates=18 \
    --output_stride=16 \
    --decoder_output_stride=4 \
    --train_crop_size=769 \
    --train_crop_size=769 \
    --train_batch_size=2 \
    --num_clones=2 \
    --dataset="cityscapes" \
    --fine_tune_batch_norm=false \
    --tf_initial_checkpoint="init_models/deeplabv3_cityscapes_train/model.ckpt" \
    --train_logdir="/mnt/data/dataset/exp/train" \
    --dataset_dir="/mnt/data/dataset/cityscapes/tfrecord/"
```

## To evaluate
```
# From /models/research/deeplab/
$ python eval.py \
    --logtostderr \
    --eval_split="val" \
    --model_variant="xception_65" \
    --atrous_rates=6 \
    --atrous_rates=12 \
    --atrous_rates=18 \
    --output_stride=16 \
    --decoder_output_stride=4 \
    --eval_crop_size=1025 \
    --eval_crop_size=2049 \
    --dataset="cityscapes" \
    --checkpoint_dir="/mnt/data/dataset/exp/train/" \
    --eval_logdir="/mnt/data/dataset/exp/eval/" \
    --dataset_dir="/mnt/data/dataset/cityscapes/tfrecord/"
```

## To visualize
```
# From /models/research/deeplab/
$ python vis.py \
    --logtostderr \
    --vis_split="val" \
    --model_variant="xception_65" \
    --atrous_rates=6 \
    --atrous_rates=12 \
    --atrous_rates=18 \
    --output_stride=16 \
    --decoder_output_stride=4 \
    --vis_crop_size=1025 \
    --vis_crop_size=2049 \
    --dataset="cityscapes" \
    --colormap_type="cityscapes" \
    --checkpoint_dir="/mnt/data/dataset/exp/train/" \
    --vis_logdir="/mnt/data/dataset/exp/vis/" \
    --dataset_dir="/mnt/data/dataset/cityscapes/tfrecord/"
```
