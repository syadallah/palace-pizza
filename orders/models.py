from django.db import models

# Create your models here.
class MenuItem(models.Model):
  group = models.CharField(max_length=64)
  item = models.CharField(max_length=64)
    return f"{self.group}, {self.item} | small: ${self.price_sm} | large: ${self.price_lg} | single size: ${self.price}"
