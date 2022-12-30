import streamlit as st

with open('sketch.txt','r') as fd:
    result=fd.readlines()
    st.write(result)


