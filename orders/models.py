from django.db import models

# Create your models here.
class MenuItem(models.Model):
  group = models.CharField(max_length=64)
  item = models.CharField(max_length=64)
  price_sm  = models.DecimalField(max_digits=5, decimal_places=2)
  price_lg  = models.DecimalField(max_digits=5, decimal_places=2)
  price     = models.DecimalField(max_digits=5, decimal_places=2)
  def __str__(self):
    return f"{self.group}, {self.item} | small: ${self.price_sm} | large: ${self.price_lg} | 1 size: ${self.price}"
    
class Topping(models.Model):
  item      = models.CharField(max_length=64)
  def __str__(self):
    return f"{self.item}"
