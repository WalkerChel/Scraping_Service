from django.shortcuts import render
from .models import Vacancy
import datetime

def home_view(request):
    qs = Vacancy.objects.all()
    date = datetime.datetime.now().date()
    time = datetime.datetime.now().time()
    name = 'Ilya'
    _context = {'date': date, 'name': name, 'time': time, 'object_list': qs}
    return render(request, 'home.html', _context)

