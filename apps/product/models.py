from django.db import models
from datetime import datetime
from apps.category.models import Category

from django.conf import settings
domain = settings.DOMAIN

class Product(models.Model):
    name = models.CharField(max_length=255)
    photo = models.URLField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    compare_price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=datetime.now)
    in_offer = models.BooleanField(default=False)

    def get_thumbnail(self):
            return  self.photo

    def __str__(self):
        return self.name