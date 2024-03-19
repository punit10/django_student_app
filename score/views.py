from django.shortcuts import render
from django.http import HttpResponse
from .models import Score
from .forms import ScoreForm
# Create your views here.

# def index(request):
#     return HttpResponse("Hello wordls")
context = {}
def index(request):
    scores = Score.objects.all()
    form = ScoreForm()
    context['student_data'] = scores
    context['title'] = 'Home'

    #handling form data
    if request.method == 'POST':
        if 'save' in request.POST:
            std_id = request.POST.get('save')

            if not std_id: #empty means add new row
                form = form = ScoreForm(request.POST)
            else:
                student = Score.objects.get(id=std_id)
                form = ScoreForm(request.POST, instance=student)    
            form.save()
            form = ScoreForm()
        elif 'delete' in request.POST:
            std_id = request.POST.get('delete')
            student = Score.objects.get(id=std_id) 
            student.delete()
        elif 'edit' in request.POST:
            std_id = request.POST.get('edit')
            student = Score.objects.get(id=std_id) 
            form = ScoreForm(instance=student)
                   
    context['form'] = form
    return render(request, 'index.html', context)    

def about(request):
    context['title'] = 'About'
    return render(request, 'about.html', context) 

def contactus(request):
    context['title'] = 'Contact Us'
    return render(request, 'contact.html', context) 
