import streamlit as st
from sections.landingpage import show as show_landing
from sections.network import show as show_network



# Streamlit App Setup
st.set_page_config(page_title="Network Optimizer", layout="wide")

# Sidebar Navigation
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Select a Page", ["🏠 Landing Page", "📡 Network Analysis"])

# Load Selected Page
if page == "🏠 Landing Page":
    show_landing()
elif page == "📡 Network Analysis":
    show_network()
else:
    st.title("🤖 AI Assistant")

