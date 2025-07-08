import streamlit as st
import requests

API_BASE = "http://web:8000/auth/" #TODO: Use st.secrets

def show_auth_page():
    st.title("Login or Signup")

    mode = st.radio("Chosse", ["Login", "Signup"])

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    email = st.text_input("Email") if mode == "Signup" else "" 

    if st.button(mode):
        data = {"username": username, "password": password}
        if mode == "Signup":
            data["email"] = email
        endpoint = "signup/" if mode == "Signup" else "login/"

        response = requests.post(API_BASE+endpoint, json=data)
        if response.status_code == 200 or response.status_code == 201:
            st.session_state["token"] = response.json().get("token")
            st.success(f"{mode} Successful!")
            st.rerun()
        else:
            st.error(response.json())

    # if st.session_state["token"]:
    #     if st.button("Logout"):
    #         requests.post(API_BASE+"logout/", headers={"Authorization": f"Token {st.session_state['token']}"})
    #         st.session_state['token'] = None
    #         show_auth_page()
    #         # st.rerun()






