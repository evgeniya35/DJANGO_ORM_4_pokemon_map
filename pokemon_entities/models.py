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
    pokemon = models.ForeignKey(Pokemon, on_delete=models.SET_NULL, null=True, verbose_name='Покемон')
    apperated_at = models.DateTimeField(null=True, default=None, verbose_name='Появляется')
    disapperated_at = models.DateTimeField(null=True, default=None, verbose_name='Исчезает')
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)
    level = models.IntegerField(null=True, verbose_name='Уровень', help_text='Поле уровень')
    health = models.IntegerField(null=True, verbose_name='Здоровье')
    strength = models.IntegerField(null=True, verbose_name='Атака')
    defence = models.IntegerField(null=True, verbose_name='Защита')
    stamina = models.IntegerField(null=True, verbose_name='Выносливость')

    def __str__(self) -> str:
        return f'{self.pokemon} опции'

