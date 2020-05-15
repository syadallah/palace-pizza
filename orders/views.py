from django.http import HttpResponse
from django.shortcuts import render
from orders.models import MenuItem
from django.core import serializers

# Create your views here.
def index(request):
    return render(request, "orders/index.html")
def login_view(request):

    context = {
      "menu": MenuItem.objects.all(),
    }
    # print('===== LOGIN ===== context: ', context)
    return render(request, "orders/login.html", context)
