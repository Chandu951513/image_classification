
from django.urls import path,include
from . import views
urlpatterns = [

    path("",views.uploder,name="up"),
    path("pred",views.predict,name="pred")
]