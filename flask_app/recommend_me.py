import base64
import numpy as np
import io
import os
import re
import h5py
import pandas as pd
import tensorflow as tf
from PIL import Image
from skimage import transform
import pymongo
from sklearn.neighbors import NearestNeighbors
from tensorflow.keras import backend as K
from tensorflow.keras.models import Sequential, load_model
import flask
from flask import request, jsonify, Flask

app = Flask('__name__')

#loading the model
model = load_model('image_class_model.h5')

#initiating functions
def nearest_neighbors(values, all_values, nbr_neighbors=11):
    nn = NearestNeighbors(nbr_neighbors, metric='cosine', algorithm='brute').fit(np.array(all_values.tolist()))
    dists, idxs = nn.kneighbors([values])
    return(idxs[0])

def imagepreparation(filename):
    np_image = np.array(filename).astype('float32')
    np_image = transform.resize(np_image, (80, 80, 3))
    np_image = np.expand_dims(np_image, axis=0)
    return np_image

imagetovec = K.function([model.layers[0].input],
                                  [model.layers[9].output])

#connecting to mongo
client = pymongo.MongoClient("mongodb://admin:admin@minime-shard-00-00-jmbfg.mongodb.net:27017,minime-shard-00-01-jmbfg.mongodb.net:27017,minime-shard-00-02-jmbfg.mongodb.net:27017/test?ssl=true&replicaSet=MiniMe-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client['Clothes']
collection = db['ClothesRepository']

@app.route('/predict', methods=["POST"])
def predict():
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    clothe = imagepreparation(image)
    vec = list(np.around(np.array(imagetovec([clothe])[0].tolist()[0]),2))
    cat = int(np.argmax(model.predict(clothe)))
    cursor = collection.find({"Category": cat})
    same_cat =  pd.DataFrame(list(cursor)).iloc[:,[2,3]]
    similar = nearest_neighbors(vec, same_cat.iloc[:,1])
    response = {
        'prediction': {
            'img1': similar[1],
            'img2': similar[2],
            'img3': similar[3],
            'img4': similar[4],
            'img5': similar[5],
            'img6': similar[6],
            'img7': similar[7],
            'img8': similar[8],
            'img9': similar[9],
            'img10': similar[10]
        }
    }
    return jsonify(response)
  
