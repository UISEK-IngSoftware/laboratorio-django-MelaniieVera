from django.contrib import admin
from .models import Pokemon
from .models import Entrenador

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    pass

@admin.register(Entrenador)
class EntrenadorAdmin(admin.ModelAdmin):
    pass
