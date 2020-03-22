from django.shortcuts import render, Http404
from django.views.generic import ListView, DetailView

from movies.models import Movie


class MoviesView(ListView):
    """
    Movie List
    """
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    """
    Movie Detail Description
    """
    model = Movie
    slug_field = "url"

