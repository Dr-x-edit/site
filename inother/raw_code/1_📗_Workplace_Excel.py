from operator import le
from pathlib import Path
import pandas as pd
import plotly_express as px
import streamlit as st
import numpy as np
import streamlit_authenticator as stauth
import os
from deta import Deta
from dotenv import load_dotenv
from streamlit_option_menu import option_menu
import database as db
import reports as rp

load_dotenv(".env")
DETA_KEY = os.getenv("DETA_KEY")
deta = Deta(DETA_KEY)
db = deta.Base("user_db")

def fetch_all_users():
    res = db.fetch()
    return res.items

users = fetch_all_users()




usernames = [user ['key'] for user in users]
names = [user['name'] for user in users]
hashed_password = [user['password'] for user in users]

st.set_page_config(page_title = "Робота з Excel", page_icon = ":green_book:", layout = "wide")


authenticator = stauth.Authenticate(names, usernames, hashed_password,
                                    "beeusers","abcdfe", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Вхід", "main")

if authentication_status == False:
    st.error("Не вірне ім'я користувача або пароль")

if authentication_status == None:
    st.warning("Будь ласка введіль ім'я користувача та пароль")

if authentication_status:

    # st.sidebar.header(f"Ласкаво просимо {name}!")
    # authenticator.logout("Вихід", 'sidebar')
    # st.sidebar.markdown("---")
    st.sidebar.header("Робота з Excel :green_book:"
    )
    check_uploded = st.sidebar.checkbox("Відображати таблицю", value = True)
    multi_uploded = st.sidebar.checkbox("Декілька файлів")
    st.sidebar.markdown("---")
    if multi_uploded:
        uploaded_file_1 = st.sidebar.file_uploader("Виберіть XLSX файл №1", type = 'xlsx')
        uploaded_file_2 = st.sidebar.file_uploader("Виберіть XLSX файл №2", type = 'xlsx')
        uploaded_file_3 = st.sidebar.file_uploader("Виберіть XLSX файл №3", type = 'xlsx')
    else:
        uploaded_file = st.sidebar.file_uploader("Виберіть XLSX файл", type = 'xlsx')
        
    
    
    with st.container():
        left_column, right_column = st.columns(2)

        with left_column:
            st.markdown("# Робота з Excel :green_book:")
            # st.write("""Робота з Excel :green_book:""")
        with right_column:
            st.write(f"#### Ласкаво просимо {name}!")
            authenticator.logout("Вихід", 'main')

    selected = option_menu(
        menu_title = None,
        options = ["Редактор файлу", "Генератор звіту", "Документація"],
        icons = ["file-earmark-plus-fill", "journal-bookmark-fill", "book-fill"],
        default_index = 0,
        orientation = "horizontal",
        )


    if selected == "Редактор файлу":
        
        if multi_uploded:
            st.title(":exclamation: Сторінка в розробці:wrench:")

        else:
            if check_uploded:
                if uploaded_file:
                    with st.container():
                        # st.title("Меню для роботи з файлом!")
                        df = pd.read_excel(uploaded_file, engine = 'openpyxl')
                        st.dataframe(df)
                        
                    with st.container():
                        st.markdown("---")
                        rp.check_colony_simple()
                    st.button("Зберегти")
                else:
                    st.info("Оберіть файл для роботи!")
            else:
                if uploaded_file:
                    rp.check_colony_simple()
                    st.button("Записати")
                    st.button("Зберегти")
                    # st.markdown("---")
                    # df = pd.read_excel(uploaded_file, engine = 'openpyxl')
                    # st.dataframe(df)
                else:
                    st.info("Оберіть файл для роботи!")
                    
                
    if selected == "Генератор звіту":
        st.title(":exclamation: Сторінка в розробці:wrench:")
    
    if selected == "Документація":
        st.title(":exclamation: Сторінка в розробці:wrench:")
                
    

