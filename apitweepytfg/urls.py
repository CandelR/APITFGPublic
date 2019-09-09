from django.urls import path

from . import views

from .views import TweepyApi

app_name = "apitweepytfg"

urlpatterns = [
    # path('apitweepytfg/get', TweepyApi.as_view()),
    path('get', TweepyApi.get, name='get'),
    path('post', TweepyApi.post),
    path('setenv', TweepyApi.setenv, name='setenv'),
    path('tag', TweepyApi.tag, name='tag'),
]