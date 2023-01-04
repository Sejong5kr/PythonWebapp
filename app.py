import streamlit as st
import generate_list as gl
import generate_timing_data as gt
import createDBtables as CDB

st.write("### 신년을 맞아 세종이가 만든 재미 있는 앱")
st.image("./Welcome.jpg")
st.write("### 현재 세종의 PC에 있는 선수들의 기록을 보여 줍니다")

col1, col2 = st.columns([2,1])

if "changed" not in st.session_state:
    st.session_state["changed"]=False

if "selected" not in st.session_state:
    st.session_state["selected"]='None'

def fnCheckChanged():
    st.session_state["changed"]=True

def main():
    CDB.initDBtables() #This will run only at the 1st time from beginning

    #This will print all athletes name and return selected as your input
    selected= gl.generateList(col1)  
    if (selected==''):
        selected=st.session_state["selected"]
    else :
        st.session_state["selected"]=selected

    gt.fnGenerate_timing_data(col2, selected) 

    input = col1.text_input(label="Enter your number", value="0.00", on_change=fnCheckChanged)
    if ((input != '0.00') and (input != '') and (st.session_state["changed"])):
        gt.fnAddNewData(selected, input)  
        st.session_state["changed"]=False


if __name__ == '__main__' : 
    main()







