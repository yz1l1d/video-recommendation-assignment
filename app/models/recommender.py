import tensorflow as tf
from tensorflow.keras import layers, Model

class VideoRecommender(Model):
    def __init__(self, num_users, num_videos, embedding_size=50):
        super(VideoRecommender, self).__init__()
        self.user_embedding = layers.Embedding(num_users, embedding_size)
        self.video_embedding = layers.Embedding(num_videos, embedding_size)
        self.dense1 = layers.Dense(128, activation="relu")
        self.dropout = layers.Dropout(0.2)
        self.output_layer = layers.Dense(1, activation="sigmoid")

    def call(self, inputs):
        user_vector = self.user_embedding(inputs["user_id"])
        video_vector = self.video_embedding(inputs["video_id"])
        x = tf.concat([user_vector, video_vector], axis=-1)
        x = self.dense1(x)
        x = self.dropout(x)
        return self.output_layer(x)

# Example instantiation (to be trained later)
model = VideoRecommender(num_users=1000, num_videos=5000)