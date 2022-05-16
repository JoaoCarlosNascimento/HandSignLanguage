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

# Database Para Livros
Titulo_Livro = pd.DataFrame(Dataframe1, columns=['Livro'])
Página = pd.DataFrame(Dataframe1, columns=['Página'])
Texto_EN = pd.DataFrame(Dataframe1, columns=['Texto_EN'])
Texto_PT = pd.DataFrame(Dataframe1, columns=['Texto_PT'])
Imagem = pd.DataFrame(Dataframe1, columns=['Imagem'])

# Database Para Tradução de EN para PT
Palavras_EN = pd.DataFrame(Dataframe2, columns=['Palavras_EN'])
Palavras_PT = pd.DataFrame(Dataframe2, columns=['Palavras_PT'])

# https://stackoverflow.com/questions/19472922/reading-external-sql-script-in-python

with open('db/createdb.sql', 'r') as sql_file:
    for index, row in Dataframe1.iterrows():
        c.execute("INSERT INTO BOOK(TITLE, IMG) values(?,?)",
                  (row.Livro, row.Imagem))
        c.execute("INSERT INTO PAGES(NUM, IMG, BOOK) values(?,?,?)",
                  (row.Página, row.Imagem, row.Livro))
        c.execute("INSERT INTO PAGE_CONTENTS(PT, EN, PAGEID) values(?,?,?)",
                  (row.Texto_EN, row.Texto_PT, row.Página))
        conn.commit()

    for index, row in Dataframe2.iterrows():
        video_name = row.Palavras_EN.replace('"', '')
        string_video = vids_path + video_name + '.mp4'
        c.execute("INSERT INTO WORDS(WORD_EN,WORD_PT,FIG_PATH) values(?,?,?)",
                  (row.Palavras_EN, row.Palavras_PT, string_video))
        conn.commit()

conn.close()
