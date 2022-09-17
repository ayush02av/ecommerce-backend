from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class account(AbstractUser):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.username

class buyer(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)

    buyer_account = models.OneToOneField(to="database.account", on_delete=models.CASCADE, related_name="buyer_account")

    def __str__(self):
        return f"Rider | {self.buyer_account.__str__()}"

class seller(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)

    seller_account = models.OneToOneField(to="database.account", on_delete=models.CASCADE, related_name="seller_account")

    def __str__(self):
        return f"Driver | {self.seller_account.__str__()}"

class product(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)

    product_name = models.CharField(max_length=250)
    product_tags = models.ManyToManyField(to="database.tag", related_name="product_tags")

    def __str__(self) -> str:
        return self.product_name

class tag(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)

    tag_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.tag_name

class inventory(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)

    inventory_product = models.ForeignKey(to="database.product", on_delete=models.CASCADE, related_name="inventory_product")
    inventory_seller = models.ForeignKey(to="database.seller", on_delete=models.CASCADE, related_name="inventory_seller")

    inventory_price = models.FloatField()
    inventory_unit = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.inventory_unit} units of {self.inventory_product.__str__()} from {self.inventory_seller.__str__()} at Rs. {self.inventory_price} each"

class cart(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)

    cart_products = models.ManyToManyField(to="database.cart_item", related_name="cart_products")
    cart_buyer = models.OneToOneField(to="database.buyer", on_delete=models.CASCADE, related_name="cart_buyer")

    def __str__(self) -> str:
        return f"Cart of {self.cart_buyer}"

class cart_item(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)

    cart_item_product = models.ManyToManyField(to="database.inventory", related_name="cart_item_product")
    cart_item_units = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.cart_item_units} units of {self.cart_item_product.__str__()}"

class order(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)

    order_items = models.ManyToManyField(to="database.order_item", related_name="order_items")
    order_buyer = models.ForeignKey(to="database.buyer", on_delete=models.SET_NULL, null=True, related_name="order_buyer")

    order_units = models.IntegerField()
    order_total_price = models.FloatField()

    def __str__(self) -> str:
        return f"{self.order_units} units of order amount Rs. {self.order_total_price}"

class order_item(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)

    order_item_name = models.CharField(max_length=250)
    order_item_seller = models.ForeignKey(to="database.seller", on_delete=models.SET_NULL, null=True, related_name="order_item_seller")
    order_item_units = models.IntegerField()
    order_item_price = models.FloatField()
    order_item_total_price = models.FloatField()

    def __str__(self) -> str:
        return f"{self.order_item_units} units of {self.order_item_name} of Rs. {self.order_item_price} each = Total Rs. {self.order_item_total_price}"