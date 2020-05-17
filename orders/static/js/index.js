document.addEventListener('DOMContentLoaded', function() {
  // Retrieve extras and toppings items data from 'storage' <div> (just some
   // random <div> with id='storage') within index.html's DOM. The data is stored
   // as strings that get serialized in views.py before ending up in the DOM.
   storage = document.querySelector('#storage');
   storage_extras = storage.getAttribute('data-storage_extras');
   storage_toppings = storage.getAttribute('data-storage_toppings');

   // Attach 'click' event listeners to all <input> checkboxes on page load
inputs = document.querySelectorAll('input')
for (let i = 0; i < inputs.length; i++) {
  inputs[i].addEventListener('click', function() {
    select_item(this);
  });
};
// Create list to keep track of active menu item selections, initialize total
// price, initialize the total number of items that have been ordered (ie. the
// number of items in the shopping cart), go through localStorage and actually
// count the number of items that are associated with the currently logged in
// user (which is obtained from the DOM) & add that number to the DOM on intial
// page load, set the total price of current selections (which should be 0) to
// $0 on initial page load
active_selections = []
let total_price = 0;
let items_ordered_count = 0;
let user = document.querySelector('#user').innerHTML;

for (let j = 0; j < localStorage.length; j++) {
  if (JSON.parse(localStorage.getItem(j)) !== null &&
      JSON.parse(localStorage.getItem(j))['user'] === user) {
    items_ordered_count++;
  };
};

document.querySelector('#total_price').append(total_price);
document.querySelector('#number-of-items-ordered').innerHTML = items_ordered_count;

// Creatr checkboc for topping and Extra

function create_checkbox(price) {
   const checkbox = document.createElement('input');
   checkbox.className = tr_id;

   checkbox.setAttribute("data-price", price);
   checkbox.type = 'checkbox';

// The onclick function for each checkbox updates the count for the total
// number of checkboxes selected.
checkbox.onclick = function() {
  let count = 0;
  list = document.getElementsByClassName(tr_id);
  for (let i = 0; i < list.length; i++) {
    if (list[i].checked === true) {
      count++;
    };
  };


}
