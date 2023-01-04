import Athlete
import streamlit as st
import pandas as pd


def fnGenerate_timing_data(col2, selected):
    athletes=Athlete.get_from_store()

    if selected in athletes : 
        sview= pd.Series(athletes[selected].top7())
        col2.write(sview)
        

def fnAddNewData(selected, input):
    athletes=Athlete.get_from_store()
    aName=''

    if selected in athletes : 
        aName=athletes[selected].name

    aFile=aName+'.txt'
    try:
        with open(aFile, 'a') as f:
            f.write(',{}'.format(input))
    except IOError as e:
        print('File error'+str(e))




