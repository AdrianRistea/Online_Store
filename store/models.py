from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)
    active = models.BooleanField(default=True)
    parent_category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)

    def subcategories(self):
        return Category.objects.filter(parent_category=self)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    descriptions = models.TextField()
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='static/product_images/', null=True, blank=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount_price_valid_until = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


# class History(models.Model):
#     text = models.TextField(max_length=400)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.text


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class UserProductPurchased(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product}"

    class Meta:
        unique_together = ['user', 'product']


class Cart(models.Model):
    STATUS = (
        ('open', 'Open'),
        ('closed', 'Closed'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS, default='open')
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f'{self.status} cart of {self.user}'


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.quantity} X {self.product} in {self.cart}'
