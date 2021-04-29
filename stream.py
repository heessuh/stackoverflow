import pandas as pd
import streamlit as st
from scrape import getQuestions, questionlist

st.title("Stackoverflow Scraper")
tag = st.text_input('Enter your search tag')

if tag != '':
    try:
        question = getQuestions(tag)

    except:
        st.subheader("Enter tag again")

df = pd.DataFrame(questionlist)
df.to_csv('stackquestions.csv', index=False)
print('Fin.')

