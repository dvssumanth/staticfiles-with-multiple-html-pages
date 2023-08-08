"""
URL configuration for project14 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app.views import *
import app1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ind/',ind,name='ind'),
    path('cric/',cric,name='cric'),
    path('food/',food,name='food'),
    path('city/',city,name='city'),
    path('cont/',cont,name='cont'),
    path('about/',about,name='about'),
    path('app1/',include('app1.urls')),
    path('vid/',vid,name='vid'),
    path('js1/',js1,name='js1'),
    path('college/',college,name='college'),
    path('usform/',usform,name='usform'),
    path('suman/',suman,name='suman'),
    path('py/',py,name='py'),
    path('dj/',dj,name='dj'),

]
