from unicodedata import category
from django.http.response import HttpResponseNotFound, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Product, Order, MyUser, Order, Category, Brand
from django.contrib.auth import authenticate, login, logout
from .forms import MyUserRegistrationForm, ProfileForm, ContactForm
from django.contrib import messages
from django.db.models import Q
from django.views.generic import FormView
from django.urls import reverse_lazy, reverse
import stripe
from django.views.generic import TemplateView
import json
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    #when submit button is pressed 
    if request.method=='POST':  
        email = request.POST.get('email')
        email.lower()
        password = request.POST.get('password')
        try:
            user=MyUser.objects.get(email=email)  
        except:
            messages.error(request, 'email does not exist')
        user=authenticate(request, email=email, password=password)
        if user is not None:
          login(request, user)
          return redirect ('view-cart')
        else:
            messages.error(request, 'An error occurred during login')
    return render(request, 'shop/login.html')

@login_required(login_url='login')
def dashboard(request):

     return render(request, 'shop/dashboard.html')


@login_required(login_url='login')
def profile(request, pk):
    page="Profile"
    user = request.user
    form = ProfileForm(instance=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'successfully updated')
            return redirect('profile', pk=pk)
           
        else:
            messages.error(request, 'erro in updating')
    context={'form':form, 'page':page}
    return render(request, 'shop/profile.html', context)

def register(request):
    if (request.user.is_authenticated):
        return redirect('dashboard')
    form=MyUserRegistrationForm()
    if request.method == 'POST':
        form=MyUserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.userame=user.username.lower()
            user.save()
            login(request, user)
            return redirect('view-cart')
        
    return render(request, 'shop/register.html', {'form':form})



def index(request):
    q=request.GET.get('q') if request.GET.get('q') !=None else ''
    products=Product.objects.all()
    products=products.filter(
        
        Q(title__icontains=q)|
        Q(category__name__icontains=q)|
        Q(description__icontains=q)

        ) 
    furProducts=products.filter(category='2')
    context={'products':products, 'furProducts':furProducts}
    return render(request, 'shop/base.html', {'products':products})


def viewCart(request):
    return render(request, 'shop/view_cart.html')

def viewWishList(request):
    return render(request, 'shop/view_wishlist.html')


def productDetails(request, pk):
    product=Product.objects.get(id=pk)
   
    return render(request, 'shop/product_details.html', {'product':product})


@csrf_exempt
def create_checkout_session(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY 
    if request.method == 'GET': 
         checkout_session = stripe.checkout.Session.create(
        # Customer Email is optional,
        # It is not safe to accept email directly from the client side
        #customer_email = request_data['email'],
        
        customer_email=request.GET.get('email'),
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                    'name': 'octo',
                    },
                    'unit_amount': int(500*100),
                },
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url=request.build_absolute_uri(
            reverse('success')
        )+ "?session_id={CHECKOUT_SESSION_ID}" ,
        #+ "?session_id={CHECKOUT_SESSION_ID}"
        cancel_url=request.build_absolute_uri(reverse('failed')),

        
            ) 
    
    return JsonResponse({'sessionId': checkout_session.id}) 

@login_required(login_url='login')
def checkout(request):
    stripe_publishable_key=settings.STRIPE_PUBLISHABLE_KEY
    if request.method=="POST":   
        #stripe payment procesing
        first_name=request.POST.get('fname')
        last_name=request.POST.get('lname')
        company=request.POST.get('company')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        city=request.POST.get('city')
        country=request.POST.get('country')
        order=request.POST.get('order')
        email=request.POST.get('email')
        postcode=request.POST.get('postcode')
        address=request.POST.get('address')
        amount=request.POST.get('orderAmount')
        user=request.user.id
        note=request.POST.get('note')
        myOder=Order(first_name=first_name, last_name=last_name,company_name=company,address=address,phone=phone,
        email=email, postcode=postcode,  note=note, country=country, amount=amount,  order=order, city=city 
        )
        myOder.user=request.user
        myOder.save()
        messages.success(request, 'Success! Your order is successfull, you will get your products in 5 working days')
        return redirect('stripe-session')  
    return render(request, 'shop/checkout.html', { 'stripe_publishable_key':stripe_publishable_key})




def shop(request):
    q=request.GET.get('q') if request.GET.get('q') !=None else ''
    categories=Category.objects.all()
    brands=Brand.objects.all()
    products=Product.objects.all()

    products=products.filter(
        
        Q(title__icontains=q)|
        Q(category__name__icontains=q)|
        Q(brand__name__icontains=q)|
        Q(description__icontains=q)

        ) 
    page_num = request.GET.get('page', 1)
    paginator=Paginator(products, 2)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)
   
   
    context={'products':products, 'page_obj':page_obj, 'categories':categories, 'brands':brands}
    return render(request, 'shop/shop.html', context )

def shop_col4(request):
    q=request.GET.get('q') if request.GET.get('q') !=None else ''
    categories=Category.objects.all()
    brands=Brand.objects.all()
    products=Product.objects.all()
    products=products.filter(
        
        Q(title__icontains=q)|
        Q(category__name__icontains=q)|
        Q(description__icontains=q)

        ) 
    page_num = request.GET.get('page', 1)
    paginator=Paginator(products, 4)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)
   
    
    context={'products':products, 'page_obj':page_obj, 'categories':categories, 'brands':brands}
    return render(request, 'shop/shop_col4.html', context)


@login_required(login_url='login')   
def myorder(request, pk):
    myorder=Order.objects.filter(user=pk)
    page_num = request.GET.get('page', 1)
    paginator=Paginator(myorder, 10)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)
    return render(request, 'shop/order.html', {'orders':myorder, 'page_obj':page_obj})



def profile_address(request, pk):
    user=MyUser.objects.get(pk=pk)
    return render(request, 'shop/billing_address.html', {'user':user})

class Contact(FormView):
    template_name = 'shop/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact-success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)

def contact_success(request):
    return render(request, 'shop/contact-success.html')

def about(request):
    return render(request, 'shop/about.html')

#stripe configuration
@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


class PaymentSuccessView(TemplateView):
    template_name = "shop/payment_success.html"

    def get(self, request, *args, **kwargs):
        session_id = request.GET.get('session_id')
        if session_id is None:
            return HttpResponseNotFound('No response')
        
        stripe.api_key = settings.STRIPE_SECRET_KEY
        session = stripe.checkout.Session.retrieve(session_id)

        order = get_object_or_404(Order, stripe_payment_intent=session.payment_intent)
        order.has_paid = True
        order.save()
        return render(request, self.template_name)

class PaymentFailedView(TemplateView):
   template_name = "shop/payment_failed.html"