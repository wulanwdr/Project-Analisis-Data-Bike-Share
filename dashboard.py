import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Data analisis rata-rata jumlah pengguna berdasarkan musim
def analyze_season_data():
    # Membaca dataset
    day_df = pd.read_csv("analysis_result.csv")

    # Mapping label musim
    season_labels = {1: "Semi", 2: "Panas", 3: "Gugur", 4: "Winter"}
    day_df["season_label"] = day_df["season"].map(season_labels)

    # Analisis musim
    season_analysis = day_df.groupby("season_label")["cnt"].agg(["mean", "sum", "count"]).reset_index()
    season_analysis = season_analysis.sort_values(by="mean", ascending=False)

    return season_analysis

# Analisis penyewaan sepeda terhadap cuaca
def analyze_weathersit_data():
    day_df = pd.read_csv("analysis_result.csv")
    
    # Mapping label cuaca
    weather_labels = {
        1: "Cerah/Berawan",
        2: "Mendung/Mendung Tipis/Berkabut",
        3: "Hujan Ringan/Salju",
        4: "Hujan Lebat/Salju Lebat"
    }
    day_df["weathersit_label"] = day_df["weathersit"].map(weather_labels)

    # Analisis Data
    weather_analysis = day_df.groupby("weathersit_label")["cnt"].sum().sort_values(ascending=False).reset_index()

    return weather_analysis

# Analisis penyewaan sepeda pada hari kerja (workingday)
def analyze_workingday_data():
    day_df = pd.read_csv("analysis_result.csv")

    # Analisis hari kerja
    workingday_analysis = day_df.groupby("workingday")["cnt"].agg(["mean", "sum", "count"]).reset_index()

    # Menambahkan label interpretasi
    workingday_labels = {0: "Non-Working Day", 1: "Working Day"}
    workingday_analysis["workingday_label"] = workingday_analysis["workingday"].map(workingday_labels)

    return workingday_analysis

# Fungsi untuk membuat visualisasi rata-rata pada setiap musim
def create_season_visualization(data):
    plt.figure(figsize=(8, 5))
    sns.barplot(x="season_label", y="mean", data=data, palette="coolwarm")
    plt.title("Rata-rata Jumlah Pengguna Sepeda Berdasarkan Musim", fontsize=14)
    plt.xlabel("Musim", fontsize=12)
    plt.ylabel("Rata-rata Jumlah Pengguna Sepeda", fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    st.pyplot(plt)  

# Fungsi untuk membuat visualisasi cuaca
def create_weathersit_visualization(data):
    plt.figure(figsize=(8, 5))
    sns.barplot(x="cnt", y="weathersit_label", data=data, palette="Blues_d")
    plt.title("Penyewaan Sepeda di Setiap Cuaca", fontsize=14)
    plt.xlabel("Total Penyewaan Sepeda", fontsize=12)
    plt.ylabel("Kondisi Cuaca", fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    st.pyplot(plt)

# Fungsi untuk membuat visualisasi hari kerja
def create_workingday_visualization(data):
    plt.figure(figsize=(8, 5))
    plt.bar(data["workingday_label"], data["mean"], color=["#FF6347", "#32CD32"])
    plt.title("Rata-rata Jumlah Penyewaan Sepeda pada Non-Hari Kerja vs Hari Kerja", fontsize=14)
    plt.xlabel("Jenis Hari", fontsize=12)
    plt.ylabel("Rata-rata Penyewaan Sepeda", fontsize=12)
    st.pyplot(plt)

# Streamlit app layout
st.title("Dashboard Analisis Penyewaan Sepeda")

st.subheader("Analisis Penyewaan Sepeda Berdasarkan Musim")
season_data = analyze_season_data()
create_season_visualization(season_data)

st.subheader("Analisis Penyewaan Sepeda Berdasarkan Cuaca")
weathersit_data = analyze_weathersit_data()
create_weathersit_visualization(weathersit_data)

st.subheader("Analisis Penyewaan Sepeda Berdasarkan Hari Kerja")
workingday_data = analyze_workingday_data()
create_workingday_visualization(workingday_data)
