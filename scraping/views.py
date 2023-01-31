from django.shortcuts import render
from .models import Vacancy

def home_view(request):
    qs = Vacancy.objects.all()
    return render(request, 'HelloWorld.html', {'object_list': qs})

