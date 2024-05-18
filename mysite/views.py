from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django import forms as LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

#登入
def logins(request):
    if request.user.is_active:  # 確認用戶是否已經登入
        return redirect('product')
    msg = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)  # 驗證用戶名和密碼
        
        if user is not None:
            login(request, user)  # 登入用戶
            return redirect('/')  # 登入成功後重定向到首頁
        else:
            msg = '帳號或密碼錯誤'  # 設定錯誤訊息
            return render(request, 'login.html', {'msg': msg})  # 將錯誤訊息傳遞給模板
    return render(request, 'login.html')
    

#登出
def logout(request):
    auth.logout(request)
    message = f'成功登出'
    return redirect('/')

def evaluate(request):
    return render(request,'evaluate.html')
def product(request):
    return render(request, "product.html")
def home(request):
    return render(request, "home.html") 

'''
def login (request):
    
    if request.method == 'GET':
        form = LoginForm()#代表會顯示的欄位 在forms那邊
        return render(request,'login.html',locals())#一定要回應
    elif request.method =='POST':
        #login=request.
        form = LoginForm(request.POST)#去request抓資料 把變數抓下來
        if form.is_valid():#一定要寫這個(if以下的) 這個是要抓裡面的值
            user_name = form.cleaned_data['user_name']
            user_password = form.cleaned_data['user_password']
            user = authenticate(username=user_name, password=user_password)#判斷登入的跟資料庫是否一樣
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    print("success")
                    message='成功'
                    return redirect('/')
                else:
                    message='未啟用'
            else:
                message='失敗'
        return render(request,'login.html',locals())#一定要回應
    else:
        massge='ERROR'

    return render(request,'login.html',locals())#一定要回應
'''
'''
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('login')  # 替换为你登录后重定向的URL名称
            else:
                error = "Invalid username or password."
        else:
            error = "Invalid username or password."
        return render(request, 'login.html', {'form': form, 'error': error})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
'''
'''
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product')  # 替換為產品頁面的URL名稱
        else:
            messages.error(request, "無效的帳號或密碼")
    return render(request, 'login.html')
'''