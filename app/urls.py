from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^anchor/', views.anchor, name='anchor'),
    url(r'^question/new', views.new_question, name='question_new'),
    url(r'^question/(?P<question_id>[0-9]+)/$', views.question, name='question'),
]