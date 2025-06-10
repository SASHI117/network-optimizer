import streamlit as st
import pandas as pd
from utils.api_fetchers import get_cell_towers, get_weather

def show():
    st.title("📡 Network Health & Weather Impact")
    st.write("Analyze network signals and check weather conditions that impact connectivity.")

    # 📍 **Why Latitude & Longitude?**  
    st.markdown("""
    **Latitude & Longitude** are used to determine the exact geographical location.  
    - **Latitude**: Measures how far north or south you are from the equator.  
    - **Longitude**: Measures how far east or west you are from the Prime Meridian.  
    - **Why is it important?**  
      - Network signals depend on tower locations in your area.  
      - Weather conditions affect signal strength and connectivity.  
      - Helps in fetching precise **network & weather data** based on your location.  
    """)

    # Sidebar for API Keys
    st.sidebar.header("🔑 API Keys")
    OPENCELLID_KEY = st.sidebar.text_input("OpenCelliD Key", type="password")
    WEATHER_KEY = st.sidebar.text_input("OpenWeatherMap Key", type="password")

    # User Inputs
    lat = st.number_input("Latitude", value=28.7041)
    lon = st.number_input("Longitude", value=77.1025)

    if st.button("🔍 Analyze Data"):
        if not OPENCELLID_KEY or not WEATHER_KEY:
            st.error("⚠️ Please enter both API keys to proceed!")
        else:
            with st.spinner("Fetching real-time data..."):
                towers = get_cell_towers(OPENCELLID_KEY, lat, lon)
                weather = get_weather(WEATHER_KEY, lat, lon)

                if towers and weather:
                    df_towers = pd.DataFrame(towers)
                    df_weather = pd.json_normalize(weather)

                    # Display Weather Alert
                    weather_main = df_weather['weather'][0]['main'].lower()
                    if "rain" in weather_main:
                        st.warning(f"⚠️ Rain detected ({weather_main}). Network conditions may be affected!")

                    # Display Weak Signal Towers
                    st.subheader("📡 Weak Signal Towers")
                    low_signal = df_towers[df_towers['avg_signal'] < -90]
                    if not low_signal.empty:
                        st.map(low_signal[['lat', 'lon']], zoom=12)
                        st.dataframe(low_signal[['lat', 'lon', 'avg_signal']])
                    else:
                        st.success("✅ All nearby towers have good signal strength!")
                else:
                    st.error("❌ API fetch failed! Please check your keys or try again later.")
