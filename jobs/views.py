from django.shortcuts import render

from .models import Job

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

def page_not_found_view(request):
    jobs = Job.objects
    return render(request, 'jobs/page_not_found_view.html', {'jobs':jobs})
