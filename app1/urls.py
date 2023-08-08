from django.urls import path
from app1.views import *
urlpatterns=[
    path('dvs/',dvs,name='dvs'),
    path('form/',form,name='form'),
    path('a',a,name='a')
]