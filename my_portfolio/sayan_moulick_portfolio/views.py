from django.shortcuts import render

from .dashboard import getBlogInfo, getProjectDetail, fetchProjectDetail

# Create your views here.

def show_myprofile(request):
    return render(request, 'index.html', {})
