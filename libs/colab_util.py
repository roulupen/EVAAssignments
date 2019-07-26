from google import colab
import tensorflow as tf
import os
import json
from typing import List, Dict, Tuple, Union

TPU_ADDRESS = f'grpc://{os.environ["COLAB_TPU_ADDR"]}' if "COLAB_TPU_ADDR" in os.environ else None


def setup_gcs(tpu_address: str = None):
    """
    Set up Google Cloud Storage for TPU.
    :param tpu_address: network address of the TPU, starting with 'grpc://'. Default: Colab's TPU address.
    :return: None
    """
    colab.auth.authenticate_user()

    tpu_address = tpu_address or TPU_ADDRESS

    with tf.Session(tpu_address) as sess:
        with open('/content/adc.json', 'r') as f:
            auth_info = json.load(f)
        tf.contrib.cloud.configure_gcs(sess, credentials=auth_info)

def get_gcs_dirs(root_dir: str, project: str) -> Tuple[str, str]:
    """
    Get recommended directories for storing datasets (data_dir) and intermediate files generated during training
    (work_dir).
    :param root_dir: Root directory, which is often the Google Cloud Storage bucket when using TPUs.
    :param project: Name of the project.
    :return: Data directory for storaing datasets, and work directory for storing intermediate files.
    """
    data_dir: str = os.path.join(root_dir, 'data', project)
    work_dir: str = os.path.join(root_dir, 'work', project)
    tf.io.gfile.makedirs(data_dir)
    tf.io.gfile.makedirs(work_dir)
    return data_dir, work_dir

