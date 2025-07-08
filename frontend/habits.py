import streamlit as st
import requests
import datetime
from habitlogs import log_habit

API_BASE = "http://web:8000/api/"
API_BASE_AUTH = "http://web:8000/auth/"
def show_habit_page():
    st.title("Habit Tracker")
    if "create_page" not in st.session_state:
        st.session_state["create_page"] = False

    if st.button("Create New Habit"):
        st.session_state["create_page"] = True

    if st.session_state["create_page"]:
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
                st.session_state["create_page"] = False
            else:
                st.error(response.json())

    if "show_logs" not in st.session_state:
        st.session_state["show_logs"] = False

    if st.button("Logs"):
        st.session_state["show_logs"] = True

    if st.session_state["show_logs"]:
        token = st.session_state['token']
        log_habit(token)

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

    if st.button("Show Logs"):
        token = st.session_state['token']
        response = requests.get(
            f"{API_BASE}habitlogs/",
            headers={"Authorization": f"Token {st.session_state['token']}"}
        )
        if response.status_code == 200:
            habitlogs = response.json()
            habit_logs = {}
            if habitlogs:
                st.subheader("Your Logs")
                for log in habitlogs:
                    # st.markdown(f"**Habit ID**: {log['habit']} | **Date**: {log['date']} | ✅ Done: {log['status']}")
                    habit = log["habit_name"]
                    habit_logs.setdefault(habit, []).append(log)
                for habit, entries in habit_logs.items():
                    st.subheader(habit)
                    for log in sorted(entries, key = lambda x: x["date"]):
                        st.write(f"📅 {log['date']} — ✅ {log['status']}")

            else:
                st.info("You do not have any logs")
        else:
            st.error(response.json())

    if st.sidebar.button("Logout"):
        requests.post(f"{API_BASE_AUTH}logout/", headers={"Authorization": f"Token {st.session_state["token"]}"})
        st.session_state['token'] = None
        st.rerun()


