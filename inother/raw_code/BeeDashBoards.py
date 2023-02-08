import requests
import streamlit as st
from streamlit_lottie import st_lottie
from turtle import right
from streamlit_option_menu import option_menu
from traitlets import default

st.set_page_config(page_title="Головна", page_icon=":honeybee:", layout="wide")

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


selected = option_menu(
    menu_title = None,
    options = ["Головна","Про нас","Робоче місце","Бібліотека"],
    icons=["house-fill","person-lines-fill","person-workspace","collection-fill"],
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
            st.write("**BDB** - це безкоштовний сервіс ***для бджолярів***, сворений для генерування швидких звітів та прийняття миттєвих рішень. Щоб отримати максимальні результати. Звіти генеруються на основі Ваших вхідних данних." )
            st.subheader("Ми працюємо:briefcase: - Ви зростаєте:chart_with_upwards_trend:")

        with right_column:
            st_lottie(lottie_BDB, height=300, key="bee")
        

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

if selected == "Робоче місце":
    st.title(f"You have selected {selected}")    


if selected == "Бібліотека":
    st.title(f"You have selected {selected}")



