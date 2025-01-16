import pickle
import streamlit as st
from os import path
import numpy as np

st.title("Flower classification App")

file_name = "lr_model.pkl"
with open(path.join("model", file_name) , 'rb') as f:
    lr_model = pickle.load(f)

sl = st.number_input("insert a sepel length")
sw = st.number_input("insert a sepel width")
pl = st.number_input("insert a petal length")
pw = st.number_input("insert a petal width")

if st.button("predict"):
    pred = lr_model.predict(np.array([[sl, sw, pl, pw]]))
    st.write("The flower is:",pred[0])
