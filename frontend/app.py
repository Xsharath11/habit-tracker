import streamlit as st
import requests

API_BASE_URL = "http://127.0.0.1:8000/auth/" # Base URL for signup

st.title("Habit Tracker")

menu = st.sidebar.selectbox("Menu", ["Signup", "Login"])
st.session_state.setdefault("token", None)

if menu == "Signup":
    st.header("Create New account")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    email = st.text_input("Email")

    if st.button("Sign up"):
        data = {"username": username, "password": password, "email": email}
        response = requests.post(f"{API_BASE_URL}signup/", json=data)

        if response.status_code == 201:
            token = response.json().get("token")
            st.session_state["token"] = token
            st.success("Account created successfully! Logged In")
        else:
            st.error(response.json())

elif menu == "Login":
    st.header("Log in")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        data = {"username": username, "password": password}
        response = requests.post(f"{API_BASE_URL}login/", json=data)

        if response.status_code == 200:
            token = response.json().get("token")
            st.session_state["token"] = token
            st.success("Logged in successfully!")
        else:
            st.error(response.json())

# Logged in state
if st.session_state.get("token"):
    st.sidebar.success("Logged in")
    if st.sidebar.button("Logout"):
        response = requests.post(f"{API_BASE_URL}logout/", headers={"Authorization": f"Token {st.session_state["token"]}"})
        st.session_state["token"] = None
        if response.status_code == 200:
            st.success("Logged out successfully")
            st.rerun()
        else:
            st.error(response.json())

