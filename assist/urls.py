"""assist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from assist.views import * #Django treats everything like it's at the highest level
                                        #so you need to specify the absolute location of the class
                                        #assist is the application the folder the file is in

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomePageView.as_view()),# maps empty string(regex) to the get method in the homepageview class
    url(r'^va/', VeteranAPIView.as_view()),
    url(r'^gen/', GenerateCSVView.as_view()),
    url(r'^update/', UpdateFormView.as_view()),
    url(r'^check/', post)
]
