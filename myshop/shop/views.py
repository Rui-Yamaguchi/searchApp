from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Book, Cart, Favorite
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

def index(request):
    books = Book.objects.all()
    return render(request, 'shop/index.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(user=request.user, book=book).exists()
    else:
        is_favorite = False
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
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.books.add(book)
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'shop/cart_detail.html', {'cart': cart})

@login_required
def remove_from_cart(request, book_id):
    cart = get_object_or_404(Cart, user=request.user)
    book = get_object_or_404(Book, pk=book_id)
    cart.books.remove(book)
    return redirect('cart_detail')

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
        # メッセージを追加する場合
        from django.contrib import messages
        messages.success(request, "お気に入りから削除しました。")

    return redirect('my_page')

@login_required
def my_page(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('book')
    return render(request, 'shop/my_page.html', {'favorites': favorites})

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'shop/signup.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'shop/profile.html')