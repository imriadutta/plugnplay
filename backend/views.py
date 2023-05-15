from django.shortcuts import render
from backend.models import *


def home(request):
    videos = Video.objects.all().order_by('-upload_time')
    return render(request, 'index.html', {'videos': videos})
