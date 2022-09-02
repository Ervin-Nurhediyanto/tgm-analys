import pandas as pd

lab_df = pd.read_excel('static\\data\\TGM_Indo_2021.xlsx', sheet_name='LABEL_TGM')

kp = lab_df['Kategori Penilaian']
