import streamlit as st
import time
import numpy as np
import streamlit_authenticator as stauth
import os
from deta import Deta
from dotenv import load_dotenv
import database as db

load_dotenv(".env")
DETA_KEY = os.getenv("DETA_KEY")
deta = Deta(DETA_KEY)
db = deta.Base("user_db")

st.set_page_config(page_title="Workplace Library", page_icon=":books:")

def fetch_all_users():
    res = db.fetch()
    return res.items

users = fetch_all_users()


usernames = [user ['key'] for user in users]
names = [user['name'] for user in users]
hashed_password = [user['password'] for user in users]



authenticator = stauth.Authenticate(names, usernames, hashed_password,
                                    "beeusers","abcdfe", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Вхід", "main")

if authentication_status == False:
    st.error("Не вірне ім'я користувача або пароль")

if authentication_status == None:
    st.warning("Будь ласка введіль ім'я користувача та пароль")

if authentication_status:

    st.sidebar.title(f"Ласкаво просимо {name}!")
    authenticator.logout("Вихід", 'sidebar')
    st.sidebar.header("Workplace Library :books:")

    st.markdown("# Workplace Library :books:")
    st.write(
        """Work with Library :books:"""
    )
