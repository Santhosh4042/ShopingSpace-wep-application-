from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from shop.form import CustomerForm
import json

def Home(request):
    products = Product.objects.filter(TRENDING=1)
    return render(request, "shop/index.html", {"trending_product": products})

def Sign_in(request):
    form = CustomerForm() 
    if request.method == 'POST': 
        form = CustomerForm(request.POST)
        if form.is_valid(): 
            form.save()
            messages.success(request,"Your account has been created successfully!!!")
            return redirect('/login')
    return render(request, "shop/sign.html", {'form':form})
def Cart_add(request): 
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
        return render(request, "shop/cart.html", {"cart":cart})
    else: 
        return redirect("/")

def Fav_add(request): 
    if request.user.is_authenticated:
        fav = Favourite.objects.filter(user=request.user)
        return render(request, "shop/fav.html", {"fav":fav})
    else: 
        return redirect("/")

def RemoveFav(request, fid): 
    cartitem = Favourite.objects.get(id = fid) 
    cartitem.delete()
    return redirect("/fav_view")

def RemoveCart(request, cid): 
    cartitem = Cart.objects.get(id = cid) 
    cartitem.delete()
    return redirect("/cart")
def FavPage(request): 
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest': 
        if request.user.is_authenticated:
            data = json.load(request)
            product_id = data['pid']
            product_status = Product.objects.get(id = product_id)
            if product_status:
                if Favourite.objects.filter(user=request.user, PRODUCT_id = product_id): 
                    return JsonResponse({'status': 'Product Already Added to Faourite'}, status =200)
                else:
                    Favourite.objects.create(user=request.user, PRODUCT_id = product_id)
                    return JsonResponse({'status': 'Product Added to Faourite'}, status =200)
        else: 
            return JsonResponse({'status': 'Login to Add Favourite'}, status =200) 
    else: 
        return JsonResponse({'status' : 'Invalid Access'}, status = 200)
    

def AddToCart(request): 
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest': 
        if request.user.is_authenticated:
            data = json.load(request)
            product_qty = data['product_qty']
            product_id = data['pid']
            product_status = Product.objects.get(id = product_id)
            if product_status:
                if Cart.objects.filter(user = request.user.id, PRODUCT_id = product_id): 
                    return JsonResponse({'status' : 'Product Already in Cart'}, status = 200)
                else: 
                    if product_status.QUANTITY>=product_qty: 
                        Cart.objects.create(user=request.user, PRODUCT_id = product_id, PRODUCT_QTY = product_qty)
                        return JsonResponse({'status': 'Product Added to Cart'}, status = 200)
                    else: 
                        return JsonResponse({'status': 'Product Stock Not '}, status =200)
            else: 
                return JsonResponse({'status': 'Login to Add Cart'}, status =200) 
        else: 
            return JsonResponse({'status' : 'Invalid Access'}, status = 200)


def Log_out(request): 
    if request.user.is_authenticated: 
        logout(request)
        messages.success(request, "Logged out successfully")
    return redirect('/')
def Log_in(request):
    if request.user.is_authenticated: 
        return redirect('/')
    else: 
        if request.method == 'POST': 
            name = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(request, username= name, password = pwd)
            if user is not None: 
                login(request, user)
                messages.success(request, "Welcome, Shoping Space!!!")
                return redirect('/')
            else: 
                messages.error(request, "Invalid user name or password")
                return redirect('/login')
        return render(request, "shop/login.html")
    
def Collections(request):
    category = Category.objects.filter(STATUS = 0)
    return render(request, "shop/collections.html",{"collections":category})

def CollectionView(request,name): 
    if(Category.objects.filter(NAME=name,STATUS = 0)): 
        products = Product.objects.filter(category__NAME = name)
        return render(request, "shop/products/index.html",{"products":products , "category" : name})
    else: 
        messages.warning(request, "No Such Category Found")
        return redirect('collections')

def ProductDetails(request,cname,pname): 
    if(Category.objects.filter(NAME=cname, STATUS=0)): 
        if(Product.objects.filter(NAME=pname, STATUS=0)):
            products = Product.objects.filter(NAME = pname, STATUS=0).first()
            return render(request, "shop/products/product_details.html",{"product":products})
        else: 
            messages.error(request, "No Such Category Found")
            return redirect('collections')
    else: 
        messages.error(request, "No Such Category Found")
        return redirect('collections')