from img2vec_pytorch import Img2Vec
import os
from PIL import Image
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Prepare Data

img2vec = Img2Vec()

data_dir = "./dataset"
train_dir = os.path.join(data_dir, "train")
val_dir = os.path.join(data_dir, "val")

data={}
for j,dir_ in enumerate([train_dir, val_dir]):
    features=[]
    labels=[]
    for category in os.listdir(dir_):
        for img_path in os.listdir(os.path.join(dir_, category)):
            img_path_ = os.path.join(dir_, category, img_path)
            
            img = Image.open(img_path_)
            img_features = img2vec.get_vec(img)
            features.append(img_features)
            labels.append(category)
    data[['training_data','validation_data'][j]] = features
    data[['training_labels','validation_labels'][j]] = labels
    

# Train Model

model = RandomForestClassifier()
model.fit(data['training_data'], data['training_labels'])


# Test Performance

y_pred = model.predict(data['validation_data'])
score = accuracy_score(y_pred, data['validation_labels'])

print("Performance: ", score)


# Save Model

with open('./model.p', 'wb') as f:
    pickle.dump(model, f)
    f.close()