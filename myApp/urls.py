from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("result/", views.result, name="result_app"),
    path("heron/", views.heron, name="heron_app"),
    path("discriminant/", views.discriminant, name="discriminant_app")
]