import pickle
from img2vec_pytorch import Img2Vec
from PIL import Image

with open('./model.p', 'rb') as f:
    model = pickle.load(f)

img2vec = Img2Vec()

def run_inference(image_path):
    img = Image.open(image_path)
    features = img2vec.get_vec(img)
    pred = model.predict([features])
    return pred
