from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from .models import Pokemon
from .forms import PokemonForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import Entrenador
from .forms import EntrenadorForm


def index(request):
    pokemons = Pokemon.objects.order_by('name')
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons}, request))

def pokemon(request,id: int):
    pokemon = Pokemon.objects.get(pk=id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
        
    else:
        form = PokemonForm()
            
    return render (request, 'pokemon_form.html', {'form': form})

def edit_pokemon(request, id: int):
    pokemon = Pokemon.objects.get(pk=id)

    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm(instance=pokemon)

    return render(request, 'pokemon_form.html', {'form': form})

def delete_pokemon(request, id: int):
    pokemon = Pokemon.objects.get(pk=id)
    pokemon.delete()
    return redirect('pokedex:index')


class CustomLoginView(LoginView):
    template_name = "login_form.html"

def lista_entrenadores(request):
    entrenadores = Entrenador.objects.all()
    template = loader.get_template('lista_entrenadores.html')
    return HttpResponse(template.render({'entrenadores': entrenadores}, request))

def add_entrenador(request):
    if request.method == 'POST':
        form = EntrenadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:lista_entrenadores')
    else:
        form = EntrenadorForm()
    
    template = loader.get_template('form_entrenador.html')
    return HttpResponse(template.render({'form': form}, request))


def edit_entrenador(request, id: int):
    entrenador = Entrenador.objects.get(pk=id)

    if request.method == 'POST':
        form = EntrenadorForm(request.POST, request.FILES, instance=entrenador)
        if form.is_valid():
            form.save()
            return redirect('pokedex:lista_entrenadores')
    else:
        form = EntrenadorForm(instance=entrenador)
    
    template = loader.get_template('form_entrenador.html')
    return HttpResponse(template.render({'form': form}, request))


def delete_entrenador(request, id: int):
    entrenador = Entrenador.objects.get(pk=id)
    entrenador.delete()
    return redirect('pokedex:lista_entrenadores')