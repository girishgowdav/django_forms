from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def django_forms(request):
    SUFO=SignUpForm()
    d={'SUFO':SUFO}
    if request.method=='POST':
        SUFDT=SignUpForm(request.POST)
        if SUFDT.is_valid():
            n=SUFDT.cleaned_data.get('name')
            print(n)
            return HttpResponse(str(SUFDT.cleaned_data))


    return render(request,'django_forms.html',d)