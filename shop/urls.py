from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView
from . views import Contact, PaymentFailedView, PaymentSuccessView,checkout

urlpatterns = [
    path('', views.index, name="home" ),
    path('view-cart/', views.viewCart, name="view-cart" ),
    path('view-wishlist/', views.viewWishList, name="view-wishlist" ),
    path('login/', views.loginPage, name="login" ),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('contact/', Contact.as_view(), name='contact'),
    path('contact/success', views.contact_success, name='contact-success'),
    path('register/', views.register, name="register" ),
    path('shop/', views.shop, name="shop" ),
    path('about/', views.about, name="about" ),
    path('shop-col4/', views.shop_col4, name="shop-col4" ),
    path('dashboard/', views.dashboard, name="dashboard" ),
    path('profile/<int:pk>', views.profile, name="profile" ),
    path('myorder/<int:pk>', views.myorder, name="myorder" ),
    path('billing-address/<int:pk>', views.profile_address, name="billing-address" ),
    path('checkout/', views.checkout, name="checkout" ),
    path('product-details/<int:pk>', views.productDetails, name="product-details" ),
    #social login
    path("accounts/", include("allauth.urls")),

    #strip url
    path('config/', views.stripe_config),
    #path('create-checkout-session/', views.create_checkout_session, name='stripe-session'),
    path('success/', PaymentSuccessView.as_view(), name='success'),
    path('failed/', PaymentFailedView.as_view(), name='failed'),
   

  
]

