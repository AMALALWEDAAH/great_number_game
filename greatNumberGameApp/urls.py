from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('response', views.play),
    path('reset', views.reset),
]
