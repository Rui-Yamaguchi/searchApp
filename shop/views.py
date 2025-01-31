from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Book, Cart, Favorite, CartBook
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib import messages

def index(request):
    books = Book.objects.all()
    return render(request, 'shop/index.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(user=request.user, book=book).exists()
    return render(request, 'shop/book_detail.html', {'book': book, 'is_favorite': is_favorite})

def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(price__icontains=query) |
            Q(volume_number__icontains=query) |
            Q(publisher__icontains=query)
        )
        print(f"Query: {query}, Results Count: {len(results)}")
    return render(request, 'shop/search_results.html', {'results': results, 'query': query})

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    total_items = cart.total_item_count
    return render(request, 'shop/cart_detail.html', {'cart': cart, 'total_items': total_items})

@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_book, created = CartBook.objects.get_or_create(cart=cart, book=book)
    if not created:
        cart_book.quantity += 1
        cart_book.save()
    return redirect('cart_detail')

@login_required
def remove_from_cart(request, book_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_book = get_object_or_404(CartBook, cart=cart, book_id=book_id)
    if cart_book.quantity > 1:
        cart_book.quantity -= 1
        cart_book.save()
    else:
        cart_book.delete()
    return redirect('cart_detail')

@login_required
def my_page(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('book')
    return render(request, 'shop/my_page.html', {'favorites': favorites})

@login_required
def add_to_favorite(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    Favorite.objects.get_or_create(user=request.user, book=book)
    return redirect('book_detail', book_id=book_id)

@login_required
def remove_from_favorite(request, book_id):
    user = request.user
    favorites = Favorite.objects.filter(user=user, book_id=book_id)
    
    if favorites.exists():
        favorites.delete()
        messages.success(request, "お気に入りから削除しました。")

    return redirect('my_page')

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'shop/signup.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'shop/profile.html')