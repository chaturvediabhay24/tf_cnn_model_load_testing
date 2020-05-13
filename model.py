import tensorflow as tf
import pickle
import numpy as np
import PIL.Image as Image
tf.keras.backend.clear_session()
import os
from tensorflow.python.framework import ops
ops.reset_default_graph()
from tensorflow.python.keras.backend import set_session


IMAGE_RES=224



with open("imagenet_labels", "rb") as fp:   
  imagenet_labels=pickle.load( fp)

global model
sess=tf.Session()
set_session(sess)

model=tf.keras.applications.MobileNet(
    input_shape=None, alpha=1.0, depth_multiplier=1, dropout=0.001,
    include_top=True, weights='imagenet', input_tensor=None, pooling=None,
    classes=1000
)
global graph
graph =  tf.compat.v1.get_default_graph()

def predictor(img = tf.keras.utils.get_file('image.jpg','https://storage.googleapis.com/download.tensorflow.org/example_images/grace_hopper.jpg')):
	img = Image.open((img)).resize((IMAGE_RES, IMAGE_RES))
	img = np.array(img)/255.0
	img = img[:, :, :3]

	global sess
	global graph

	with graph.as_default():
		set_session(sess)
		result = model.predict(img[np.newaxis, ...])
	result=np.argsort(result)[0,::-1][0]
	X=int(result)+1
	decoded = imagenet_labels[X]
	return str(decoded)

# with open("code.png", 'rb') as f:
#   contents = f.read()
# print(predictor())