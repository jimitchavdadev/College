<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<%
    String name = request.getParameter("name");
    String address = request.getParameter("address");
    String age = request.getParameter("age");
    String number = request.getParameter("number");
    String email = request.getParameter("email");
    String gender = request.getParameter("gender");

    // Process and display the submitted data
%>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Submitted Data</title>
</head>
<body>
    <h2>Student Details</h2>
    <p><strong>Name:</strong> <%= name %></p>
    <p><strong>Address:</strong> <%= address %></p>
    <p><strong>Age:</strong> <%= age %></p>
    <p><strong>Phone Number:</strong> <%= number %></p>
    <p><strong>Email:</strong> <%= email %></p>
    <p><strong>Gender:</strong> <%= gender %></p>
</body>
</html>

