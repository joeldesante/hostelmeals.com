from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("recipe/<slug:slug>", views.recipe, name="recipe"),
    path("new", views.add_recipe, name="add_recipe"),
]