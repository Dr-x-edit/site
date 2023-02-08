import streamlit as st
import sqlite3
import pandas as pd
import hashlib
from ast import Not
from asyncio.windows_events import NULL
from re import I
from this import d
from unittest import result
from bleach import clean
from streamlit_option_menu import option_menu
    

def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

conn = sqlite3.connect('Users.db')
c = conn.cursor()



def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT PRIMARY KEY,password TEXT NOT NULL)')


def add_userdata(username,password):
    try:
        c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
        conn.commit()
    except:
        err = st.warning("**Увага!** Користувач з ім'ям *{}* вже зареєстрований".format(new_user))

def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data = c.fetchall()
    return data

def user(username):
    c.execute('SELECT * FROM userstable WHERE username =?',(username,))
    data = c.fetchall()
    return data

def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data
def clear_table():
    c.execute('DROP TABLE userstable')

with st.sidebar:
    login_singup = option_menu(
        menu_title = None,
        options = ["Реєстрація", "Вхід"],
        icons = ["pencil-square","box-arrow-in-right"],
        default_index = 0,
        orientation="horizontal",
    )
if login_singup == "Реєстрація":
    with st.container():
        st.title("Реєстрація")
        st.write("---")
        left_column, right_column = st.columns(2)
        
        with left_column:
            new_user = st.text_input("Ім'я користувача")
            new_password = st.text_input("Пароль", type='password')

            if st.button("Реєстрація"):
                create_usertable()
                result = user(new_user)
                add_userdata(new_user,make_hashes(new_password))
                if result:
                    st.warning("Використайте інше ім'я")
                else:
                    st.success('Вітаємо! Ви зареєструвалися як {}'.format(new_user))
                    st.info("Увійдіть будь ласка!")

        with right_column:
            st.empty()
else:
    with st.container():
        st.title("Вхід")
        st.write("---")
        left_column, right_column = st.columns(2)
        
        with left_column:
            usrename = st.text_input("Ім'я користувача")
            password = st.text_input("Пароль", type='password')
            st.write("---")
            if st.button("Вхід"):
                # if password == 'sdds':
                create_usertable()
                hashed_pswd = make_hashes(password)
                result = login_user(usrename,check_hashes(password,hashed_pswd))
                if result:

                    st.success("Ви увійшли як {}".format(usrename))


                else:
                    st.warning("Не вірне Ім'я користувача чи пароль")

            if st.button("Удалить таблицю"):
                result = clear_table()

        with right_column:
            st.empty()

