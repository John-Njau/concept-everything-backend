from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Genres"


class Movie(models.Model):
    name = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    description = models.TextField()
    release_date = models.DateTimeField(auto_now_add=True)
    stars = models.IntegerField()

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    age = models.IntegerField()
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Actors"


class Director(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    age = models.IntegerField()
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Directors"


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Reviews"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    comment = models.TextField()
    visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Comments"
