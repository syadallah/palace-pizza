document.addEventListener('DOMContentLoaded', function() {
  // ==================== REGISTER ==============================================

    document.querySelector('#submit-register').onclick = () => {
      // Ensure that all registration information was entered
    const username = document.querySelector('#register-username').value;
    const password = document.querySelector('#register-password').value;
    const first_name = document.querySelector('#register-first-name').value;
    const last_name = document.querySelector('#register-last-name').value;
    const email = document.querySelector('#register-email').value;
    if (username !== '' && password !== '' && first_name !== '' && last_name !== '' && email !== '') {

    // Initialize POST request, extract the CSRF value from the index.html DOM,
    // and put that into the header of the POST request.
    const request = new XMLHttpRequest();
    request.open('POST', '/register');
    const csrf_token = document.querySelector('#csrf').childNodes[0]['value'];
    request.setRequestHeader("X-CSRFToken", csrf_token);
 };
});
