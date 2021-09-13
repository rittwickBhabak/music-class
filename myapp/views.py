from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from .models import Song 

def index(request):
    context = {
        'songs': Song.objects.all()
    }
    return render(request, 'myapp/index.html', context=context)

def song(request, id):
    context = {
        'song': get_object_or_404(Song, id=id)
    }
    return render(request, 'myapp/song.html', context=context) 
