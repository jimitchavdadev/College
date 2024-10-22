<?php
$x = 5;
$y = "John";
echo "$x\n";
var_dump(5);
var_dump("John");
var_dump(3.14);
var_dump(true);
var_dump([2, 3, 56]);
var_dump(NULL);

function myTest($x)
{
    // using x inside this function will generate an error
    echo "<p>Variable x inside function is: $x</p>";
}
myTest(5);

$txt1 = "Learn PHP";
$txt2 = "W3Schools.com";

echo "<h2>$txt1</h2>";
echo "<p>Study PHP at $txt2</p>";
