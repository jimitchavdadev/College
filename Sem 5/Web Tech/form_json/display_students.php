<?php
// Read the JSON file
$jsonData = file_get_contents('students.json');

// Decode the JSON data to a PHP array
$students = json_decode($jsonData, true);

// Check if the file was successfully decoded
if ($students === null) {
    echo "Error reading JSON data";
    exit;
}

// Add some CSS styles to the page
echo "
<style>
    body {
        font-family: Arial, sans-serif;
        margin: 20px;
        background-color: #f0f0f0;
    }
    h1 {
        color: #333;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 20px;
        background-color: #fff;
    }
    table, th, td {
        border: 1px solid #ddd;
    }
    th, td {
        padding: 12px;
        text-align: left;
    }
    th {
        background-color: #f2f2f2;
    }
    tr:hover {
        background-color: #f1f1f1;
    }
</style>
";

// Display the student data in a styled HTML table
echo "<h1>Student Data</h1>";
echo "<table>";
echo "<tr><th>ID</th><th>Name</th><th>Age</th><th>Course</th></tr>";

foreach ($students['students'] as $student) {
    echo "<tr>";
    echo "<td>" . $student['id'] . "</td>";
    echo "<td>" . $student['name'] . "</td>";
    echo "<td>" . $student['age'] . "</td>";
    echo "<td>" . $student['course'] . "</td>";
    echo "</tr>";
}

echo "</table>";
?>
