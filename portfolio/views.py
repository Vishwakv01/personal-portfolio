from django.shortcuts import render
from portfolio.models import Projects
# Create your views here.


def about(request):
    projects = Projects.objects.all()
    return render(request, 'portfolio/about.html', {'projectkey':projects})