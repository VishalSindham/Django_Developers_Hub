from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def sample(request):
    # return HttpResponse('Here is the sample project I have set up ')
    return render(request, 'sample.html')