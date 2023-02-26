import streamlit as st

st.title("Welcome to all ...😊😊😊😊")
st.write('''Hello!
    My name is Shivakant
    Currently,I am a Btech 3rd year student from Mechanical Engineering,
    I am interested in data science and machine learning field.
               ''')
st.snow()


btn_click = st.button("Click Me 👈")

if btn_click == True:
    st.subheader("Try to see the data visualisation of heart disease by clicking on dasboard")
    st.balloons()

    
    