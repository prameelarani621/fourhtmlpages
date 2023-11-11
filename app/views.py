from django.shortcuts import render

# Create your views here.
def hansi(request):
    return render(request,'hansi.html')

def ammu(request):
     return render(request,'ammu.html')

def bablu(request):
     return render(request,'bablu.html')

def rani(request):
     return render(request,'rani.html')