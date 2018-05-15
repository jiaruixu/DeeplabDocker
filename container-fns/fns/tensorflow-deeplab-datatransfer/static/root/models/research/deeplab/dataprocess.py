"""Transfer different datasets into tfrecord.
"""

import six
import os
import tensorflow as tf

flags = tf.app.flags
FLAGS = flags.FLAGS

flags.DEFINE_string('dataset', 'cityscapes',
                    'Name of the segmentation dataset.')
flags.DEFINE_string('data_path', None, 'Where the dataset reside')

flags.DEFINE_string('output_path', None, 'Path to store dataset in tfrecord format.')

def _convert_cityscapes():
    if len(os.listdir(FLAGS.data_path)) == 0:
        tf.logging.info('The dataset Path for Cityscapes dataset cannot be None. Please input a dataset path')
        exit(0)
    # Create training labels.
    os.system('python ./cityscapesScripts/cityscapesscripts/preparation/createTrainIdLabelImgs.py')
    # Create output directory for storing TFRecords.
    output_dir = os.path.join(FLAGS.output_path, 'tfrecord')
    tf.gfile.MakeDirs(output_dir)
    # Build TFRecords of the dataset.
    os.system('python ./datasets/build_cityscapes_data.py --cityscapes_root=%s --output_dir=%s' % (FLAGS.data_path, output_dir))

def _convert_ade20k():
    if len(os.listdir(FLAGS.data_path)) == 0:
        # Download ADE20K dataset and convert into tfrecord format
        os.system('sh ./download_and_convert_ade20k.sh %s' % FLAGS.output_path)
    else:
        train_image_folder = os.path.join(FLAGS.data_path, 'images/training/')
        train_image_label_folder = os.path.join(FLAGS.data_path, 'annotations/training/')
        val_image_folder = os.path.join(FLAGS.data_path, 'images/validation/')
        val_image_label_folder = os.path.join(FLAGS.data_path, 'annotations/validation/')
        # Create output directory for storing TFRecords.
        output_dir = os.path.join(FLAGS.output_path, 'tfrecord')
        tf.gfile.MakeDirs(output_dir)
        # Build TFRecords of the dataset.
        os.system('python ./datasets/build_ade20k_data.py  --train_image_folder=%s --train_image_label_folder=%s \
                  --val_image_folder=%s --val_image_label_folder=%s --output_dir=%s' % (train_image_folder,
                  train_image_label_folder, val_image_folder, val_image_label_folder, output_dir))

def _convert_voc2012():
    if len(os.listdir(FLAGS.data_path)) == 0:
        # Download VOC2012 dataset and convert into tfrecord format
        os.system('sh ./download_and_convert_voc2012.sh %s' % FLAGS.output_path)
    else:
        # Remove the colormap in the ground truth annotations.
        SEG_FOLDER = os.path.join(FLAGS.data_path, 'VOC2012/SegmentationClass')
        SEMANTIC_SEG_FOLDER = os.path.join(FLAGS.output_path, 'VOC2012/SegmentationClassRaw')
        tf.gfile.MakeDirs(SEMANTIC_SEG_FOLDER)

        tf.logging.info('Removing the color map in ground truth annotations...')
        os.system('python ./datasets/remove_gt_colormap.py --original_gt_folder=%s --output_dir=%s' % (SEG_FOLDER, SEMANTIC_SEG_FOLDER))

        # Build TFRecords of the dataset.
        IMAGE_FOLDER = os.path.join(FLAGS.data_path, 'VOC2012/JPEGImages')
        LIST_FOLDER = os.path.join(FLAGS.data_path, 'VOC2012/ImageSets/Segmentation')
        # Create output directory for storing TFRecords.
        output_dir = os.path.join(FLAGS.output_path, 'tfrecord')
        tf.gfile.MakeDirs(output_dir)

        tf.logging.info('Converting PASCAL VOC 2012 dataset...')
        os.system('python ./datasets/build_voc2012_data.py  --image_folder=%s --semantic_segmentation_folder=%s \
                  --list_folder=%s --image_format=%s --output_dir=%s' % (IMAGE_FOLDER,
                  SEMANTIC_SEG_FOLDER, LIST_FOLDER, "jpg", output_dir))

def main(unused_argv):
  tf.logging.set_verbosity(tf.logging.INFO)
  if FLAGS.dataset == 'cityscapes':
      tf.logging.info('Converting Cityscapes dataset...')
      _convert_cityscapes()
      tf.logging.info('Converting Finished.')

  elif FLAGS.dataset == 'ade20k':
      tf.logging.info('Converting ADE20K dataset...')
      _convert_ade20k()
      tf.logging.info('Converting Finished.')

  elif FLAGS.dataset == 'pascal_voc_seg':
      tf.logging.info('Converting PASCAL VOC 2012 dataset...')
      _convert_voc2012()
      tf.logging.info('Converting Finished.')

  else:
      tf.logging.info('This dataset has not been added to deeplab yet.')
      exit(0)

if __name__ == '__main__':
    tf.app.run()
