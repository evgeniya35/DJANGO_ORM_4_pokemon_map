from django.db import models  # noqa F401

# your models here

class tbl1(models.Model):
    text = models.CharField(max_length=2)

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.SET_NULL, null=True)
    apperated_at = models.DateTimeField(null=True, default=None)
    disapperated_at = models.DateTimeField(null=True, default=None)
    lat = models.FloatField()
    lon = models.FloatField()