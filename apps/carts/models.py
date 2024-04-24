from django.db import models
from django.contrib.auth import get_user_model

from apps.products.models import Product

User = get_user_model()

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="user_carts",
        verbose_name="Пользователь"
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )

    def __str__(self):
        return f"{self.user} {self.created}"
    
    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE,
        related_name='cart_items',
        verbose_name="Корзина"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name="product_items",
        verbose_name="Товар"
    )
    quantity = models.PositiveIntegerField(
        default=1, verbose_name="Количество"
    )

    def __str__(self):
        return f"{self.cart} {self.product} {self.quantity}"
    
    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"
    