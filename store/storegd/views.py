from .models import *
import datetime
import json
from .forms import registerForm,loginForm
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import *
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login

# Create your views here.


def store(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, comlete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0,'shipping':False}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    product_id = products[:9]
    context = {'products': product_id, 'cartItem': cartItems}
    return render(request, 'storegp/store.html', context)


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, comlete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0,'shipping':False}
        cartItems = order['get_cart_items']

    context = {'items':items,'order':order,'cartItem':cartItems}
    return render(request, 'storegp/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, comlete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0,'shipping':False}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order,'cartItem':cartItems}
    return render(request, 'storegp/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action', action)
    print('productId', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, comlete=False)
    orderItem,created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

#from django.views.decorators.csrf import csrf_exempt
#@csrf_exempt


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, comlete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )
    else:
        print('User is not logged in..')
    return JsonResponse('Payment complete!', safe=False)


def about(request):
    return render(request, 'storegp/about.html')


class login(View):
    def get(self,request):
        context = registerForm
        return render(request,'storegp/login.html',{'context': context})

    def post(self,request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username,email,password)
        user.save()
        return render(request,'storegp/dataok.html')


class loginuser(View):
    def get(self,request):
        context = loginForm
        return render(request,'storegp/log.html',{'context':context})

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            #login(request, user)
            authenticate(user)
            return render(request,'storegp/dataok.html')
        else:
            return render(request,'storegp/datanotok.html')


def allproduct(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, comlete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    context = {'products': products, 'order': order,'cartItem': cartItems}
    return render(request, 'storegp/allpro.html', context)


def viewpro(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, comlete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    product_id = products[0:1]
    context = {'products': product_id, 'order': order, 'cartItem': cartItems}
    return render(request, 'storegp/viewpro.html', context)