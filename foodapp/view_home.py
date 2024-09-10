from django.shortcuts import render
from django.http import HttpResponse

def homePage(request):
    return render(request=request, template_name='foodOnline_template/index.html')