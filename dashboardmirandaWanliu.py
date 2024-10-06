# Untuk Run cd /Users/miranda/Downloads/a555-dashboard-main/, streamlit run dashboardmiranda.py , email m197B4KX2506@bangkit.academy

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np  # Import numpy

# Judul Dashboard
st.title('Dashboard Analisis Kualitas Udara Wanliu')

# Memuat dataset
uploaded_file = st.file_uploader("Pilih file CSV", type=['csv'])
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Menampilkan DataFrame
    st.subheader('Data Kualitas Udara')
    st.dataframe(df)  # Menggunakan st.dataframe untuk menampilkan data lebih baik

    # Menampilkan informasi dataset
    st.write("Dataset informasi:")
    st.write(df.describe())  # Menampilkan ringkasan statistik dari data

    # Visualisasi Histogram untuk PM2.5
    st.subheader('Distribusi PM2.5')
    plt.figure(figsize=(10, 5))
    sns.histplot(df['PM2.5'], bins=30, kde=True)
    plt.title('Distribusi PM2.5')
    st.pyplot(plt)

    # Visualisasi Histogram untuk PM10
    st.subheader('Distribusi PM10')
    plt.figure(figsize=(10, 5))
    sns.histplot(df['PM10'], bins=30, kde=True)
    plt.title('Distribusi PM10')
    st.pyplot(plt)

    # Matriks Korelasi
    st.subheader('Matriks Korelasi')
    plt.figure(figsize=(12, 8))

    # Mengambil hanya kolom numerik untuk matriks korelasi
    numeric_df = df.select_dtypes(include=['float64', 'int64'])

    # Hitung matriks korelasi
    correlation_matrix = numeric_df.corr()
    
    # Visualisasikan
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
    plt.title('Matriks Korelasi')
    st.pyplot(plt)

    # Insight
    st.subheader('Insight')

    # Pertanyaan 1
    st.write("**Pertanyaan 1**: Bagaimana perubahan suhu dan kecepatan angin memengaruhi tingkat PM2.5 di Wanliu?")
    st.write("- **Insight**: Dalam analisis ini, kami menemukan bahwa perubahan suhu dan kecepatan angin memiliki pengaruh yang signifikan terhadap tingkat PM2.5. Data menunjukkan bahwa saat suhu meningkat, tingkat PM2.5 juga cenderung meningkat. Hal ini dapat dihubungkan dengan peningkatan aktivitas manusia, seperti penggunaan kendaraan dan pembakaran bahan bakar, yang lebih sering terjadi pada hari-hari yang lebih hangat.")
    st.write("- Selain itu, kecepatan angin yang lebih tinggi dapat berfungsi sebagai faktor penentu dalam penyebaran polutan. Ketika kecepatan angin meningkat, polutan cenderung tersebar lebih merata, yang dapat mengurangi konsentrasi PM2.5 di beberapa lokasi. Namun, di area yang tidak terdampak angin, peningkatan polusi dapat terjadi, terutama ketika aktivitas industri meningkat.")

    # Pertanyaan 2
    st.write("**Pertanyaan 2**: Apakah kualitas udara (PM2.5 dan PM10) di Wanliu memburuk pada bulan-bulan tertentu dalam setahun?")
    st.write("- **Insight**: Analisis data bulanan menunjukkan bahwa kualitas udara, terutama konsentrasi PM2.5 dan PM10, cenderung memburuk selama bulan-bulan musim dingin. Hal ini bisa disebabkan oleh beberapa faktor, termasuk penggunaan pemanas yang lebih tinggi di rumah dan emisi dari kendaraan yang terperangkap dalam kondisi cuaca dingin dan tenang. Akibatnya, polutan dapat terakumulasi di atmosfer tanpa ada cukup aliran udara untuk membubarkannya.")
    st.write("- Penelitian ini menunjukkan bahwa tindakan pengendalian polusi yang lebih efektif perlu diimplementasikan selama periode-periode ini, seperti pembatasan aktivitas industri atau penggunaan bahan bakar yang lebih bersih. Selain itu, edukasi masyarakat tentang dampak polusi selama musim dingin juga dapat membantu mengurangi emisi yang tidak perlu.")

    # Rangkuman
    st.write("Melalui analisis ini, kami dapat memahami bagaimana faktor lingkungan seperti suhu dan kecepatan angin berinteraksi dengan tingkat polusi di Wanliu. Hasil ini bisa menjadi dasar untuk kebijakan pengendalian polusi yang lebih baik dan program kesadaran masyarakat tentang pentingnya menjaga kualitas udara.")   


else:
    st.write("Silakan unggah file CSV untuk memulai.")
