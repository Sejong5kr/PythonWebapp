import glob
import Athlete
import streamlit as st
import sqlite3

def generateList(col1):
    data_files = glob.glob("*.txt")
    athletes= Athlete.put_to_store(data_files)

    connection = sqlite3.connect('coachdata.sqlite')
    cursor = connection.cursor()

    selected=''
    col1.write("Coach Sejong's List of Athletes")
 
    for each_t in athletes : 
        name = athletes[each_t].name
        dob = athletes[each_t].dob

        cursor.execute("INSERT INTO athletes (name, dob) VALUES (?,?)", (name, dob))
        connection.commit()

        if col1.button(name):
            selected=name

    connection.close()
    return(selected)

