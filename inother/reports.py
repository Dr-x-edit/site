from codecs import ignore_errors
from numpy import datetime64
import streamlit as st
import pandas as pd
import plotly_express as px
import numpy as np



def check_colony_simple(df, uploaded_file):
    
    st.header('Бланк перегляду')
    st.write("Бланк створено для зручного додавання данних до Вашого файлу")
    # st.markdown("---")
    with st.form("Бланк перегляду", clear_on_submit=True):
        with st.container():
            date_check, namber_of_hive = st.columns(2)

            with date_check:
                date = st.date_input("Дата огляду:")

            with namber_of_hive:
                n_hive = st.number_input("Номер вулика:", min_value = 0, format = "%i", step = 1)

        # st.markdown("---")
        with st.expander("Сім'я та матка"):

            with st.container():
                general_status, status_colony, queen_info = st.columns(3)

                with general_status:
                    st.write("#### Загальні дані:")
                    st.markdown("---")

                    gs1 = st.radio("Матка", options = ['Так', '-','Ні'], index = 1, horizontal = True)
                    gs2 = st.radio("Маточники", options = ['Так', '-','Ні'], index = 1, horizontal = True)
                    gs3 = st.radio("Яйця", options = ['Так', '-', 'Ні'], index = 1, horizontal = True)
                    gs4 = st.radio("Відкритий розплід", options = ['Так', '-','Ні'], index = 1, horizontal = True)
                    gs5 = st.radio("Закритий розплід", options = ['Так', '-','Ні'], index = 1, horizontal = True)
                    gs6 = st.radio("Трутовий розплід", options = ['Так', '-','Ні'], index = 1, horizontal = True)
                    gs7 = st.radio("Строкатий розплід", options = ['Так', '-','Ні'], index = 1, horizontal = True)
                    gs8 = st.radio("Медовий наприск", options = ['Так', '-','Ні'], index = 1, horizontal = True)
                    gs9 = st.radio("Печатний мед", options = ['Так', '-','Ні'], index = 1, horizontal = True)
                    gs10 = st.radio("Перга", options = ['Так', '-','Ні'], index = 1, horizontal = True)

                with status_colony:
                    st.write("#### Дані про родину:")
                    
                    st.markdown("---")
                    sc1 = st.radio("Вид маточника", options = ['Ройовий', 'Свищевий', 'Тиха заміна', 'Штучний', 'Відсутні'], index = 4, horizontal = False)
                                            
                    st.markdown("---")
                    sc2 = st.radio("Стан родини", options = ['Спокійні', 'Менш спокійн', 'Менш нервові', 'Нервові', 'Більш нервові', 'Менш агресивін', 'Агресивні'], horizontal = False)

                    st.markdown("---")
                    sc3 = st.radio("Сила родини", options = ['Слабкі', 'Менш слабкі', 'Менше середнього', 'Середня', 'Більше середнього', 'Менш сильні', 'Сильні'], horizontal = False)

                    st.markdown("---")
                    sc4 = st.text_input("Чи хворія сім'я:", value="Хвороби відсутні")

                with queen_info:
                    st.write("#### Дані про матку:")
                    st.markdown("---")

                    qi1 = st.radio("Мічена матка", options = ['Так', '-','Ні'], index = 1, horizontal = True)
                    qi2 = st.date_input("Рік:")
                    qi3 = st.text_input("Шифр матки:")

                    st.markdown("---")
                    st.write("Дані про материнську матку:")

                    qi4 = st.number_input("Номер вулику:", min_value = 0, format = "%i", step = 1, value = n_hive)
                    qi5 = st.text_input("Тип маточнику:")
                    qi6 = st.date_input("Рік виведення:")
                    qi7 = st.text_input("Від матки:")

        # st.markdown("---")
        with st.expander('Рамки та медозбір'):

            with st.container():

                namber_of, honey = st.columns(2)
                with namber_of:
                    st.write("#### Кількість:")

                    no1 = st.number_input(f"Корпусів:", min_value = 0, format = "%i", step = 1)
                    no2 = st.number_input(f"Рамок:", min_value = 0, format = "%i", step = 1)
                    no3 = st.number_input(f"Рамок з медом:", min_value = 0, format = "%i", step = 1)
                    no4 = st.number_input(f"Рамок з розплодом:", min_value = 0, format = "%i", step = 1)
                    no5 = st.number_input(f"Рамок з пергою:", min_value = 0, format = "%i", step = 1)
                    no6 = st.number_input(f"Рамок з вощиною:", min_value = 0, format = "%i", step = 1)

                with honey:
                    st.write("#### Дані про медозбір:")

                    h1 = st.date_input("Дата медозбору:")
                    h2 = st.number_input(f"Відкачано рамок:", min_value = 0, format = "%i", step = 1)
                    h3 = st.number_input(f"Вага меду:", min_value = 0, format = "%d", step = 1)
                    h4 = st.text_input("Гатунок меду:")

        st.markdown("---")

        with st.container():
            st.write("#### Примітки:")
            com = st.text_area("Введіть додаткову інформацію:")


        
        submited = st.form_submit_button('Занести дані')
        if submited:
            d = {"Дата огляду" : [datetime64(date)], "Номер вулика" : [int(n_hive)], 
            "Матка" : [gs1], "Маточники" : [gs2], 
            "Яйця" : [gs3], "Відкритий розплід" : [gs4], 
            "Закритий розплід" : [gs5], "Трутовий розплід" : [gs6], 
            "Строкатий розплід" : [gs7], "Медовий наприск" : [gs8], 
            "Печатний мед" : [gs9], "Перга" : [gs10], 
            "Вид маточника" : [sc1], "Стан родини" : [sc2], 
            "Сила родини" : [sc3], "Чи хворія сім'я" : [sc4], 
            "Мічена матка" : [qi1], "Рік" : [datetime64(qi2)], 
            "Шифр матки" : [qi3], "Номер вулику" : [int(qi4)], 
            "Тип маточнику" : [qi5], "Рік виведення" : [datetime64(qi6)], 
            "Від матки" : [int(qi7)], "Корпусів" : [int(no1)], 
            "Рамок" : [int(no2)], "Рамок з медом" : [int(no3)], 
            "Рамок з розплодом" : [int(no4)], "Рамок з пергою" : [int(no5)], 
            "Рамок з вощиною" : [int(no6)], "Дата медозбору" : [datetime64(h1)], 
            "Відкачано рамок" : [int(h2)], "Вага меду" : [int(h3)], 
            "Гатунок меду" : [h4], "Примітки" :[com]} 
            column = ["Дата огляду", "Номер вулика", 
            "Матка", "Маточники", 
            "Яйця", "Відкритий розплід", 
            "Закритий розплід", "Трутовий розплід", 
            "Строкатий розплід", "Медовий наприск", 
            "Печатний мед", "Перга", 
            "Вид маточника", "Стан родини", 
            "Сила родини", "Чи хворія сім'я", 
            "Мічена матка", "Рік", 
            "Шифр матки", "Номер вулику", 
            "Тип маточнику", "Рік виведення", 
            "Від матки", "Корпусів", 
            "Рамок", "Рамок з медом", 
            "Рамок з розплодом", "Рамок з пергою", 
            "Рамок з вощиною", "Дата медозбору", 
            "Відкачано рамок", "Вага меду", 
            "Гатунок меду", "Примітки"] 
            df_report = pd.DataFrame(d)
            df = df.add(df_report)
            st.write(df)

