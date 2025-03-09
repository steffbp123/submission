import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Data
file_path = "/mnt/data/all_data.csv"
df = pd.read_csv(file_path)

# Pisahkan Data Harian dan Jam
hari_list = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
df_harian = df[df["Kategori"].isin(hari_list)]
df_harian.set_index("Kategori", inplace=True)

df_jam = df[df["Kategori"].str.contains("Jam")]
df_jam["Jam"] = df_jam["Kategori"].str.extract("(\\d+)").astype(int)
df_jam.set_index("Jam", inplace=True)

# Streamlit Dashboard
st.title("Dashboard Pengguna Kasual")

# Pie Chart
st.subheader("Distribusi Pengguna Kasual per Hari")
fig1, ax1 = plt.subplots()
ax1.pie(df_harian["Jumlah Casual Users"], labels=df_harian.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
ax1.set_title("Distribusi Pengguna Kasual Berdasarkan Hari")
st.pyplot(fig1)

# Bar Chart
st.subheader("Jumlah Pengguna Kasual per Jam")
fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.bar(df_jam.index, df_jam["Jumlah Casual Users"], color='lightcoral')
ax2.set_xlabel("Jam")
ax2.set_ylabel("Jumlah Pengguna Kasual")
ax2.set_title("Jumlah Pengguna Kasual Berdasarkan Jam dalam Sehari")
ax2.set_xticks(range(0, 24))
ax2.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig2)

st.write("Sumber data: all_data.csv")
