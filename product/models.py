from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import TextChoices
from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='images/', default='')
    name = models.CharField(max_length=55)
    price = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(9_999_999_999)])
    color = models.CharField(max_length=55)
    memory = models.PositiveIntegerField(validators=[MinValueValidator(8), MaxValueValidator(2_000)])
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class StatusEnum(TextChoices):
    PENDING = 'PENDING', 'pending'
    PROGRESS = 'PROGRESS', 'progress'
    COMPLETED = 'COMPLETED', 'completed'
    FAILED = 'FAILED', 'failed'


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=15, choices=StatusEnum.choices, default=StatusEnum.PENDING)

    def __str__(self):
        return self.user


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.IntegerField()
    price = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(9_999_999_999)])
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.order} - {self.product}"
