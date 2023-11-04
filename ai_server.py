import tensorflow as tf
import os
import json
import numpy as np
from flask import Flask, request, jsonify, Response
import tempfile

from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

from tensorflow.keras.preprocessing import image

app = Flask(__name__)

model = tf.keras.models.load_model('./고선우.h5')

classes = ["코르크 마개", "키보드"]
    

def predict_image(filename, model):
    img_ = image.load_img(filename, target_size=(224, 224))
    img_array = image.img_to_array(img_)
    img_processed = np.expand_dims(img_array, axis=0)
    img_processed /= 255.
    
    prediction = model.predict(img_processed)

    index = np.argmax(prediction)
    return classes[index]

@app.route('/')
def index():
    return 'Hello world'

@app.route('/predict/image', methods=['POST'])
def predict():
    try:
        print(request.files)
        image_file = request.files.get('photo')
        print(image_file)
        if image_file and isinstance(image_file, FileStorage) and image_file.filename.endswith(('.jpg', '.jpeg', '.png')):
            tempDir = tempfile.gettempdir()
            image_path = os.path.join(
                tempDir, secure_filename("temp_image.jpg"))
            prediction = predict_image(image_path, model)
            response = json.dumps({"result": prediction}, ensure_ascii=False)
            return Response(response, content_type="application/json; charset=utf-8")
    except:
        return "Error"
    

if __name__ == '__main__':
    app.run(port="5000", debug=True)