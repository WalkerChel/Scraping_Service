from django.shortcuts import render
from .models import Vacancy
from .forms import FindForm
import datetime

def home_view(request):
    # print(request.GET)
    form = FindForm()
    city = request.GET.get('city')
    language = request.GET.get('language')
    qs = []
    if city or language:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if language:
            _filter['language__slug'] = language

        qs = Vacancy.objects.filter(**_filter)
    date = datetime.datetime.now().date()
    time = datetime.datetime.now().time()
    name = 'Ilya'
    _context = {'date': date, 'name': name, 'time': time, 'object_list': qs, 'form': form}
    return render(request, 'scraping/home.html', _context)

