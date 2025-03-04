import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# Helper function yang dibutuhkan untuk menyiapkan berbagai dataframe

def create_daily_rentals_df(df):
    daily_rentals_df = df.resample(rule='D', on='dteday').agg({
        "cnt": "sum"
    })
    daily_rentals_df = daily_rentals_df.reset_index()
    daily_rentals_df.rename(columns={
        "cnt": "rental_count"
    }, inplace=True)
    return daily_rentals_df

def create_hourly_rentals_df(df):
    hourly_rentals = df.groupby('hr')['cnt'].sum().reset_index()
    return hourly_rentals

def create_weekday_rentals_df(df):
    weekday_rentals = df.groupby('weekday')['cnt'].sum().reset_index()
    return weekday_rentals

def create_seasonal_rentals_df(df):
    seasonal_rentals = df.groupby('season')['cnt'].sum().reset_index()
    return seasonal_rentals

def create_weather_rentals_df(df):
    weather_rentals = df.groupby('weathersit')['cnt'].sum().reset_index()
    return weather_rentals

def create_monthly_user_rentals_df(df):
    monthly_user_rentals = df.groupby('mnth')[['casual', 'registered']].sum().reset_index()
    return monthly_user_rentals

def create_yearly_rentals_df(df):
    yearly_rentals = df.groupby('yr')['cnt'].sum().reset_index()
    return yearly_rentals

# Load cleaned data
hour_df = pd.read_csv("hour_cleaned.csv")
day_df = pd.read_csv("day_cleaned.csv")

# Konversi kolom 'dteday' ke datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Filter data
min_date = day_df["dteday"].min()
max_date = day_df["dteday"].max()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://img.freepik.com/free-vector/professional-bikes-with-flat-design_23-2147681639.jpg?t=st=1741038743~exp=1741042343~hmac=6a4bd400302948fd5dac8d8259012cfef7288d6caa4f3362d604cb5f6f785399&w=1060")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu', min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = day_df[(day_df["dteday"] >= pd.to_datetime(start_date)) & 
                 (day_df["dteday"] <= pd.to_datetime(end_date))]

# Menyiapkan berbagai dataframe
daily_rentals_df = create_daily_rentals_df(main_df)
hourly_rentals_df = create_hourly_rentals_df(hour_df)
weekday_rentals_df = create_weekday_rentals_df(main_df)
seasonal_rentals_df = create_seasonal_rentals_df(main_df)
weather_rentals_df = create_weather_rentals_df(main_df)
monthly_user_rentals_df = create_monthly_user_rentals_df(main_df)
yearly_rentals_df = create_yearly_rentals_df(main_df)

# Agregasi data per bulan
monthly_rentals = day_df.groupby('mnth')['cnt'].sum()

# Dashboard
st.header('Bike Sharing Dashboard :sparkles:')

# Daily Rentals
st.subheader('Daily Rentals')

col1, col2 = st.columns(2)

with col1:
    total_rentals = daily_rentals_df.rental_count.sum()
    st.metric("Total Rentals", value=total_rentals)

with col2:
    avg_rentals = daily_rentals_df.rental_count.mean()
    st.metric("Average Rentals per Day", value=round(avg_rentals, 2))

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    daily_rentals_df["dteday"],
    daily_rentals_df["rental_count"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
ax.set_title("Daily Rentals Over Time", fontsize=25)
ax.set_xlabel("Date", fontsize=20)
ax.set_ylabel("Number of Rentals", fontsize=20)

st.pyplot(fig)

# Performa Penyewaan Sepeda dalam Beberapa Bulan Terakhir
st.subheader('Performa Penyewaan Sepeda dalam Beberapa Bulan Terakhir')

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x=monthly_rentals.index, y=monthly_rentals.values, marker='o', linewidth=2, color="#90CAF9")
plt.title('Tren Penyewaan Sepeda per Bulan (2011-2012)', fontsize=20)
plt.xlabel('Bulan', fontsize=15)
plt.ylabel('Total Penyewaan Sepeda', fontsize=15)
plt.xticks(range(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid(True)
st.pyplot(fig)

# Penyewaan Sepeda per Jam dan Penyewaan Sepeda per Hari dalam Seminggu
st.subheader('Penyewaan Sepeda per Jam dan Penyewaan Sepeda per Hari dalam Seminggu')

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Penyewaan Sepeda per Jam**")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x=hourly_rentals_df["hr"], y=hourly_rentals_df["cnt"], marker='o', linewidth=2, color="#90CAF9")
    plt.title('Penyewaan Sepeda per Jam', fontsize=20)
    plt.xlabel('Jam dalam Sehari', fontsize=15)
    plt.ylabel('Total Penyewaan Sepeda', fontsize=15)
    plt.xticks(range(0, 24))
    plt.grid(True)
    st.pyplot(fig)

with col2:
    st.markdown("**Penyewaan Sepeda per Hari dalam Seminggu**")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=weekday_rentals_df["weekday"], y=weekday_rentals_df["cnt"], palette='viridis')
    plt.title('Penyewaan Sepeda per Hari dalam Seminggu', fontsize=20)
    plt.xlabel('Hari dalam Seminggu', fontsize=15)
    plt.ylabel('Total Penyewaan Sepeda', fontsize=15)
    plt.xticks(ticks=range(7), labels=['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu'])
    st.pyplot(fig)

# Pengaruh Musim terhadap Penyewaan Sepeda
st.subheader('Pengaruh Musim terhadap Penyewaan Sepeda')

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=seasonal_rentals_df["season"], y=seasonal_rentals_df["cnt"], palette='viridis')
plt.title('Pengaruh Musim terhadap Penyewaan Sepeda', fontsize=20)
plt.xlabel('Musim', fontsize=15)
plt.ylabel('Total Penyewaan Sepeda', fontsize=15)
plt.xticks(ticks=[0, 1, 2, 3], labels=['Dingin', 'Semi', 'Panas', 'Gugur'])
st.pyplot(fig)

# Pengaruh Cuaca terhadap Penyewaan Sepeda
st.subheader('Pengaruh Cuaca terhadap Penyewaan Sepeda')

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=weather_rentals_df["weathersit"], y=weather_rentals_df["cnt"], palette='viridis')
plt.title('Pengaruh Cuaca terhadap Penyewaan Sepeda', fontsize=20)
plt.xlabel('Kondisi Cuaca', fontsize=15)
plt.ylabel('Total Penyewaan Sepeda', fontsize=15)
plt.xticks(ticks=[0, 1, 2, 3], labels=['Cerah', 'Mendung', 'Hujan Ringan', 'Hujan Lebat'])
st.pyplot(fig)

# Tren Penyewaan Sepeda per Bulan untuk Pengguna Casual dan Terdaftar
st.subheader('Tren Penyewaan Sepeda per Bulan (Casual vs Registered)')

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x=monthly_user_rentals_df["mnth"], y=monthly_user_rentals_df["casual"], label='Casual', marker='o', linewidth=2, color="#90CAF9")
sns.lineplot(x=monthly_user_rentals_df["mnth"], y=monthly_user_rentals_df["registered"], label='Registered', marker='o', linewidth=2, color="#FFA500")
plt.title('Tren Penyewaan Sepeda per Bulan (Casual vs Registered)', fontsize=20)
plt.xlabel('Bulan', fontsize=15)
plt.ylabel('Total Penyewaan Sepeda', fontsize=15)
plt.xticks(range(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.legend()
plt.grid(True)
st.pyplot(fig)

# Perbandingan Penyewaan Sepeda antara Tahun 2011 dan 2012
st.subheader('Perbandingan Penyewaan Sepeda antara Tahun 2011 dan 2012')

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=yearly_rentals_df["yr"], y=yearly_rentals_df["cnt"], palette='viridis')
plt.title('Perbandingan Penyewaan Sepeda antara Tahun 2011 dan 2012', fontsize=20)
plt.xlabel('Tahun', fontsize=15)
plt.ylabel('Total Penyewaan Sepeda', fontsize=15)
plt.xticks(ticks=[0, 1], labels=['2011', '2012'])
st.pyplot(fig)

st.caption('Copyright © Bagas Cahyawiguna 2025')