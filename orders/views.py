from django.http import HttpResponse
from django.shortcuts import render
from orders.models import MenuItem, Topping
from django.core import serializers
from django.contrib.auth.models import User

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
      "toppings": serializers.serialize('json', Topping.objects.all()),
      "extras": serializers.serialize('json', Extra.objects.all()),

    }
    # print('===== LOGIN ===== context: ', context)
    return render(request, "orders/login.html", context)
# ============================ REGISTER ==========================================

def register_view(request):

  # Grab username & password submitted via POST request and make sure that no
  # fields are empty.
  username = request.POST["username"]
  password = request.POST["password"]
  first_name = request.POST["first_name"]
  last_name = request.POST["last_name"]
  email = request.POST["email"]
  if username == '' or password == '' or first_name == '' or last_name == '' or email == '':
    return HttpResponse('{"success": false, "message": "All fields must be completed."}')
    # Try to see if the username already exists in the database; if not, register
  # a new user.
  try:
    User.objects.get(username=username)
    return HttpResponse('{"success": false, "message": "Username already exists."}')
  except:
     # Create a User instance/object which is used with Django's authentication
    # system.
    user = User.objects.create_user(username, email, password)
    user.first_name = first_name
    user.last_name = last_name
    user.save()

      # Django built-in username & password authentication + login session -- by
    # logging the user in, request.user.is_authenticated == True in the
    # def index(request): route.
    user = authenticate(request, username=username, password=password)
    login(request, user)
    return HttpResponse('{"success": true, "message": ""}')
