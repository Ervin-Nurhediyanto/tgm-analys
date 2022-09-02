from flask import Flask, render_template, url_for, request
from src.data.main import *

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('home.html', len = len(df.index), prov = prov, fm = fm, jb = jb, dm = dm, fai = fai, dai = dai)

@app.route('/home')
def home():
  return render_template('home.html', len = len(df.index), prov = prov, fm = fm, jb = jb, dm = dm, fai = fai, dai = dai)

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/analysis')
def analysis():
  arr_analys = []
  for i in range(len(int_df.index)):
    arr_analys.append('Frekuensi Membaca')
  df = pd.DataFrame({
    'Analysis': arr_analys,
    'Frekuensi/Minggu': int_fm,
    'Prov': prov
    })
  fig = px.bar(df, x='Analysis', y='Frekuensi/Minggu', color='Prov', barmode='group')
  graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
  return render_template('analysis.html', graphJSON=graphJSON)

# Tingkat Kegemaran Membaca
@app.route('/analysis_tgm')
def analysis_tgm():
  arr_analys = []
  for i in range(len(int_df.index)):
    arr_analys.append('Tingkat Kegemaran Membaca')
  df = pd.DataFrame({
    'Analysis': arr_analys,
    'Score': int_tgm,
    'Prov': prov
    })
  fig = px.bar(df, x='Analysis', y='Score', color='Prov', barmode='group')
  graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
  return render_template('analysis.html', graphJSON=graphJSON)

# Frekuensi Membaca
@app.route('/analysis_fm')
def analysis_fm():
  arr_analys = []
  for i in range(len(int_df.index)):
    arr_analys.append('Frekuensi Membaca')
  df = pd.DataFrame({
    'Analysis': arr_analys,
    'Frekuensi/Minggu': int_fm,
    'Prov': prov
    })
  fig = px.bar(df, x='Analysis', y='Frekuensi/Minggu', color='Prov', barmode='group')
  graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
  return render_template('analysis.html', graphJSON=graphJSON)

# Jumlah Bahan Bacaan
@app.route('/analysis_jb')
def analysis_jb():
  arr_analys = []
  for i in range(len(int_df.index)):
    arr_analys.append('Jumlah Bahan Bacaan')
  df = pd.DataFrame({
    'Analysis': arr_analys,
    'Buku/Triwulan': int_jb,
    'Prov': prov
    })
  fig = px.bar(df, x='Analysis', y='Buku/Triwulan', color='Prov', barmode='group')
  graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
  return render_template('analysis.html', graphJSON=graphJSON)

# Durasi Membaca
@app.route('/analysis_dm')
def analysis_dm():
  arr_analys = []
  for i in range(len(int_df.index)):
    arr_analys.append('Durasi Membaca')
  df = pd.DataFrame({
    'Analysis': arr_analys,
    'Menit/Hari': int_dm,
    'Prov': prov
    })
  fig = px.bar(df, x='Analysis', y='Menit/Hari', color='Prov', barmode='group')
  graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
  return render_template('analysis.html', graphJSON=graphJSON)

# Frekuensi Akses Internet
@app.route('/analysis_fai')
def analysis_fai():
  arr_analys = []
  for i in range(len(int_df.index)):
    arr_analys.append('Frekuensi Akses Internet')
  df = pd.DataFrame({
    'Analysis': arr_analys,
    'Frekuensi/Minggu': int_fai,
    'Prov': prov
    })
  fig = px.bar(df, x='Analysis', y='Frekuensi/Minggu', color='Prov', barmode='group')
  graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
  return render_template('analysis.html', graphJSON=graphJSON)

# Durasi Akses Internet
@app.route('/analysis_dai')
def analysis_dai():
  arr_analys = []
  for i in range(len(int_df.index)):
    arr_analys.append('Durasi Akses Internet')
  df = pd.DataFrame({
    'Analysis': arr_analys,
    'Menit/Hari': int_dai,
    'Prov': prov
    })
  fig = px.bar(df, x='Analysis', y='Menit/Hari', color='Prov', barmode='group')
  graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
  return render_template('analysis.html', graphJSON=graphJSON)

# Korelasi
@app.route('/analysis_correlation')
def analysis_correlation():
  def df_to_plotly(int_df):
    return {'z': int_df.values.tolist(),
            'x': int_df.columns.tolist(),
            'y': int_df.index.tolist() }
  dfNew = int_df.corr()
  fig = go.Figure(data=go.Heatmap(df_to_plotly(dfNew)))
  graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
  return render_template('analysis.html', graphJSON=graphJSON)

@app.route('/results')
def output():
  round_tgm = []
  for i in range(len(int_df.index)):
    round_tgm.append(round(int_df['Tingkat Gemar Membaca'][i], 2))
  return render_template('results.html', len = len(df.index), prov = prov, tgm = round_tgm, kp = kp)

if __name__ == '__main__':
  app.run(debug=True)
