from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    volume_number = models.IntegerField(default=1)
    publisher = models.CharField(max_length=100, default='Unknown Publisher')
    image = models.ImageField(upload_to='manga/', null=True, blank=True)
    image_name = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - Volume {self.volume_number}"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return sum(cart_book.book.price * cart_book.quantity for cart_book in self.cart_books.all())

    @property
    def total_item_count(self):
        return sum(cart_book.quantity for cart_book in self.cart_books.all())

class CartBook(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_books', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='book_carts', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='favorited_by')
    created_at = models.DateTimeField(auto_now_add=True)