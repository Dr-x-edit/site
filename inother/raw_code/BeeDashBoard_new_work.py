from asyncio.windows_events import NULL
from typing import Any
from unittest import result
from pyparsing import empty
import requests
import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
import extra_streamlit_components as stx
import database as db
import hashlib
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import os
from deta import Deta
from dotenv import load_dotenv



st.set_page_config(page_title="BeeDashBoard", page_icon=":honeybee:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")

lottie_BDB = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_5f2kwbj1.json")
lottie_BDB_1 = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_uuulvovp.json")
lottie_BDB_2 = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_mul4s5jq.json")


load_dotenv(".env")
DETA_KEY = os.getenv("DETA_KEY")
deta = Deta(DETA_KEY)
db = deta.Base("user_db")




def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()


def insert_user(username, name, password):
    try:
        db.insert({"key": username, "name": name, "password": password})
        st.success('Вітаємо! Ви зареєструвалися як {}'.format(new_user))
        st.info("Увійдіть будь ласка!")
    except:
        st.error("**Увага!** Користувач з ім'ям *{}* вже зареєстрований".format(new_user))
        st.info("Використайте інше ім'я")
        

def fetch_all_users():
    res = db.fetch()


def get_user(new_user):
    db.get(new_user)

def user(key):
    db.fetch(key)

st.sidebar.success("Select a demo above.")

selected = option_menu(
    menu_title = None,
    options = ["Головна","Реєстрація","Про нас"],
    icons=["house-fill","person-plus-fill","person-lines-fill"],
    default_index=0,
    orientation= "horizontal",
)
if selected == "Головна":
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)

        with left_column:
            st.title("Вітаємо Вас на BDB! :wave:")
            st.subheader("Що таке BDB?")
            st.write("""**BDB** - це безкоштовний сервіс ***для бджолярів***, сворений для генерування швидких звітів та прийняття миттєвих рішень. 
                    Щоб отримати максимальні результати. Звіти генеруються на основі Ваших вхідних данних.
                    Для користуванням сервісом Вам необхідно пройти швидку реєстрацію.""" )
            st.subheader("Ми працюємо:briefcase: - Ви зростаєте:chart_with_upwards_trend:")

        with right_column:
            st_lottie(lottie_BDB, height=300, key="bee")

if selected == "Реєстрація":
    with st.container():
            st.title("Реєстрація")
            st.write("---")
            left_column, right_column = st.columns(2)
            
            with left_column:
                st.info("Поля відмічені * обов'язкові для заповнення!")
                new_user = st.text_input("Ім'я користувача*")
                new_name = st.text_input("Ваше ім'я*")
                new_password = st.text_input("Пароль*", type='password')
                hashed_password= make_hashes(new_password)
                
                if new_user:
                    if len(new_name) > 0:
                        if len(new_password) > 0:
                            if st.button("Реєстрація"): 
                                insert_user(new_user,new_name,hashed_password)
                        else:
                            st.warning("Введіть пароль.")
                    else:
                        st.warning("Введіть Ваше ім'я.")    
                else:
                    st.warning("Введіть ім'я користувача.") 








                # if st.button("Реєстрація"):
                #     result =    user(new_user)
                #     insert_user(new_user,new_name,hashed_password)
                #     while new_user in result:
                #         st.success('Вітаємо! Ви зареєструвалися як {}'.format(new_user))
                #         st.info("Увійдіть будь ласка!")
                # else:
                #     st.info("asssa")

                    # if new_user == get_user(new_user):
                                
                    #     insert_user(new_user,new_name,hashed_password)
                    #     st.success('Вітаємо! Ви зареєструвалися як {}'.format(new_user))
                    #     st.info("Увійдіть будь ласка!")    
                    # else:
                    #     st.error("Користувач з іменем {} вже зареєстрований!".format(new_user))
                        
            
            with right_column:
                st.empty()


if selected == "Про нас":
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)

        with left_column:
            st_lottie(lottie_BDB_1, height=400, key="bees")

        with right_column:
            st.subheader("Вітаю! Радий познайомитив вас з нашою командою!")
            st.write("---")
            st.write('''
                Вісім привіт мене звуть Вова і я поки єдиний розробник даного сервісу.
                Мені дуже подобається займатися бджільництвом. Спостерігати за розвитком колоній. Робити записи при перегляді кожної колонії.
                У мене зібралося багато таких записів і тому я вирішив їх спочатку систематизувати у електронній таблиці Excel. 
                А згодом  виникла ідея автоматизувати генерацію звітів з перегляду. І читати їх у зручному форматі.
            ''')
            st.write("[Зв'язатися зі мною :e-mail:](https://www.facebook.com/drzyama)")
    st.write("---")
    with st.container():
        st.header("Напишіть нам:")
        left_column, right_column = st.columns(2)

        with left_column:
            contact_form = '''
            <form action="https://formsubmit.co/shevchenko.v.vladimirovich@gmail.com" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Ваше ім'я" required>
                <input type="email" name="email" placeholder="Ваш e-mail" required>
                <textarea name="massage" placeholder="Ваше повідомлення" required></textarea>
                <button type="submit">Send</button>
            </form>
            '''
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st_lottie(lottie_BDB_2, height=250, key="mail")



