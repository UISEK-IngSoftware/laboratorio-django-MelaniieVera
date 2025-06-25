from rest_framework import viewsets
from pokedex.models import Pokemon
from .serializers import PokemonSerializer
from pokedex.models import Entrenador
from .serializers import EntrenadorSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.order_by('name')
    serializer_class = PokemonSerializer
    
class EntrenadorViewSet(viewsets.ModelViewSet):
    queryset = Entrenador.objects.all()
    serializer_class = EntrenadorSerializer
