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

class Extra(models.Model):
  item      = models.CharField(max_length=64)
  price_sm  = models.DecimalField(max_digits=5, decimal_places=2)
  price_lg  = models.DecimalField(max_digits=5, decimal_places=2)
  def __str__(self):
    return f"{self.item}"
    
class OrderHistory(models.Model):
  created       = models.DateTimeField(auto_now_add=True)
  data_group    = models.CharField(max_length=64, default=None)
  data_size     = models.CharField(max_length=64, default=None)
  extras        = models.CharField(max_length=64, default=None)
  extras_price  = models.DecimalField(max_digits=5, decimal_places=2, default=None)
  name          = models.CharField(max_length=64, default=None)
  price         = models.DecimalField(max_digits=5, decimal_places=2, default=None)
  toppings      = models.CharField(max_length=64, default=None)
  user          = models.CharField(max_length=64, default=None)
  def __str__(self):
    return f"created: {self.created} | data_group: {self.data_group} | data_size: {self.data_size} | extras: {self.extras} | extras_price: {self.extras_price} | name: {self.name} | price: {self.price} | toppings: {self.toppings} | user: {self.user}"
