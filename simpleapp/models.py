from django.core.cache import cache
from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    description = models.TextField()
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)],
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='products',
    )
    price = models.FloatField(
        validators=[MinValueValidator(0.0)],
    )

def __str__(self):
    """
    Returns a string representation of the object.

    This method formats the object's name and description to create a string
    that represents the object. The name is converted to title case using the
    `title()` method, and the description is truncated to the first 10
    characters using slicing.

    Returns:
        str: The string representation of the object, in the format
        "<name_title>: <description_10>".
    """
    name_title = self.name.title()
    description_10 = self.description[:10]
    return f'{name_title}: {description_10}'

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # сначала вызываем метод родителя, чтобы объект сохранился
        cache.delete(f'product-{self.pk}')  # затем удаляем его из кэша, чтобы сбросить его


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()


class Subscription(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
