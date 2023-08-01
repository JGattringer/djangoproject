import os
from django.conf import settings
from django.shortcuts import render
from .models import My_movies

import os
from django.conf import settings
from django.shortcuts import render
from .models import My_movies


def MovieListView(request):
    # Caminho para a pasta de covers dos filmes
    covers_dir = os.path.join(settings.STATIC_ROOT, 'images', 'movies_covers')

    # Obter a lista de arquivos de imagem da pasta static/images/movies_covers
    images_list = os.listdir(covers_dir)

    # Obter os dados dos filmes do banco de dados
    movies_list = My_movies.objects.all()

    # Renderizar o template com a lista de filmes e a lista de imagens
    return render(request, 'home.html', {'movies_list': movies_list, 'images_list': images_list})


def homepage(request):
    return MovieListView(request)