import streamlit as st
from auth import show_auth_page
from habits import show_habit_page

st.set_page_config(page_title="Habit Tracker", layout="centered")

if "token" not in st.session_state:
    st.session_state['token'] = None

if st.session_state['token'] is not None:
    show_habit_page()
else:
    show_auth_page()
