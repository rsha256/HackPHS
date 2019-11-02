from fastai.vision import *
from fastai.metrics import error_rate
from pathlib import Path
from glob2 import glob
from sklearn.metrics import confusion_matrix
import os
from PIL import Image


path = Path(os.getcwd())/"data"
tfms = get_transforms(do_flip=True,flip_vert=True)
data = ImageDataBunch.from_folder(path,test="test",ds_tfms=tfms,bs=16)
learn = create_cnn(data,models.resnet34,metrics=error_rate)
learn.load("trained_model")

print(learn.predict(open_image('plastic100.jpg')))