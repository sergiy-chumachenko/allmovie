from django.contrib import admin

from movies.models import Category, Actor, Genre, Movie, MovieShot, RatingStar, Rating, Review

admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShot)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Review)
