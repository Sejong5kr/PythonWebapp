import streamlit as st
import generate_list as gl
import generate_timing_data as gt


def main():
 
    st.write("## 신년을 맞아 세종이가 만든 재미 있는 앱")
    st.write("현재 세종의 PC에 있는 선수들 명단")

    selected= gl.generateList()
    gt.fnGenerate_timing_data(selected)


if __name__ == '__main__' : 
    main()







