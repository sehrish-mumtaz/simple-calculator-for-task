import streamlit as st

# Define functions for basic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Title of the app
st.title("Sehrish Calculator")

# Dropdown menu for selecting the operation
operation = st.selectbox("Choose an operation:", ("Add", "Subtract", "Multiply", "Divide"))

# Input fields for the two numbers
num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")

# Perform the selected operation
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
        st.success(f"The result is: {result}")
    elif operation == "Subtract":
        result = subtract(num1, num2)
        st.success(f"The result is: {result}")
    elif operation == "Multiply":
        result = multiply(num1, num2)
        st.success(f"The result is: {result}")
    elif operation == "Divide":
        result = divide(num1, num2)
        st.success(f"The result is: {result}")
