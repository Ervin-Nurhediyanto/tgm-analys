import pandas as pd

df = pd.read_excel('static\\data\\TGM_Indo_2021.xlsx', sheet_name='DATA_TGM')

round_dm = []
for i in range(len(df.index)):
  round_dm.append(round(df['Durasi Membaca'][i], 2))

round_dai = []
for i in range(len(df.index)):
  round_dai.append(round(df['Durasi Akses Internet'][i], 2))

prov = df['Provinsi']
fm = df['Frekuensi Membaca']
jb = df['Jumlah Bahan Bacaan']
dm = round_dm
fai = df['Frekuensi Akses Internet']
dai = round_dai
