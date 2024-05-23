from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django import forms as LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from mysite.models import Product
#登入
def logins(request):
    if request.user.is_active:  # 確認用戶是否已經登入
        return redirect('home')
    msg = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)  # 驗證用戶名和密碼
        
        if user is not None:
            login(request, user)  # 登入用戶
            return redirect('home')  # 登入成功後重定向到首頁
        else:
            msg = '帳號或密碼錯誤'  # 設定錯誤訊息
            return render(request, 'login.html', {'msg': msg})  # 將錯誤訊息傳遞給模板
    return render(request, 'login.html')
    

#登出
def logout(request):
    auth.logout(request)
    message = f'成功登出'
    return redirect('/')

#搜尋
'''
def search(request):
    kw = request.GET.get('q')#抓表單的東西(看你header的名字)
    product = product.objects.filter(title__icontains=kw)#title__icontains相似查詢
    return render(request, 'search.html', {'product': product, 'keyWord': kw})
'''

def evaluate(request):
    return render(request,'evaluate.html')
def product(request):
    return render(request, "product.html")
def home(request):
    return render(request, "home.html") 
def mine(request):
    return render(request, "mine.html") 
def car(request):
    return render(request, "car.html") 
def man(request):
    return render(request, "man.html") 
def girl(request):
    return render(request, "girl.html") 
def child(request):
    return render(request, "child.html") 
def jewelry(request):
    return render(request,"jewelry.html")
def shoe(request):
    return render(request,"shoe.html")
def shopcar(request):
    return render(request,"shopcar.html")
def register(request):
    return render(request,"register.html")
