import streamlit as st
st.write("<h1>Hello world</h1>",unsafe_allow_html=True)
#ing colour of test
st.write("<h1ss style='color:red;'>hello world</h1>",unsafe_allow_html=True)
st.file_uploader("upload file")
import streamlit as st
import numpy as np

st.set_page_config(layout ="wide")
st.title("Student Management System")
st.sidebar.title("Fee Management System")

st.sidebar.subheader("Add Student")
rollnumber=st.sidebar.number_input("Roll Number")
name=st.sidebar.text_input("Name")
fees=st.sidebar.number_input("Fees")
add=st.sidebar.button("Add")
