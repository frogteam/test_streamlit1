import streamlit as st

st.title("Hello")

kor = st.number_input("국어점수")
math = st.number_input('영어점수')

st.write(kor + math)