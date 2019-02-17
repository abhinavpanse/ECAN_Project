import json

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt 
from django.contrib.auth import views as auth_views

from .forms import CustomUserCreationForm
from .myfunctions import *
from .models import CustomUser


def register(request):

    if request.method == 'POST':
        
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            useremail = form.cleaned_data.get('email')
            discount_code = form.cleaned_data.get('discount_code')
            status_of_discode = gendisc(discount_code)
            
            if status_of_discode==False:
                shop_url = "https://%s:%s@%s.myshopify.com/admin" % (API_KEY, PASSWORD, SHOP_NAME)
                shopify.ShopifyResource.set_site(shop_url)
                shop = shopify.Shop.current()
                print("shopify shop connected after disconnect",SHOP_NAME)
                status_of_discode = gendisc(discount_code)

            if status_of_discode:        
                form.save()
                send_success_message(useremail)
                messages.success(request, f'Account created for {username}!')
                return redirect('login')
        
            else:
                print('your discount code is not made')
                send_fail_message(useremail)
                return HttpResponse("not made")
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})


def profile(request):
    current_user = request.user
    
    print (current_user.sales)
    res = "<h1>"+str(current_user.sales)+str(current_user.username)+"</h1>"
    context = {'current_user':current_user}
    return render(request, 'profile.html')


@csrf_exempt
def webhooklistner(request):

    if request.method == "POST":
        jsonrecieved = json.loads(request.body)
        print('-----------------------------------------------------------------------')
          
        print(jsonrecieved['discount_codes'][0]['code'])
        discount_code0code = jsonrecieved['discount_codes'][0]['code']
        print(discount_code0code)
        usr = CustomUser.objects.filter(discount_code__iexact=discount_code0code).first()
        usr.sales += 1
        usr.save()

    else:
        print("olleh")

    return HttpResponse('pong')


def home(request):
    form = CustomUserCreationForm()
    return render(request,'home.html',{'form':form})

