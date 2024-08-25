from django.shortcuts import render,HttpResponse
import pickle
from skimage.io import imread
from skimage.transform import resize
import numpy as np
import matplotlib.pyplot as plt

model=pickle.load(open("model.pkl","rb"))

# Create your views here.
def uploder(request):
    return render(request,"uploder.html")


def predict(request):
    if request.method=="POST":
   
        img=request.FILES['image']
        img_array=imread(img)
        resiz=resize(img_array,(150,150,3))
        flat=resiz.flatten()
        r=model.predict([flat])
        i=plt.imshow(resiz)
        if r[0]==0:
            result="sunflower"
        elif r[0]==1:
            result="cars"
        elif r[0]==2:
            result="bikes"
            
        return render(request,"predict.html",{"result":result,"i":i})
        