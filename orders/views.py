from django.http import HttpResponse
from django.shortcuts import render
from orders.models import MenuItem
from django.core import serializers

# Create your views here.
def index(request):
    return render(request, "orders/index.html")
def login_view(request):
  # POST
  if request.method == 'POST':

    # Grab username & password submitted via POST request & make sure that both
    # fields are not empty
    username = request.POST["username"]
    password = request.POST["password"]
    if username == '' or password == '':
      return HttpResponse('{"success": false, "message": "Both username and password are required."}')

    # Django built-in username & password authentication + login session -- by
    # logging the user in, request.user.is_authenticated == True in the
    # def index(request): route.
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return HttpResponse('{"success": true, "message": ""}')
    else:
      return HttpResponse('{"success": false, "message": "Invalid username and/or password."}')

  # GET
  else:
    context = {
      "menu": MenuItem.objects.all(),
    }
    # print('===== LOGIN ===== context: ', context)
    return render(request, "orders/login.html", context)
