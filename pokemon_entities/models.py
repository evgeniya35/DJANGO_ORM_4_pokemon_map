from django.db import models
from datetime import datetime


class Pokemon(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название (рус.)'
        )
    title_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Название (англ.)'
        )
    title_jp = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Название (яп.)'
        )
    image = models.ImageField(
        null=True,
        blank=True,
        verbose_name='Изображение'
        )
    description = models.TextField(blank=True, verbose_name='Описание')
    previous_evolution = models.ForeignKey(
        'Pokemon',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='next_evolution',
        verbose_name='Родитель'
        )

    def __str__(self) -> str:
        return f'{self.title}, {self.pk}'

    class Meta:
        verbose_name = 'Покемон'
        verbose_name_plural = 'Покемоны'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        related_name='pokemon_entities',
        verbose_name='Покемон'
        )
    apperated_at = models.DateTimeField(
        default=datetime.now,
        verbose_name='Появляется'
        )
    disapperated_at = models.DateTimeField(
        default=datetime.now,
        verbose_name='Исчезает'
        )
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    level = models.IntegerField(
        default=0,
        blank=True,
        verbose_name='Уровень',
        help_text='Поле уровень'
        )
    health = models.IntegerField(
        default=0,
        blank=True,
        verbose_name='Здоровье'
        )
    strength = models.IntegerField(
        default=0,
        blank=True,
        verbose_name='Атака'
        )
    defence = models.IntegerField(
        default=0,
        blank=True,
        verbose_name='Защита'
        )
    stamina = models.IntegerField(
        default=0,
        blank=True,
        verbose_name='Выносливость'
        )

    def __str__(self) -> str:
        return f'{self.pokemon}'

    class Meta:
        verbose_name = 'Способность'
        verbose_name_plural = 'Способности'
