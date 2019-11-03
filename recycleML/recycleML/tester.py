from fastai.vision import *
from fastai.metrics import error_rate
from pathlib import Path
import os
from PIL import Image
import warnings
warnings.filterwarnings("ignore")

def get_classification(image_name):
    path2 = str(Path(os.getcwd()))+"/static/img/data"
    print(path2)
    tfms = get_transforms(do_flip=True,flip_vert=True)
    data = ImageDataBunch.from_folder(path2, test="test", ds_tfms=tfms, bs=16)
    learn = create_cnn(data,models.resnet34,metrics=error_rate)
    learn.load("trained_model")

    prediction = learn.predict(open_image(image_name))
    a = []
    for i in prediction[2]:
        a.append(i.item())

    mainPred = str(prediction[0])
    mainPerc = str((max(a))*100)[:5]+"%"

    new = list(a)
    new.remove(max(a))

    classifications = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']
    secPred = classifications[a.index(max(new))]
    secPerc = str(max(new)*100)[:5]+"%"
    if(max(new)*100 < .001):
        secPerc = "0%"
    new.remove(max(new))

    thirdPred = classifications[a.index(max(new))]
    thirdPerc = str(max(new)*100)[:5]+"%"
    if(max(new)*100 < .001):
        thirdPerc = "0%"
    new.remove(max(new))

    fourthPred = classifications[a.index(max(new))]
    fourthPerc = str(max(new)*100)[:5]+"%"
    if(max(new)*100 < .001):
        fourthPerc = "0%"
    new.remove(max(new))

    fifthPred = classifications[a.index(max(new))]
    fifthPerc = str(max(new)*100)[:5]+"%"
    if(max(new)*100 < .001):
        fifthPerc = "0%"
    new.remove(max(new))

    lastPred = classifications[a.index(max(new))]
    lastPerc = str(max(new)*100)[:5]+"%"
    if(max(new)*100 < .001):
        lastPerc = "0%"
    new.remove(max(new))
    #open_image(image_name) <---- ORIGINAL IMAGE THAT WAS SENT IN

    return [mainPred.capitalize(), mainPerc, secPred.capitalize(), secPerc, thirdPred.capitalize(), thirdPerc, fourthPred.capitalize(), fourthPerc, fifthPred.capitalize(), fifthPerc, lastPred.capitalize(), lastPerc]

# print(get_classification('/Users/varun/RecycleML/recycleML/recycleML/static/img/data/train/cardboard/cardboard200.jpg'))
