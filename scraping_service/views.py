from django.shortcuts import render

import datetime

def tihon(request):
    return render(request, "tihon.html")

def home(request):
    date = datetime.datetime.now().date()
    time = datetime.datetime.now().time()
    name = 'Ilya'
    _context = {'date': date, 'name': name, 'time': time}
    return render(request, "home", _context)
