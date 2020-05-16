from django.contrib import admin
from .models import MenuItem, Topping, Extra, OrderHistory
# Register your models here.

admin.site.register(MenuItem)
admin.site.register(Topping)
admin.site.register(Extra)
admin.site.register(OrderHistory)
