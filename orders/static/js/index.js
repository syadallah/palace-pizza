document.addEventListener('DOMContentLoaded', function() {
  // Retrieve extras and toppings items data from 'storage' <div> (just some
   // random <div> with id='storage') within index.html's DOM. The data is stored
   // as strings that get serialized in views.py before ending up in the DOM.
   storage = document.querySelector('#storage');
   storage_extras = storage.getAttribute('data-storage_extras');
   storage_toppings = storage.getAttribute('data-storage_toppings');
}
