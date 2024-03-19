from django.shortcuts import render
from django.http import HttpResponse
from .models import Score
# Create your views here.
context = {}
def index(request):
    # return HttpResponse("Hello wordls")
    scores = Score.objects.all()
    context['student_data'] = scores
    context['title'] = 'Home'
    return render(request, 'index.html', context)    

def about(request):
    context['title'] = 'About'
    return render(request, 'about.html', context) 

def contactus(request):
    context['title'] = 'Contact Us'
    return render(request, 'contact.html', context) 
