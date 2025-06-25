import streamlit as st
import requests
import datetime

API_BASE = "http://127.0.0.1:8000/api/"
API_BASE_AUTH = "http://127.0.0.1:8000/auth/"
def show_habit_page():
    st.title("Habit Tracker")

    st.subheader("Create New Habit")
    name = st.text_input("Habit Name")
    created_at = st.date_input("Start Date", value=datetime.date.today())

    if st.button("Create Habit"):
        token = st.session_state['token']
        response = requests.post(
            f"{API_BASE}habits/", 
            headers={
                "Authorization": f"Token {token}",
                "Content-Type": "application/json",
            },
            json = {"name": name, "created_at": str(created_at)},
        )
        if response.status_code == 201:
            st.success("Habit Created!")
        else:
            st.error(response.json())
    
    if st.button("Show habits"):
        token = st.session_state['token']
        response = requests.get(
            f"{API_BASE}habits/",
            headers={"Authorization": f"Token {st.session_state['token']}"}
        )
        if response.status_code == 200:
            habits = response.json()
            if habits:
                st.subheader("Your Habits")
                for habit in habits:
                    st.markdown(f"- **{habit['name']}** (Created on: {habit['created_at']})")
            else:
                st.info("You do not have any habits")
        else:
            st.error(response.json())

    if st.sidebar.button("Logout"):
        requests.post(f"{API_BASE_AUTH}logout/", headers={"Authorization": f"Token {st.session_state["token"]}"})
        st.session_state['token'] = None
        st.rerun()


