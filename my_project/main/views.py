from django.shortcuts import render
from .models import My_movies

# Create your views here.
def homepage(request):
    return render(
                    request=request,
                    template_name="home.html",
                    context={"Movies": My_movies.objects.all}
                )
