from unicodedata import name
import os
import streamlit as st 
from PIL import Image
from pathlib import Path
from PyPDF2 import PdfFileMerger, PdfFileReader
from streamlit_option_menu import option_menu



st.sidebar.write(f"#### Вкажіть шлях до файлів!")   

st.sidebar.markdown("---")

open_pdf = st.sidebar.text_input("Вкажіть шлях до pdf файлів:", key = 'open_pdf')
name_pdf = st.sidebar.text_input("Вкажіть ім'я pdf файлу:", key = 'name_pdf')

save_pdf_button = st.sidebar.button("Зберегти PDF")
# st.sidebar.info(path_open)
st.sidebar.markdown("---")

if save_pdf_button:    
    # try:
        pdfs = []

        for file in os.listdir(open_pdf):
            if file.endswith('.pdf'):
                pdfs.append(file)
        st.info(pdfs)
        merger = PdfFileMerger()
        for pdf in pdfs:
            merger.append(pdf)
        merger.write(name_pdf +'.pdf')
        merger.close()
        st.info("J.dsdsdsd")
    # except:
    #     st.info("Вкажіть шлях до pdf файлів")




