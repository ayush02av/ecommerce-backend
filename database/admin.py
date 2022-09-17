from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.account)
admin.site.register(models.buyer)
admin.site.register(models.seller)
admin.site.register(models.product)
admin.site.register(models.tag)
admin.site.register(models.inventory)
admin.site.register(models.cart)
admin.site.register(models.cart_item)
admin.site.register(models.order)
admin.site.register(models.order_item)