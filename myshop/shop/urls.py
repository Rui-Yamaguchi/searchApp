from django.urls import path
from shop import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:book_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('my_page/', views.my_page, name='my_page'),
    path('add_to_favorite/<int:book_id>/', views.add_to_favorite, name='add_to_favorite'),
    path('my_page/remove/<int:book_id>/', views.remove_from_favorite, name='remove_from_favorite'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('search/', views.search, name='search'),
    path('accounts/profile/', views.profile, name='profile'),
]