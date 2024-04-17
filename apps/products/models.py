from django.db import models

from apps.categories.models import Category

# Create your models here.
class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name="category_products",
        verbose_name="Категория",
        blank=True, null=True
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    price = models.PositiveIntegerField(
        verbose_name="Цена"
    )
    image = models.ImageField(
        upload_to='product_images/',
        verbose_name="Фотография"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создание"
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"