from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')
def evaluate(request):
    return render(request,'evaluate.html')
def product(request):
    return render(request, "product.html")