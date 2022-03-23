import pandas as pd
import numpy as np

imiona = pd.read_excel('files_sources\Imiona_nadane_wPolsce_w_latach_2000-2019.xlsx')

imiona.info(memory_usage='deep')

imiona.columns = ['rok', 'imie', 'liczba', 'plec']
imiona.columns
imiona.imie = imiona.imie.astype('category')
imiona.plec = imiona.plec.astype('category')
imiona.rok = imiona.rok.astype('int16')
imiona.liczba = imiona.liczba.astype('int64')

imiona.rok.value_counts()
imiona.liczba.value_counts()

il = imiona[(imiona.plec == 'M')][['imie','liczba']]
il
gr = il.groupby('imie')
out = gr.sum()[gr.sum().liczba > 10].sort_values('liczba', ascending=False)

out.to_clipboard()