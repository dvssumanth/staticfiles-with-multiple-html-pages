from django.shortcuts import render

# Create your views here.
def dvs(request):
    return render(request,'dvs.html')
def form(request):
    return render(request,'form.html')
def a(request):
    return render(request,'a.html')