import streamlit as st

def find_largest(num1, num2, num3):
  """
  This function finds the largest among three numbers.
  """
  largest = num1
  if num2 > largest:
    largest = num2
  if num3 > largest:
    largest = num3
  return largest

st.title("Find the Largest Number")

# Create input fields for the three numbers
num1 = st.number_input("Enter the first number", key="num1")
num2 = st.number_input("Enter the second number", key="num2")
num3 = st.number_input("Enter the third number", key="num3")

# Find the largest number
largest = find_largest(num1, num2, num3)

# Display the results
if st.button("Find Largest"):
  st.write("The largest number is:", largest)
