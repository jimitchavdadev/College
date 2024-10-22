<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Registration</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }

        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background-color: white;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h2 {
            text-align: center;
            color: #333;
        }

        .form-group {
            margin-bottom: 15px;
        }

        .form-group label {
            display: block;
            font-weight: bold;
        }

        .form-group input,
        .form-group select {
            width: 100%;
            padding: 8px;
            box-sizing: border-box;
        }

        .form-group input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }

        .form-group input[type="submit"]:hover {
            background-color: #45a049;
        }

        .error-message {
            color: red;
            margin-bottom: 15px;
            font-weight: bold;
        }
    </style>
</head>

<body>
    <div class="container">
        <h2>Student Registration Form</h2>
        <?php
        $name = $dob = $gender = $email = $phone = $address = $age = "";
        $errorMessage = "";

        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $name = htmlspecialchars(trim($_POST['name']));
            $dob = htmlspecialchars(trim($_POST['dob']));
            $gender = htmlspecialchars(trim($_POST['gender']));
            $email = htmlspecialchars(trim($_POST['email']));
            $phone = htmlspecialchars(trim($_POST['phone']));
            $address = htmlspecialchars(trim($_POST['address']));
            $age = htmlspecialchars(trim($_POST['age']));

            // Validation
            if (empty($name) || strlen($name) < 3 || !preg_match("/^[a-zA-Z]+$/", $name)) {
                $errorMessage = "Name must be at least 3 alphabetic characters long.";
            } elseif (empty($dob)) {
                $errorMessage = "Please enter your date of birth.";
            } elseif (empty($gender)) {
                $errorMessage = "Please select your gender.";
            } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
                $errorMessage = "Invalid email format.";
            } elseif (!preg_match("/^\d{10}$/", $phone)) {
                $errorMessage = "Phone number must be exactly 10 digits.";
            } elseif ($age <= 0) {
                $errorMessage = "Age must be a positive number.";
            } elseif (empty($address)) {
                $errorMessage = "Please enter your home address.";
            } else {
                // Display submitted data if validation passes
                echo "<h2>Student Registration Details:</h2>";
                echo "Name: $name<br>";
                echo "Date of Birth: $dob<br>";
                echo "Gender: $gender<br>";
                echo "Email: $email<br>";
                echo "Phone: $phone<br>";
                echo "Address: $address<br>";
                echo "Age: $age<br>";
                exit(); // Stop execution after displaying the details
            }
        }
        ?>

        <form method="post" action="">
            <?php if (!empty($errorMessage)): ?>
                <div class="error-message"><?php echo $errorMessage; ?></div>
            <?php endif; ?>

            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" value="<?php echo $name; ?>">
            </div>

            <div class="form-group">
                <label for="dob">Date of Birth:</label>
                <input type="date" id="dob" name="dob" value="<?php echo $dob; ?>">
            </div>

            <div class="form-group">
                <label for="gender">Gender:</label>
                <select id="gender" name="gender">
                    <option value="">--Select Gender--</option>
                    <option value="Male" <?php if ($gender == "Male") echo "selected"; ?>>Male</option>
                    <option value="Female" <?php if ($gender == "Female") echo "selected"; ?>>Female</option>
                </select>
            </div>

            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" value="<?php echo $email; ?>">
            </div>

            <div class="form-group">
                <label for="phone">Phone Number:</label>
                <input type="text" id="phone" name="phone" value="<?php echo $phone; ?>">
            </div>

            <div class="form-group">
                <label for="age">Age:</label>
                <input type="number" id="age" name="age" value="<?php echo $age; ?>">
            </div>

            <div class="form-group">
                <label for="address">Address:</label>
                <input type="text" id="address" name="address" value="<?php echo $address; ?>">
            </div>

            <div class="form-group">
                <input type="submit" value="Submit">
            </div>
        </form>
    </div>
</body>

</html>