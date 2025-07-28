
# ⚡ Smart Network Optimizer

## 🔍 Overview  
**Smart Network Optimizer** is an AI-powered application I developed to monitor, analyze, and optimize network performance in real time. The tool combines live weather data and geolocation-based network tower information to detect signal strength patterns and environmental disruptions. It provides AI-powered insights for better connectivity decisions and optimization.

---

## ✨ Key Highlights
- **📡 Real-Time Signal Monitoring** – Detects and visualizes nearby network towers using latitude and longitude.
- **⛅ Weather-Aware Analysis** – Analyzes weather conditions that may impact network performance.
- **🖥️ Interactive Interface** – Designed using Streamlit to ensure a smooth, responsive user experience.
- **🤖 AI-Driven Recommendations** – Applies machine learning (Random Forest) to predict and suggest network improvements.
- **🔗 API Integrations** – Uses OpenCelliD and OpenWeatherMap APIs for accurate, real-time data.

---

## 🧩 Project Architecture
```
smart-network-optimizer/
│-- app.py                  # Entry point of the Streamlit web app
│-- requirements.txt        # List of Python dependencies
│-- sections/               # Organized UI sections
│   │-- landing.py          # Intro and guide section
│   │-- network.py          # Network data visualization & insights
│   │-- ai_assistant.py     # AI-based recommendations
│-- utils/
│   │-- api_fetchers.py     # Utilities for API data fetching
│-- Images/
│   │-- ai-visual.jpg       # Banner for landing section
│-- README.md               # Project documentation
```

---

## ⚙️ Installation Guide

### 🔽 Clone the Repository
```bash
git clone https://github.com/your-username/smart-network-optimizer.git
cd smart-network-optimizer
```

### 🧪 Install Required Packages
```bash
pip install -r requirements.txt
```

### 🚀 Launch the App
```bash
streamlit run app.py
```

---

## 🔐 API Keys Needed
Before running the app, ensure you have the following API keys:
- **OpenCelliD API Key** – for accessing network tower data  
- **OpenWeatherMap API Key** – for fetching live weather conditions  

👉 These keys can be entered via the app sidebar during runtime.

---

## 🧭 App Navigation
- **Landing Page**: Introduction and quick guide to using the app  
- **Network Analyzer**: Live data on network towers and environmental conditions  
- **AI Assistant**: Machine learning-based recommendations to enhance connectivity  

---

## 🎥 Media Enhancement (Optional)
To replace static images with video demos, you can use the following in your `app.py`:
```python
st.video("Videos/network_analysis.mp4")
```

---

## 🧠 Future Roadmap
- Integration of advanced AI models for more precise predictions  
- Enhanced visualizations with Plotly/Altair  
- Mobile-responsive layout for broader accessibility  
- Auto-alerts for weak signal detection

---

## 🙌 Built With
- **Python**
- **Streamlit**
- **Random Forest (scikit-learn)**
- **OpenWeatherMap API**
- **OpenCelliD API**

---

> 👨‍💻 Developed with 💡 by Sashi Vardhan Pragada  
> For any inquiries: mesashivardhan4080@gmail.com
