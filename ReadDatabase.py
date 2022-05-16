import pandas as pd  # pip install pandas
import sqlite3
from sqlite3 import OperationalError
import numpy as np
from db import *

# pip install openpyxl

conn = sqlite3.connect('db/books.db')
c = conn.cursor()

excel_path = 'Database/Database.xlsx'
vids_path = 'WordsVids/Vids/'
# Folha1/Folha2: Excel em Português / Sheet1/Sheet2: Excel em Inglês
Dataframe1 = pd.read_excel(excel_path, 'Folha1')
Dataframe2 = pd.read_excel(excel_path, 'Folha2')

# https://stackoverflow.com/questions/19472922/reading-external-sql-script-in-python

with open('db/createdb.sql', 'r') as sql_file:
    for index, row in Dataframe1.iterrows():
        c.execute("INSERT INTO BOOK(TITLE, IMG) values(?,?)",
                  (str(Dataframe1.Livro[index]), str(Dataframe1.Imagem[index])))
        c.execute("INSERT INTO PAGES(NUM, IMG, BOOK) values(?,?,?)",
                  (Dataframe1.Página[index], Dataframe1.Imagem[index], Dataframe1.Livro[index]))
        c.execute("INSERT INTO PAGE_CONTENTS(PT, EN, PAGEID) values(?,?,?)",
                  (Dataframe1.Texto_EN[index], Dataframe1.Texto_PT[index], Dataframe1.Página[index]))
        conn.commit()

    for index, row in Dataframe2.iterrows():
        video_name = Dataframe2.Palavras_EN[index].replace('"', '')
        string_video = vids_path + video_name + '.mp4'
        c.execute("INSERT INTO WORDS(WORD_EN,WORD_PT,FIG_PATH) values(?,?,?)",
                  (Dataframe2.Palavras_EN[index], Dataframe2.Palavras_PT[index], string_video))
        conn.commit()

conn.close()
