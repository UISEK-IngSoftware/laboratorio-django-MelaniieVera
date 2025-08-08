from rest_framework import viewsets
from pokedex.models import Pokemon
from .serializers import PokemonSerializer
from pokedex.models import Entrenador
from .serializers import EntrenadorSerializer
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasScope
from rest_framework.permissions import IsAuthenticated, AllowAny

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.order_by('name')
    serializer_class = PokemonSerializer
    
    authentication_classes = [OAuth2Authentication]
    required_scopes = ['write']
    
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated(), TokenHasScope()]
        return [AllowAny()]
    
    
    
class EntrenadorViewSet(viewsets.ModelViewSet):
    queryset = Entrenador.objects.all()
    serializer_class = EntrenadorSerializer
    
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]