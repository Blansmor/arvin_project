import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

st.title("Dashboard Sederhana AQI")

aqi_df = pd.read_csv("dataset_bersih.csv")

col1, col2= st.columns(2)

with col1:
    st.header("Pertanyaan 1")

    # Membuat pivot table dengan parameter year untuk mencari mean PM2.5 tertinggi
    aqi_pertanyaan1 = aqi_df.groupby(by=aqi_df['year']).agg({
        'PM2.5': 'mean'
    })

    #Melakukan reset index agar kolom month dapat di visualisasi
    aqi_pertanyaan1.reset_index(inplace=True)

    # Membuat visualisasi grafik rata-rata PM2.5 dari tahun ke tahun
    plt.plot(aqi_pertanyaan1['year'],aqi_pertanyaan1['PM2.5'])
    plt.xlabel('Year')
    plt.ylabel('Rata-rata PM2.5')

    st.pyplot()

with col2:
    st.header("Pertanyaan 2")

    # Membuat pivot table dengan parameter year untuk mencari O3 tertinggi
    aqi_pertanyaan2 = aqi_df.groupby(by=aqi_df['year']).agg({
    'O3': 'max'
    })

    #Melakukan reset index agar kolom month dapat di visualisasi
    aqi_pertanyaan2.reset_index(inplace=True)

    # Membuat visualisasi grafik nilai tertinggi O3 dari tahun ke tahun
    plt.plot(aqi_pertanyaan2['year'],aqi_pertanyaan2['O3'])
    plt.xlabel('Year')
    plt.ylabel('O3 tertinggi')

    st.pyplot()