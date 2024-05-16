from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django import forms as LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def login(request):
    return render(request, 'login.html')
def evaluate(request):
    return render(request,'evaluate.html')
def product(request):
    return render(request, "product.html")

def login (request):
    '''
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
        '''
    return render(request,'login.html',locals())#一定要回應

