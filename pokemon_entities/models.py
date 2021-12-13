from django.db import models  # noqa F401

# your models here

class tbl1(models.Model):
    text = models.CharField(max_length=2)

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=None, null=True, blank=True)

    def __str__(self) -> str:
        return self.title