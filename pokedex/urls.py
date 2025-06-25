from django.urls import path

from . import views

app_name = "pokedex"

urlpatterns = [
    path("", views.index, name="index"),
    path("pokemon/<int:id>/", views.pokemon, name="detail"),
    path("pokemon/add/", views.add_pokemon, name="add_pokemon"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("edit_pokemon/<int:id>/",views.edit_pokemon,name="edit_pokemon"),
    path("delete_pokemon/<int:id>/",views.delete_pokemon,name="delete_pokemon"),
    
    path("entrenadores/", views.lista_entrenadores, name="lista_entrenadores"),
    path("entrenadores/add/", views.add_entrenador, name="add_entrenador"),
    path("entrenadores/<int:id>/", views.edit_entrenador, name="edit_entrenador"),
    path("entrenadores/<int:id>/delete/", views.delete_entrenador, name="delete_entrenador"),
]