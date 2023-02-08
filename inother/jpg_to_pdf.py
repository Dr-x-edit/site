from unicodedata import name
import os
import streamlit as st 
from PIL import Image


st.sidebar.write(f"#### Вкажіть шлях до файлів!")   

st.sidebar.markdown("---")

path_open = st.sidebar.text_input("Вкажіть шлях до файлів:", key = 'open')
path_save = st.sidebar.text_input("Вкажіть шлях до файлів:", key = 'save')

st.sidebar.markdown("---")

save_button = st.sidebar.button("Зберегти")
# st.sidebar.info(path_open)
try:
    items = os.listdir(str(path_open))
    st.dataframe(items)

except:
    st.info("Вкажіть шлях до файлів")


if save_button:
    for item in items:
        image1 = Image.open(str(path_open) + "\\" + item)
        file1 = image1.convert('RGB')
        i_s = item.split('.jpeg')[0]
        file1.save(path_save + '\\' + i_s + '.pdf')
    st.info("Файли сконвертовано успішно!")

    new_item = os.listdir(str(path_save))
    st.dataframe(new_item)