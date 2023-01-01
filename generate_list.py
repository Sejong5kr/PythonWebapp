import glob
import Athlete
import streamlit as st


def generateList():
    data_files = glob.glob("*.txt")
    athletes= Athlete.put_to_store(data_files)

    selected=''
    st.write("Coach Sejong's List of Athletes")
    for each_t in athletes : 
        if st.button(athletes[each_t].name):
            selected=athletes[each_t].name

    st.write('You selected '+ selected)
    return(selected)

