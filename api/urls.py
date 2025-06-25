from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'pokemons', views.PokemonViewSet)
router.register(r'entrenadores', views.EntrenadorViewSet)


urlpatterns = [
    path('', include(router.urls))   
    
    
]