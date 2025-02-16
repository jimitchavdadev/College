const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
const PORT = 3000;

// Middleware to parse JSON data and URL-encoded data
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Serve static files from the public directory
app.use(express.static('public'));

// Middleware for validating username and password
const validateUser = (req, res, next) => {
    const { username, password } = req.body;

    if (!username || !password) {
        return res.sendFile(path.join(__dirname, 'public', 'auth_fail.html'));
    }

    if (username.length < 5) {
        return res.sendFile(path.join(__dirname, 'public', 'auth_fail.html'));
    }

    if (password.length < 8) {
        return res.sendFile(path.join(__dirname, 'public', 'auth_fail.html'));
    }

    next(); // Proceed to the next middleware or route handler
};

// Serve the form page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Route to handle user registration/login
app.post('/auth', validateUser, (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'auth_success.html'));
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});