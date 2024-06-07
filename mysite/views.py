from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django import forms as LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from mysite.models import Product
from mysite.forms import UserRegisterForm
from django.shortcuts import render, redirect
from .models import Member,shoppingCart
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

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
def search(request):
    kw = request.POST.get('q')#抓表單的東西(看你header的名字)
    products = Product.objects.filter(name__icontains=kw)#name__icontains 要以name這個欄位做相似查詢相似查詢
    return render(request, 'search.html', {'products': products, 'keyWord': kw})

#註冊
def register(request):
    if request.method == 'POST':
        # 從 POST 請求中獲取表單數據
        name = request.POST.get('name')
        borndate = request.POST.get('borndate')
        gender = request.POST.get('gender')
        gender = 'M' if gender == 'male' else 'W'
        phoneNum = request.POST.get('phoneNum')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        # 檢查密碼是否一致
        if password != confirm_password:
            return render(request, 'register.html', {'error': '密碼與確認密碼不一致'})
        
        # 創建會員對象並保存到資料庫中
        member = Member.objects.create_user(
            username=name,
            borndate=borndate,
            gender=gender,
            phoneNum=phoneNum,
            email=email,
            password=password
        )
        
        # 重定向到註冊成功頁面或其他適當的頁面
        return redirect('/')
    else:
        # 如果不是 POST 請求，返回空的註冊表單
        return render(request, 'register.html')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Comment
from .forms import CommentForm

def evaluate(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.member_id = request.user # 假设你有一个从用户到会员的外键关系
            comment.product_id = product
            comment.save()
            return redirect('product', id=product_id)
    else:
        form = CommentForm()

    return render(request, 'evaluate.html', {'product': product, 'form': form,'product_id': product_id})




def showproduct(request, id):
	try:
		product = Product.objects.get(id = id)
		if product != None:
			return render(request, 'product.html', locals())
	except:
		return redirect('/')
    
def home(request):
    items = Product.objects.all()
    return render(request, 'home.html', {'items': items}) 
def man(request):
    mans_products = Product.objects.filter(category='man')
    return render(request, 'man.html', {'mans_products': mans_products})
def girl(request):
    girls_products = Product.objects.filter(category='woman')
    return render(request, 'girl.html', {'girls_products': girls_products})
def child(request):
    childs_products = Product.objects.filter(category='child')
    return render(request, 'child.html', {'childs_products': childs_products})
def jewelry(request):
    jewelrys_products = Product.objects.filter(category='jewelry')
    return render(request, 'jewelry.html', {'jewelrys_products': jewelrys_products})
def shoe(request):
    shoes_products = Product.objects.filter(category='shoe')
    return render(request, 'shoe.html', {'shoes_products': shoes_products})


def mine(request):
    return render(request, "mine.html") 

#更新使用者資料
@login_required(login_url='/login/') 
def profile(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            username = request.user.username
            try:
                userinfo = Member.objects.get(username=username)
                # 从 Profile 对象中提取字段数据
                form = {
                    'username': userinfo.username,
                    'borndate': userinfo.borndate,
                    'phoneNum': userinfo.phoneNum,
                    'email': userinfo.email
                    # 添加更多字段
                }
            except Member.DoesNotExist:
                form = {
                    'username': '',
                    'borndate': '',
                    'phoneNum': '',
                    'email': ''
                    # 添加更多字段
                }
            return render(request, 'userinfo.html', {'form': form})

    elif request.method == 'POST':
        username = request.user.username
        try:
            userinfo = Member.objects.get(username=username)
            form = {
                'username': request.POST.get('username'),
                'borndate': request.POST.get('borndate'),
                'phoneNum': request.POST.get('phoneNum'),
                'email': request.POST.get('email'),
                # 添加更多字段
            }
            # 更新现有 Profile 对象
            userinfo.username = form['username']
            userinfo.borndate = form['borndate']
            userinfo.phoneNum = form['phoneNum']
            userinfo.email = form['email']
            # 更新更多字段
            userinfo.save()
            message = '成功更新個人資料！'
        except Member.DoesNotExist:
            form = {
                'username': request.POST.get('username'),
                'borndate': request.POST.get('borndate'),
                'phoneNum': request.POST.get('phoneNum'),
                'email': request.POST.get('email'),
                # 添加更多字段
            }
            # 创建新的 Profile 对象
            userinfo = Member(
                user=request.user,
                username=form['username'],
                borndate=form['borndate'],
                phoneNum=form['phoneNum'],
                email=form['email'],
                # 添加更多字段
            )
            userinfo.save()
            message = '成功新增！'

        # 处理密码更新逻辑
        password = request.POST.get('password')
        newPassword1 = request.POST.get('newPassword1')
        newPassword2 = request.POST.get('newPassword2')

        if password and newPassword1 and newPassword2:  # 只有在密码字段都不为空时才处理密码更新
            if not check_password(password, request.user.password):
                return render(request, 'userinfo.html', {'form': form, 'msg': '密碼錯誤'})
            elif newPassword1 != newPassword2:
                return render(request, 'userinfo.html', {'form': form, 'msg': '兩次密碼輸入不同'})
            else:
                request.user.set_password(newPassword1)
                request.user.save()
                messages.success(request, '密碼修改成功，請重新登入')
                return redirect('login')

        return render(request, 'userinfo.html', {'form': form, 'message': message})

    else:
        message = "ERROR"
        print('出錯回首頁')
        return redirect("/")  # 如果请求不是 GET 或 POST，则重定向到首页
#產品
def product(request):
    products = Product.objects.all()
    return render(request, "product.html", {'products': products})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, shoppingCart

# def add_to_cart(request, product_id):
#     member = request.user  # 假設會員是通過登錄的用戶關聯的
#     product = get_object_or_404(Product, id=product_id)
#     cart_item, created = shoppingCart.objects.get_or_create(
#         member_id=member,
#         product_id=product,
#         defaults={'orderQua': 1}
#     )
#     if not created:
#         cart_item.orderQua = str(int(cart_item.orderQua) + 1)
#         cart_item.save()
#     return redirect('shopcar')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # 获取当前用户的 ID
    member_id = request.user.id
    
    # 确保用户已登录
    if member_id:
        # 使用 get_or_create 方法创建 shoppingCart 实例，并传递 member_id 参数
        cart_item, created = shoppingCart.objects.get_or_create(
            product_id=product, 
            member_id_id=member_id, 
            defaults={'orderQua': 1}
        )
        
        if not created:
            cart_item.orderQua = str(int(cart_item.orderQua) - 1)
            cart_item.save()
        
        return redirect('shopcar')
    else:
        # 用户未登录，重定向到登录页面或者其他处理逻辑
        return redirect('login')
    
def shopcar(request):
    member_id = request.user.id
    if member_id:
        cart_items = shoppingCart.objects.filter(member_id_id=member_id)
        return render(request, 'shopcar.html', {'cart_items': cart_items})
    else:
        return redirect('login')

# def shopcar(request):
#     return render(request,"shopcar.html")
def order(request):
    return render(request,"order.html")

def pay(request):
     return render(request,"pay.html")