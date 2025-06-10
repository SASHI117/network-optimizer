import streamlit as st  

def show():  
    # Page Title with Custom Styling  
    st.markdown(  
        """  
        <style>  
        .title {  
            text-align: center;  
            font-size: 36px;  
            font-weight: bold;  
            color: #1E88E5;  
        }  
        .subtitle {  
            text-align: center;  
            font-size: 20px;  
            font-weight: bold;  
            color: #424242;  
        }  
        .highlight {  
            color: #D32F2F;  
            font-weight: bold;  
        }  
        </style>  
        """,  
        unsafe_allow_html=True  
    )  

    # Display Title  
    st.markdown('<p class="title">🚀 Welcome to Network Optimizer!</p>', unsafe_allow_html=True)  
    st.markdown('<p class="subtitle">Optimize connectivity with real-time AI-powered insights.</p>', unsafe_allow_html=True)  

    # Add Image  
    st.image("Images/ai-generated-8259052.jpg", use_column_width=True, caption="Optimizing Networks with AI")  

    # Introduction Section  
    st.markdown("""  
    **📡 What is Network Optimizer?**  
    This **AI-powered tool** analyzes **network performance** and helps optimize connectivity using real-time insights.  
    
    🔹 **How it Works?**  
    1️⃣ **Enter Your Location** (Latitude & Longitude) 📍  
    2️⃣ **Provide API Keys** for network & weather data 🔑  
    3️⃣ **View Real-Time Insights** & AI-powered optimizations 🚀  
    4️⃣ **Get Recommendations** for better connectivity 📈  
    """)  

    # Key Features Section  
    st.subheader("✨ Key Features")  
    st.markdown("""  
    ✅ **Live Network Performance Analysis**  
    ✅ **Weather Impact on Signal Strength**  
    ✅ **AI-Based Optimization & Recommendations**  
    ✅ **User-Friendly Dashboard for Quick Insights**  
    ✅ **Secure & Fast API Integration**  
    """)  

    # Call to Action  
    st.success("🎯 Get Started Now! Enter your location and API keys to begin optimizing your network.")  
