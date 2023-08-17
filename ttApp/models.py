from django.contrib.auth.models import User
from django.db import models

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    summary = models.TextField()
    description = models.TextField()
    specs = models.TextField()
    shipping_info = models.TextField()
    price = models.FloatField()
    img = models.ImageField(upload_to='img/', null=True, blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    bought = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)



