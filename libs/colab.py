from .imports import *

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

