from unicodedata import category
from django.shortcuts import render, redirect
from .models import Product, Order, MyUser, Order, Category, Brand
from django.contrib.auth import authenticate, login, logout
from .forms import MyUserRegistrationForm, ProfileForm, ContactForm
from django.contrib import messages
from django.db.models import Q
from django.views.generic import FormView
from django.urls import reverse_lazy
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
          return redirect ('dashboard')
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
            return redirect('dashboard')
        
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

@login_required(login_url='login')
def checkout(request):
    r='n'
    if request.method=="POST":
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
       
        try:
            myOder.save()
            r='r'
        except:
            r='n'

       
        messages.success(request, 'Success! Your order is successfull, you will get your products in 5 working days')
        #return redirect('home')

          
    return render(request, 'shop/checkout.html', {'r':r})




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