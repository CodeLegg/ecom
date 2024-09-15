from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def wholesale(request):
    return render(request, 'wholesale.html', {})