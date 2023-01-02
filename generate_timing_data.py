import Athlete
import streamlit as st
import cgi


def fnGenerate_timing_data(selected):
    athletes=Athlete.get_from_store()
    #form_data= cgi.FieldStorage()
    #athlete_name= form_data[selected].value
    
    # for each_t in athletes : 
    #     if athletes[each_t].name == selected:
    #         st.write(athletes[each_t].top3())

    if selected in athletes : 
        st.write(athletes[selected].top3())




