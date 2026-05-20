
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard Penjualan",
    layout="wide"
)

st.title("Dashboard Penjualan Sederhana")
st.write("Dashboard ini dibuat menggunakan Python dan Streamlit.")

df = pd.read_csv("data.csv")

st.subheader("Preview Data")
st.dataframe(df)

kategori = st.selectbox(
    "Pilih kategori:",
    df["kategori"].unique()
)

df_filter = df[df["kategori"] == kategori]

st.subheader("Tren Penjualan")
fig_line = px.line(
    df_filter,
    x="bulan",
    y="penjualan",
    markers=True,
    title=f"Tren Penjualan Kategori {kategori}"
)
st.plotly_chart(fig_line, use_container_width=True)

st.subheader("Perbandingan Penjualan per Kategori")
fig_bar = px.bar(
    df,
    x="kategori",
    y="penjualan",
    color="kategori",
    title="Perbandingan Penjualan per Kategori"
)
st.plotly_chart(fig_bar, use_container_width=True)
