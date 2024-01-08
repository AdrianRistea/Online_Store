from django.contrib import admin
from store.models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)