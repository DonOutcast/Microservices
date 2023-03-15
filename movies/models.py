from django.db import models

from datetime import date


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


class Actor(models.Model):
    """Актёры и режисёры"""

    name = models.CharField(verbose_name="Имя", max_length=100)
    age = models.PositiveSmallIntegerField(verbose_name="Возраст", default=0)
    description = models.TextField("Описание")
    image = models.ImageField(verbose_name="Изображение", upload_to="actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актёры и режисёры"
        verbose_name_plural = "Актёры и режисёры"


class Genre(models.Model):
    """Жанры"""
    name = models.CharField(verbose_name="Имя", max_length=100)
    description = models.TextField(verbose_name="Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Movie(models.Model):
    """Фильм"""
    title = models.CharField(verbose_name="Название", max_length=100)
    tagline = models.CharField(verbose_name="Слоган", max_length=100, default='')
    description = models.TextField("Описание")
    poster = models.ImageField(verbose_name="Постер", upload_to="movies/")
    year = models.PositiveSmallIntegerField(verbose_name="Дата выхода", default=2019)
    country = models.CharField(verbose_name="Страна", max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name="Режиссёр", related_name="file_director")
    actors = models.ManyToManyField(Actor, verbose_name="Актёры", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="Жанры")
    world_premiere = models.DateField(verbose_name="Примьера в мире", default=date.today)
    budget = models.PositiveIntegerField(verbose_name="Бюджет", default=0, help_text="Указывать сумму в долларах")
    fees_in_usa = models.PositiveIntegerField(verbose_name="Сборы в США", default=0,
                                              help_text="Указывать сумму в долларах")
    fees_in_world = models.PositiveIntegerField(verbose_name="Сборы в Мире", default=0,
                                                help_text="Указывать сумму в долларах")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    urls = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField(verbose_name="Черновик", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class MovieShots(models.Model):
    """Кадры из фильмы"""
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField(verbose_name="Изображение", upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр фильма"
        verbose_name_plural = "Кадры из фильма"


class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.PositiveSmallIntegerField(verbose_name="Знание", default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField(verbose_name="IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    movie = models.ForeignKey(Movie, on_delete=models.CharField, verbose_name="Фильм")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

class Reviews(models.Model):
    """Отзовы"""
    email = models.EmailField()
    name = models.CharField(verbose_name="Имя", max_length=100)
    text = models.TextField(verbose_name="Сообщение", max_length=5000)
    parent = models.ForeignKey("self", verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


