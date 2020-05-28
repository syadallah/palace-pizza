from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from orders.models import MenuItem, Topping, Extra
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.
def index(request):
     context = {
      "user": request.user,
      "menu": MenuItem.objects.all(),
      "toppings": serializers.serialize('json', Topping.objects.all()),
      "extras": serializers.serialize('json', Extra.objects.all()),
     }
     return render(request, "orders/index.html", context)

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
  username = request.POST.get('username')
  password = request.POST.get('password')
  first_name = request.POST.get('first_name')
  last_name = request.POST.get('last_name')
  email = request.POST.get('email')
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

    # ============================ LOGOUT ============================================

def logout_view(request):
  logout(request)
  return render(request, "orders/logout.html", {"message": "Logged out."})

  # ============================ ORDERS ============================================

def orders_view(request):
  if request.method == 'GET':
    return render(request, "orders/orders.html")

  if request.method == 'POST':

    # Save order data to the database
    add = OrderHistory(
            data_group=request.POST['data_group'],
            data_size=request.POST['data_size'],
            extras=request.POST['extras'],
            extras_price=request.POST['extras_price'],
            name=request.POST['name'],
            price=request.POST['price'],
            toppings=request.POST['toppings'],
            user=request.POST['user'],
          )
    add.save()

    # Make API request to Stripe to create a charge -- set your secret key, but
    # remember to change this to your live secret key in production.
    # See your keys here: https://dashboard.stripe.com/account/apikeys.
    try:
      import stripe
      # stripe.api_key = "sk_test_1xe9xL3ilJwRXLABHF1JfPhL00QFOSOlPx"

      # Stripe requires the price to be in the smallest unit of currency, ex.
      # pennies in the US.
      price = int(float(request.POST['price'] + request.POST['extras_price']) * 100)
      charge = stripe.Charge.create(
        amount=price,
        currency="usd",
        source="tok_visa", # obtained with Stripe.js
        description=("Charge for " + request.POST['user']),)
      pass

    # Errors are caught in stripe.error.Carderror.
    except stripe.error.CardError as e:
      body = e.json_body
      err  = body.get('error', {})
      print("Status is: %s" % e.http_status)
      print("Type is: %s" % err.get('type'))
      print("Code is: %s" % err.get('code'))
      print("Param is: %s" % err.get('param')) # 'param' is '' in this case
      print("Message is: %s" % err.get('message'))

    # Too many requests made to the API too quickly.
    except stripe.error.RateLimitError as e:
      pass

    # Invalid parameters were supplied to Stripe's API.
    except stripe.error.InvalidRequestError as e:
      pass

    # Authentication with Stripe's API failed (ex. invalid secret key).
    except stripe.error.AuthenticationError as e:
      pass

    # Network communication with Stripe failed.
    except stripe.error.APIConnectionError as e:
      pass

    # Display a very generic error to the user (might be a good idea to trigger
    # a notification email to the site admin).
    except stripe.error.StripeError as e:
      pass

    # Something else happened, completely unrelated to Stripe
    except Exception as e:
      pass

    print(charge)
  return HttpResponse('Success!')
