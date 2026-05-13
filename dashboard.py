import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Covid-19 Dashboard",
    page_icon="🌍",
    layout="wide"
)

# ---------------- TITLE ----------------
st.title("🌍 Covid-19 Analytics Dashboard")
st.markdown("### Real-Time Style Covid-19 Data Analysis Website")

# ---------------- LOAD DATA ----------------
df = pd.read_csv(
    r"C:\Users\anamg\OneDrive\Desktop\HexSoftwares_Covid19_Project\covid.csv"
)

# ---------------- WORLD STATS ----------------
world_confirmed = df["Confirmed"].max()
world_deaths = df["Deaths"].max()
world_recovered = df["Recovered"].max()

st.subheader("🌍 Worldwide Covid-19 Statistics")

w1, w2, w3 = st.columns(3)

w1.metric("🌡 Total Confirmed", f"{world_confirmed:,}")
w2.metric("☠ Total Deaths", f"{world_deaths:,}")
w3.metric("💚 Total Recovered", f"{world_recovered:,}")

# ---------------- SIDEBAR ----------------
st.sidebar.title("🌍 Covid Dashboard")
st.sidebar.markdown("---")
st.sidebar.write("Select any country to view Covid-19 analysis.")

country_list = df["Country/Region"].unique()

selected_country = st.sidebar.selectbox(
    "🌎 Select Country",
    country_list
)

# ---------------- FILTER DATA ----------------
country_data = df[df["Country/Region"] == selected_country]

latest_data = country_data.iloc[-1]

confirmed = latest_data["Confirmed"]
deaths = latest_data["Deaths"]
recovered = latest_data["Recovered"]
active = confirmed - deaths - recovered

# ---------------- METRIC CARDS ----------------
st.subheader(f"📊 Covid-19 Statistics for {selected_country}")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Confirmed Cases", f"{confirmed:,}")
col2.metric("Deaths", f"{deaths:,}")
col3.metric("Recovered", f"{recovered:,}")
col4.metric("Active Cases", f"{active:,}")

# ---------------- DATASET PREVIEW ----------------
st.subheader("📄 Latest Dataset Records")
st.dataframe(country_data.tail(10))

# ---------------- LINE CHART ----------------
st.subheader("📈 Confirmed Cases Trend")

trend_data = country_data.groupby("Date")["Confirmed"].max()

# Reduce dates for cleaner graph
trend_data = trend_data.iloc[::15]

fig1, ax1 = plt.subplots(figsize=(12,5))

ax1.plot(
    trend_data.index,
    trend_data.values,
    marker='o'
)

ax1.set_title(f"Covid-19 Trend in {selected_country}")

ax1.set_xlabel("Date")
ax1.set_ylabel("Confirmed Cases")

# Rotate labels
plt.xticks(rotation=45)

# Grid for clean look
ax1.grid(True)

plt.tight_layout()

st.pyplot(fig1)

# ---------------- PIE CHART ----------------
st.subheader("🥧 Cases Distribution")

labels = ["Recovered", "Deaths", "Active"]

sizes = [recovered, deaths, active]

fig2, ax2 = plt.subplots(figsize=(6,6))

ax2.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%'
)

ax2.set_title("Covid-19 Case Distribution")

st.pyplot(fig2)

# ---------------- TOP 10 COUNTRIES ----------------
st.subheader("🏆 Top 10 Countries by Confirmed Cases")

top10 = (
    df.groupby("Country/Region")["Confirmed"]
    .max()
    .sort_values(ascending=False)
    .head(10)
)

fig3, ax3 = plt.subplots(figsize=(12,6))

ax3.bar(top10.index, top10.values)

ax3.set_title("Top 10 Countries")
ax3.set_xlabel("Country")
ax3.set_ylabel("Confirmed Cases")

plt.xticks(rotation=45)

plt.tight_layout()

st.pyplot(fig3)

# ---------------- FOOTER ----------------
st.markdown("---")

st.success("✅ Covid-19 Analytics Dashboard Successfully Running")

st.markdown(
    """
    ### 👨‍💻 Developed By
    Gurya | Data Science & Python Project
    
    🚀 Internship Project - Hex Softwares
    """
)