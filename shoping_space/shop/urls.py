from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home, name='home'),
    path('sign', views.Sign_in, name='sign'),
    path('login', views.Log_in, name='login'),
    path('logout', views.Log_out, name='logout'),
    path('cart', views.Cart_add, name='cart'),
    path('fav', views.FavPage, name='fav'),
    path('fav_view', views.Fav_add, name='fav_view'),
    path('remove_cart/<str:cid>', views.RemoveCart, name='remove_cart'),
    path('remove_fav/<str:fid>', views.RemoveFav, name='remove_fav'),
    path('collection', views.Collections, name='collections'),
    path('collection/<str:name>', views.CollectionView, name='collections'),
    path('collection/<str:cname>/<str:pname>', views.ProductDetails, name='product_details'),
    path('addtocart', views.AddToCart, name='addtocart'),
]