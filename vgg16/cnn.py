from tensorflow.python.keras.models import load_model
from project.settings import BASE_DIR
import numpy as np
import cv2
import os


model_path = os.path.join(BASE_DIR, 'works/cnn_model.h5')
model = load_model(model_path)


def classification(Img):
    img_data = cv2.resize(Img, (224, 224))
    img_data = img_data[np.newaxis]
    img_data = np.asarray(img_data)
    img_data = img_data / 255.0
    prd = model.predict(img_data)

    return prd[0][0]
