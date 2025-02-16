<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name']; 
    $email = $_POST['email'];
    
    setcookie("name", $name, time() + 60, "/");
    setcookie("email", $email, time() + 60, "/");

    header("Location: " . $_SERVER['PHP_SELF']); 
    exit; 
} 
?>

<!DOCTYPE html>         
<html>
    <body>
        <?php 
            if (isset($_COOKIE["name"]) && isset($_COOKIE["email"])) {
                echo "Cookies have been set!<br>";
                echo "Name: " . $_COOKIE["name"] . "<br>";
                echo "Email: " . $_COOKIE["email"] . "<br>";
            } else {
                echo "No cookies set yet.";
            }
        ?>
        <form action="" method="post">
            Name: <input type="text" name="name"><br>
            E-mail: <input type="text" name="email"><br>
            <input type="submit">
        </form>
    </body>
</html>
