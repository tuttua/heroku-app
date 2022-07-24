import streamlit as st

st.write("Subtraction")

def user_input_features():
    n1=st.number_input("Enter the minuend:")
    n2=st.number_input("Enter the subtrahend:")
    return n1,n2
n1,n2=user_input_features()
if st.button('Calculate'):
    st.write(n1-n2)
