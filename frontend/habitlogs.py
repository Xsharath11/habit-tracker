import streamlit as st
import requests
import datetime

API_BASE = "http://web:8000/api/"
def log_habit(token):
    st.header("Log a Habit")

    headers = {"Authorization": f"Token {token}"}
    habit_response = requests.get(f"{API_BASE}habits/", headers=headers)

    if habit_response.status_code != 200:
        st.error("Could not fetch habits")
        return

    habits = habit_response.json()

    if not habits:
        st.info("No habits found. Create one first")
        return

    habit_names = {habit["name"]: habit["id"] for habit in habits}
    selected_habit = st.selectbox("Select a Habit to log", habit_names.keys())
    selected_date = st.date_input("Date", datetime.date.today())

    if st.button("Submit Log"):
        payload = {
            "habit": habit_names[selected_habit],
            "date": selected_date.isoformat(),
            "status": "Done" 
        }
        response = requests.post(f"{API_BASE}habitlogs/", json=payload, headers=headers)
        if response.status_code == 201:
            st.success("habit logged successfully")
            st.session_state["show_logs"] = False
        elif response.status_code == 400:
            st.error(response.json())
        else:
            st.error("Something Went wrong")




