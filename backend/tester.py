from fastai.vision import *
from fastai.metrics import error_rate
from pathlib import Path
import os
from PIL import Image
import warnings
warnings.filterwarnings("ignore")

def get_classification(image_name):
    path = Path(os.getcwd())/"data"
    tfms = get_transforms(do_flip=True,flip_vert=True)
    data = ImageDataBunch.from_folder(path,test="test",ds_tfms=tfms,bs=16)
    learn = create_cnn(data,models.resnet34,metrics=error_rate)
    learn.load("trained_model")

    prediction = learn.predict(open_image(image_name))
    a = []
    for i in prediction[2]:
        a.append(i.item())

    print(str(prediction[0]))
    print(str((max(a))*100)[:5]+"%")

    new = list(a)
    new.remove(max(a))

    classifications = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']
    print(classifications[a.index(max(new))])
    print(str(max(new)*100)[:5]+"%")
    print(open_image(image_name))

get_classification('plastic100.jpg')