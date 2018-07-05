from django.conf.urls import url
from django.contrib import admin
 
#importing views
#we need to create views.py
from . import views
 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #define the url getdata that we have written inside form
    url(r'^getdata/', views.decision),
 	url(r'^getdataone/', views.navie),
 	url(r'^getdatatwo/', views.kmean),
 	
    #defining the view for root URL
    url(r'^$', views.decision),
]