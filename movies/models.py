from django.db import models
from django.urls import reverse

from datetime import date


class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=1024)
    url = models.SlugField(max_length=128, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Actor(models.Model):
    name = models.CharField(max_length=64)
    age = models.PositiveIntegerField(default=0)
    description = models.TextField(max_length=2048)
    image = models.ImageField(upload_to='actors/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Actors and directors'
        verbose_name_plural = 'Actors and directors'


class Genre(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=1028)
    url = models.SlugField(max_length=128, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Movie(models.Model):
    title = models.CharField(max_length=128)
    tagline = models.CharField(max_length=128, default='')
    description = models.TextField(max_length=4096)
    poster = models.ImageField(upload_to='movies/')
    year = models.PositiveSmallIntegerField(default=2019)
    country = models.CharField(max_length=64)
    directors = models.ManyToManyField(Actor, verbose_name='Director', related_name='film_director')
    actors = models.ManyToManyField(Actor, verbose_name='Actor', related_name='film_actor')
    genre = models.ManyToManyField(Genre, verbose_name='Genre', related_name='film_genre')
    world_premiere = models.DateField(default=date.today)
    budget = models.PositiveIntegerField(default=0, help_text='amount in USD')
    gross_usa = models.PositiveIntegerField(default=0, help_text='amount in USD')
    gross_world = models.PositiveIntegerField(default=0, help_text='amount in USD')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=64, unique=True)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'


class MovieShot(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=1028)
    image = models.ImageField(upload_to="movies/shots/")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Movie shot'
        verbose_name_plural = 'Movie shots'


class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name_plural = 'Rating stars'
        verbose_name = 'Rating star'


class Rating(models.Model):
    ip = models.CharField(name='IP address', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie.title} - {self.star.value}"

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"


class Review(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=32)
    text = models.TextField(max_length=2048)
    parent = models.ForeignKey(
        to='self',
        verbose_name="Parent",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
