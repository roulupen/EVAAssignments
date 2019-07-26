import tensorflow as tf
from tqdm import tqdm_notebook

def int_tffeature(value) -> tf.train.Feature:
    if not isinstance(value, list):
        value = [value]
    return tf.train.Feature(int64_list=tf.train.Int64List(value=value))

def float_tffeature(value) -> tf.train.Feature:
    if not isinstance(value, list):
        value = [value]
    return tf.train.Feature(float_list=tf.train.FloatList(value=value))

def numpy_tfexample(x, y=None) -> tf.train.Example:
    if y is None:
        feat_dict = {'image': float_tffeature(x.tolist())}
    else:
        feat_dict = {'image': float_tffeature(x.tolist()), 'label': int_tffeature(y)}
    return tf.train.Example(features=tf.train.Features(feature=feat_dict))

def numpy_tfrecord(output_fn: str, X, y=None, overwrite: bool = False):
    n = X.shape[0]
    X_reshape = X.reshape(n, -1)

    if overwrite or not tf.io.gfile.exists(output_fn):
        with tf.io.TFRecordWriter(output_fn) as record_writer:
            for i in tqdm_notebook(range(n)):
                example = numpy_tfexample(X_reshape[i]) if y is None else numpy_tfexample(X_reshape[i], y[i])
                record_writer.write(example.SerializeToString())
    else:
        tf.logging.info('Output file already exists. Skipping.')