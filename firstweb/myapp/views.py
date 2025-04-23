from django.shortcuts import render
from django.http import HttpResponse # add line

# start create fn for myapp\urls.py

def Home(request):
    #return HttpResponse('<h1>Hello World from DataSloth</h1>')
    return render(request, 'myapp/home.html')