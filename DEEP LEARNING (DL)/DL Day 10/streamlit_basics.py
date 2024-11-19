import streamlit as st

# Set the title of the web app
st.title('Hello Streamlit!')

# Add a header
st.header('This is a header')

# Add a text input
name = st.text_input('Enter your name:')

# Add a number input
number = st.number_input('Pick a number:', min_value=0, max_value=100)

# Add a slider
slider_value = st.slider('Select a value:', min_value=0, max_value=200, value=50)

# Add a select box
option = st.selectbox('Choose an option:', ['Yes', 'No', 'None of these'])

# Add a checkbox
checkbox = st.checkbox('Check me')

# Add a button and display a message when clicked
if st.button('Button'):
    st.write(f'Hello, {checkbox}!')