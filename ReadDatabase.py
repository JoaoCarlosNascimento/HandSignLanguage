import pandas as pd # pip install pandas
import sqlite3
import numpy as np
from db import *
excel_path = 'Database/Database.xlsx'
# pip install openpyxl
# Folha1/Folha2: Excel em Português / Sheet1/Sheet2: Excel em Inglês
Dataframe1 = pd.read_excel(excel_path, 'Folha1')
Dataframe2 = pd.read_excel(excel_path, 'Folha2')

# Database Para Livros
Titulo_Livro = pd.DataFrame(Dataframe1, columns= ['Livro'])
Página = pd.DataFrame(Dataframe1, columns= ['Página'])
Texto_EN = pd.DataFrame(Dataframe1, columns= ['Texto_EN'])
Texto_PT = pd.DataFrame(Dataframe1, columns= ['Texto_PT'])
Imagem = pd.DataFrame(Dataframe1, columns= ['Imagem'])

# Database Para Tradução de EN para PT
Palavras_EN = pd.DataFrame(Dataframe2, columns= ['Palavras_EN'])
Palavras_PT = pd.DataFrame(Dataframe2, columns= ['Palavras_PT'])
'''
INSERT INTO BOOK(TITLE, IMG)
VALUES(Titulo_Livro, Imagem)
'''