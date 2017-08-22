import tensorflow as tf
model_path = "./movie_dialog_model"
ckpt = tf.train.get_checkpoint_state(model_path)
input_checkpoint = ckpt.model_checkpoint_path
isExist = tf.gfile.Exists(input_checkpoint)

print("111")

