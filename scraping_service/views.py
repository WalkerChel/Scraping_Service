from django.shortcuts import render

import datetime

def home(request):
    return render(request, "home.html")

def norm(request):
    date = datetime.datetime.now().date()
    time= datetime.datetime.now().time()
    name = 'Ilya'
    _context = {'date': date, 'name': name,'time': time}
    return render(request, "HelloWorld.html", _context)
