document.addEventListener('DOMContentLoaded', function() {
    // Dummy user data
    const users = [
        { email: 'user1', password: 'password1' },
        { email: 'user2', password: 'password2' }
    ];

    // Function to authenticate user
    function authenticate() {
        const email = document.querySelector('input[type="email"]').value;
        const password = document.querySelector('input[type="password"]').value;

        const user = users.find(user => user.email === email && user.password === password);

        if (user) {
            alert('Authentication successful! 🎉');
            // Redirect to dashboard page
            window.location.replace('/Home Page/Home.html');
        } else {
            alert('Authentication failed. Please check your email and password. 😞');
        }
    }

    // Event listener for submit button click
    document.getElementById('submitButton').addEventListener('click', function(event) {
        event.preventDefault(); // Prevent the default form submission
        authenticate();
    });
});