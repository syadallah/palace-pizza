// Initialize POST request, extract the CSRF value from the index.html DOM,
// and put that into the header of the POST request
const request = new XMLHttpRequest();
const csrf_token = document.querySelector('#csrf').childNodes[1]['value'];
request.open('POST', '/test');
request.setRequestHeader("X-CSRFToken", csrf_token);

// Callback function for when request completes
request.onload = () => {
  // console.log('request loaded');

  // Extract responseText for fun
  // const data = request.responseText;
  // console.log(data);
};

// Add data to send with request
// const data = new FormData();

// Send request
request.send();
// return false;
