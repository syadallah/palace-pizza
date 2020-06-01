# Pinpcchios-pizza

# Description

It is a website built using Django that features the menu for a restaurant called "Palace Pizza & Subs" and allows visitors to create a profile, login, select items from the menu to order, view the total price of the order, and "place" an order. When an order is placed, a record of it is stored in an sqlite3 database (a local database only used for development purposes).


# Configuration, Structure - Run Locally

- Navigate to the ~/project3 folder and run pip3 install -r requirements.txt to make sure that Django is installed -- requirements.txt lists Django==3.0.6

- Start the Django pizza application from within ~/project3 by running:

  $ python manage.py runserver

  ... and the website should be accessible at 127.0.0.1:8000.


  > Within the pizza/ folder:

    1. settings.py -- the only thing which has been added to it are some settings involving the static/ folder.

    2. urls.py
      - links "" to orders/urls.py
      - links "admin/" to a built-in Django app which allows a GUI to interact with and modify the sqlite3 database

  > Within the orders/ folder:

    1. urls.py -- establishes all of the URL syntax for the orders app (which has been linked from the urls.py file within the pizza/ folder), and links these URL routes to functions within the views.py file

    2. views.py -- controls what happens when a user visits a URL route (acts like app.py, or application.py, in a FLASK application)

    3. models.py -- create the structure of tables to be used with the sqlite3 database
      - to create the SQL commands to reflect the changes to any tables within models.py, you create a "migration" file, which is stored in ~/orders/migrations/, by running:

        $ python manage.py makemigrations

      - to apply the SQL located within migration files and alter the database, run:

        $ python.manage.py migrate

    4. admin.py -- add models from ~/orders/models.py to admin.py in order to track them using the built-in Django admin GUI

- To open the Django shell where you can run Python commands, including commands that can manipulate the sqlite3 database, navigate to ~/project3 and run:

    $ python manage.py shell

# What's contained in the files

_login.html, views.py_
  - When a user visits the site they are given an option to login or to register a new account:

    1. If a user tries to register, views.py makes sure that all required fields are filled out and if so then a new 'user' object is created via Django's built-in User model imported from django.contrib.auth.models and the data is stored in the database, and then the user is "logged in" through Django's built-in authentication() and login() functions imported from django.contrib.auth.

    2. If a user tries to log in, views.py uses the authentication() function to ensure that they have a correct combination of username & password, and if so then it uses the login() function to log them in and create a user object associated with the account. Both functions are imported from django.contrib.auth.

_index.html, index.js, models.py, views.py_
  - The index.html page displays a header with the username, a logout link, a link to view any items that have been added to the order (aka, "shopping cart"), and a counter which keeps track of the number of items added to the order.

  - Below the header there are two sections: the menu, and a list of currently selected items. The menu is divided into 6 categories with each item listed by price, size, and selectable by clicking on its checkbox. When an item's checkbox is checked, that item is included in the list of currently selected items. The data for these menu items, toppings, and extras, are made available to index.html by retrieving them from the sqlite3 database which come from the MenuItem, Extra, and Topping models that are imported from orders.models and exist within the file ~/orders/models.py. The data is stored in a variable named "context" which is passed to index.html from views.py. The data can then be referenced directly from within index.html using templating syntax, ex. {{ user }}, {{ menu }}, etc.

  - Multiple items can be added to the list simultaneously, -except- any items with toppings or extras that come in both Small or Large sizes -- in these cases, only either the Small or the Large option can be selected, not both (this was a design decision that could be better). The reason is that when an item with toppings or extras is selected, a new row is added beneath that item that allows the user to select the different toppings or extras options, and for space reasons it was decided to only allow one of either a Small or Large option to be selected at a time.

  - Once the user is satisfied with their selections, they can hit the "Add to Order" button to move these items into localStorage, and the "x items ordered" counter is updated to reflect the total number of items added to the order (aka, the "shopping cart"). This clears all of the items in the list of currently selected items. Note: at this point, if a user had previous selected a Small item with toppings or extras and added that to their order, they could now select a Large version of the same item and add it to their order. This is a sort of work-around for the multiple sizes exclusion problem mentioned earlier.

  - Once a user is satisfied with their order, they can hit the "View Orders" button in the header which takes them to the orders.html page where they can then view their total order and the total price.

_orders.html, orders.js, views.py_
  - At the top of the orders.html page the displayed header is similar to the one on index.html. There is also a "Back to Menu" button which links back to index.html.

  - The main section of the page shows a list which represents the current order, aka "shopping cart". It consists of a simple header that reads "Order:" along with a button that reads "Place Order". These two items act as a small header for this section, and are dynamically generated with JavaScript from within orders.js.

  - Next, any items in localStorage that have their "user" attribute equal to the user name that is extracted from the DOM are displayed in a list, along with their individual price, and the total price for all items.

  - If the user is satisfied with their order, they can hit the "Place Order" button which does three things:

    1. Store the localStorage data that is associated with all of the items in the order in the sqlite3 database.

    2. Create a "charge" object using the Stripe library and send relevant data about the order to the Stripe API to process the money transaction (currently only works in testing mode, not ready for production).

    3. Erase all of the order items from localStorage, remove the order header (not the main page header) and generate a message that reads "Your order has been placed!" using JavaScript from orders.js to replace the order header.
