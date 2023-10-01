from django.contrib.auth import authenticate, login as auth_login, logout
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from .models import product,contact,checkout
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    products=product.objects.all()

    return render(request, "index.html",{"Product":products})

def about(request):
    return render(request, "about.html")


def shop(request):
    products=product.objects.all()
    a=product.objects.values('sub_category')
    p=Paginator(products,9,orphans=1)
    page_number=request.GET.get('page')
    final_data=p.get_page(page_number)
    data={

    "Product": final_data,
    "cat":a,
    }
    return render(request, "shop.html",data)


def blog_details(request):
    return render(request, "blog-details.html")


def checkouts(request,id):
    if request.method == "POST":
        p_id=id
        first_name = request.POST.get('f_name')
        last_name = request.POST.get('l_name')
        country = request.POST.get('country')
        size = request.POST.get('size')
        Address = request.POST.get('address')
        City = request.POST.get('city')
        state = request.POST.get('state')
        postcode = request.POST.get('postcode')
        phone = request.POST.get('number')
        email = request.POST.get('email')
        notes = request.POST.get('notes')
        answer=request.POST.get('answer')
        Checkout=checkout(answer=answer,first_name=first_name,last_name=last_name,country=country,size=size,Address=Address,City=City,state=state,postcode=postcode,phone=phone,email=email,notes=notes,p_id=p_id)
        Checkout.save()

    Product = product.objects.filter(product_id=id)
    return render(request, "checkout.html",{"product":Product[0]})


def contacts(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact=contact(name=name,email=email,message=message)
        Contact.save()
    return render(request, "contact.html")


def shopping_cart(request):
    return render(request, "shopping-cart.html")


def blog(request):
    return render(request, "blog.html")


def shop_details(request):
    return render(request, "shop-details.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        if User.objects.filter(email=email):
            messages.error(request,"Already registered with this email")
            return render(request,"index.html")
        if password != password_confirm:
            messages.error(request,"password didn't matched")
            return render(request,"index.html")
        myUser = User.objects.create_user(username, email, password)
        myUser.save()
        messages.success(request, "Your account has been succesfully created")

        subject="Welcome to Mancot"
        message="Hello "+myUser.username+", \nWelcome To MANCOT \n Thank You for Visiting our website\n We have sent you an email address for conformation"
        from_email=settings.EMAIL_HOST_USER
        to_list=[myUser.email,]
        send_mail(subject,message,from_email,to_list)
        return redirect("signup")
    return render(request, "main.html")


def signup(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return render(request, "index.html",{'username':username})
        else:
            messages.error(request,"Bad Credentials")
            return render(request,"index.html")

    return render(request, "login.html")


def signout(request):
    logout(request)
    messages.success(request,"Logout Successfully")
    return render(request, "index.html")
def products(request,id):

    produc=product.objects.filter(product_id=id)

    return render(request,"products.html",{"product": produc[0]})
def carts(request,id):

    productS=product.objects.filter(product_id=id)
    return render(request,"shopping-cart.html",{"product": productS[0]})


