<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Form</title>
    <script type="text/javascript">
        // Function for form validation
        function validateForm() {
            var name = document.getElementById("name").value;
            var address = document.getElementById("address").value;
            var age = document.getElementById("age").value;
            var number = document.getElementById("number").value;
            var email = document.getElementById("email").value;
            var gender = document.querySelector('input[name="gender"]:checked');

            // Name validation
            if (name == "") {
                alert("Name must be filled out");
                return false;
            }

            // Address validation
            if (address == "") {
                alert("Address must be filled out");
                return false;
            }

            // Age validation
            if (age == "" || isNaN(age) || age < 18 || age > 100) {
                alert("Please enter a valid age between 18 and 100");
                return false;
            }

            // Number validation
            var phonePattern = /^[0-9]{10}$/;
            if (!phonePattern.test(number)) {
                alert("Please enter a valid 10-digit phone number");
                return false;
            }

            // Email validation
            var emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
            if (!emailPattern.test(email)) {
                alert("Please enter a valid email address");
                return false;
            }

            // Gender validation
            if (!gender) {
                alert("Please select gender");
                return false;
            }

            return true;
        }
    </script>
</head>
<body>
    <h2>Student Form</h2>
    <form action="submit_student.jsp" method="POST" onsubmit="return validateForm()">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name"><br><br>

        <label for="address">Address:</label><br>
        <textarea id="address" name="address" rows="4" cols="50"></textarea><br><br>

        <label for="age">Age:</label><br>
        <input type="number" id="age" name="age" min="18" max="100"><br><br>

        <label for="number">Phone Number:</label><br>
        <input type="text" id="number" name="number"><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email"><br><br>

        <label for="gender">Gender:</label><br>
        <input type="radio" id="male" name="gender" value="Male">
        <label for="male">Male</label>
        <input type="radio" id="female" name="gender" value="Female">
        <label for="female">Female</label><br><br>

        <input type="submit" value="Submit">
    </form>
</body>
</html>

