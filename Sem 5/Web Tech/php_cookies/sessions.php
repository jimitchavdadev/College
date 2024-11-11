<?php
session_start(); 
if (!isset($_SESSION['created'])) {
    $_SESSION['created'] = time(); 
}

if (time() - $_SESSION['created'] > 10) {
    session_unset(); 
    session_destroy(); 
    echo "Session has expired. Please refresh the page to start again.";
    exit; 
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    
    $name = $_POST['name']; 
    $email = $_POST['email']; 
    
    $_SESSION['name'] = $name;
    $_SESSION['email'] = $email;

    echo "Session has been set!<br>";
    echo "Name: " . $_SESSION['name'] . "<br>";
    echo "Email: " . $_SESSION['email'] . "<br>";
    echo "This session will expire in 10 seconds.";
} else {
    echo "No data submitted.";
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Session Example</title>
</head>
<body>
    <form action="sessions.php" method="post">
        Name:<input type="text" name="name"><br>
        E-mail:<input type="text" name="email"><br>
        <input type="submit">
    </form>
</body>
</html>
