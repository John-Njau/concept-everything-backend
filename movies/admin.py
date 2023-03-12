from django.contrib import admin
from movies.models import Actor, Director, Genre, Movie, Review


# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Review)
