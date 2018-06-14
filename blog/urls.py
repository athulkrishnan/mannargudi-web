from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='blog'),
    url(r'^page/(?P<page>\d+)$', views.home, name='archive'),
    url(r'^(?P<slug>.*)$', views.post, name='blog_post'),
    url(r'^test/', views.post, name='blog_post'),
]
