
from django.urls import path

from .views.home import Index,store
from .views.signup import Signup
from .views.login import Login,logout
from .views.forgetPassword import ForgetPassword
from .views.verifyOtp import VeryfyOTP
from .views.resetPassword import ResetPassword
from .views.userProfile import UserProfile
from .views.products import product
from .views.productDetail import product_detail
from .views.checkout_page import Chckout_Page,Checkout_View
from .views.cart_count import Cart_Count
from .views.wishlist import Wishlist
from .views.cart import add_to_cart,Remove_From_Cart,increment_quantity,decrement_quantity,cart_view,Cart_Totle_Count
# from .views.home import store
from .views.country import get_countries,get_states_by_country,get_cities_by_state


from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   path("",Index.as_view(),name='home'),
   path("signup",Signup.as_view(),name='signup'),
   path("wishlist",Wishlist,name='wishlist'),
   path("login",Login.as_view(),name='login'),
   path("logout",logout,name='logout'),
   path("forget-password",ForgetPassword.as_view(),name="forgetpassword"),
   path("verify-otp", VeryfyOTP.as_view(), name="verifyotp"), 
   path("reset-password", ResetPassword.as_view(), name="resetpassword"), 
   path("user-profile", UserProfile.as_view(), name="userprofile"), 
   path("products", product, name="product"), 
   path("product/<int:product_id>/", product_detail, name="product_detail"),  
   path("cart/add/<int:product_id>/", add_to_cart, name="add_to_cart"),  
   path("cart/remove/<int:product_id>/", Remove_From_Cart, name="remove_from_cart"),  
   path("cart/increment/<int:product_id>/", increment_quantity, name="cart_increment"),  
   path("cart/decrement/<int:product_id>/", decrement_quantity, name="cart_decrement"),  
   path("store", store, name="store"), 
   path("cart", cart_view, name="cart_view"), 
   path("cartcount/", Cart_Count, name="Cart_Count"), 
   path("cart/total/", Cart_Totle_Count, name="cart_total"), 
   path("checkout_page", Chckout_Page, name="checkout_page"), 
   path("checkout/process", Checkout_View, name="checkout_view"), 
   path('api/countries/', get_countries, name='get_countries'),
   path('get-states/<str:country_name>/', get_states_by_country, name='get_states'),
   path('get-cities/<int:state_id>/', get_cities_by_state, name='get_cities_by_state'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
