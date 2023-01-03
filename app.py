import streamlit as st
import generate_list as gl
import generate_timing_data as gt
import createDBtables as CDB

Rcount=0
def main():

    st.write("### 신년을 맞아 세종이가 만든 재미 있는 앱")
    st.image("./Welcome.jpg")
    st.write("### 현재 세종의 PC에 있는 선수들의 기록을 보여 줍니다")

    CDB.initDBtables() #This will run only at the 1st time from beginning

    #This will print all athletes name and return selected as your input
    selected= gl.generateList()  

    gt.fnGenerate_timing_data(selected) 

    input = st.text_input(label="Enter your number", value="0.00")
    if (input != '0.00'):
        #This will print the timing data of your selected
        gt.fnAddNewData(selected, str(input))  


if __name__ == '__main__' : 
    main()







