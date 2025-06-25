from django.db import models

class Entrenador(models.Model):
    name = models.CharField(max_length=15, null=False)
    lastname = models.CharField(max_length=15, null=False)
    level = models.IntegerField(null=False)
    picture = models.ImageField(upload_to="entrenador_images", null=True)
    
    def __str__(self):
        return f"{self.name} {self.lastname}"


class Pokemon(models.Model):
    name = models.CharField(max_length=40, null=False)
    type = models.CharField(max_length=30, null=False)
    weight = models.IntegerField(null=False)
    height = models.IntegerField(null=False)
    picture = models.ImageField(upload_to="pokemon_images", null=True)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.SET_NULL, null=True, blank=True)

    
    def __str__(self):
        return self.name 
    
