from django.db import models


class Category(models.Model):
    """Категории"""
    name = models.CharField(verbose_name="Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
