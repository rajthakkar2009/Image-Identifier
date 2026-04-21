import tensorflow as tf
import numpy as np
from PIL import Image

# Load model once
model = tf.keras.models.load_model("model/best_model.keras")

def preprocess_image(image: Image.Image):
    image = image.resize((224, 224))
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def predict(image):
    processed = preprocess_image(image)
    pred = model.predict(processed)[0][0]

    if pred > 0.5:
        return "dog", float(pred)
    else:
        return "cat", float(1 - pred)