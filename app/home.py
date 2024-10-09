import streamlit as st
import streamlit.components.v1 as components

# home.py

def home_page():
    # Your code here
    pass


# Custom HTML and CSS
html_code = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stylish Streamlit Interface</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f0f2f6;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            width: 80%;
            background-color: #fff;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #333;
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 1.5rem;
        }
        p {
            font-size: 1.1rem;
            line-height: 1.8;
            color: #555;
            text-align: justify;
        }
        .btn {
            display: block;
            width: 200px;
            margin: 2rem auto;
            text-align: center;
            background-color: #4CAF50;
            color: white;
            padding: 0.7rem;
            border-radius: 30px;
            font-size: 1rem;
            cursor: pointer;
            text-decoration: none;
        }
        .btn:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to My Streamlit App</h1>
        <p>
            This is a sample interface designed to showcase how you can style your Streamlit application using
            custom HTML and CSS. You can modify the layout, colors, typography, and much more to create an interface
            that reflects your style or brand.
        </p>
        <a href="#" class="btn">Get Started</a>
    </div>
</body>
</html>
'''

# Displaying the HTML in Streamlit
components.html(html_code, height=600)