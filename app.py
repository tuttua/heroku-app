import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

st.write("Subtraction")
minuend=st.number_input('Enter the minuend')
subtrahend=st.number_input('Enter the subtrahend')
difference=minuend-subtrahend
st.write(minuend, ' - ',subtrahend, ' = ',difference)
