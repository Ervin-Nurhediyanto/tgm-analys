import pandas as pd

int_df = pd.read_excel('static\\data\\TGM_Indo_2021.xlsx', sheet_name='INT_TGM')

int_fm = int_df['Frekuensi Membaca']
int_jb = int_df['Jumlah Bahan Bacaan']
int_dm = int_df['Durasi Membaca']
int_fai = int_df['Frekuensi Akses Internet']
int_dai = int_df['Durasi Akses Internet']
int_tgm = int_df['Tingkat Gemar Membaca']
