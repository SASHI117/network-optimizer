# Network Optimizer

## 🚀 Overview
Network Optimizer is an AI-powered tool designed to analyze network health and weather impact based on real-time data. It provides insights into signal strength, weak network areas, and weather conditions that may affect connectivity.

## 🌟 Features
- **Real-time Network Analysis**: Fetches network tower data based on latitude and longitude.
- **Weather Impact Detection**: Identifies weather conditions that might affect network performance.
- **Interactive UI**: Built with Streamlit for a seamless user experience.
- **AI-based Optimization**: Uses AI algorithms to improve network performance.
- **API Integration**: Supports OpenCelliD and OpenWeatherMap APIs for live data.

## 🏗️ Project Structure
```
Network Optimizer/
│-- app.py                  # Main Streamlit app to run the project
│-- requirements.txt        # Dependencies for the project
│-- sections/               # Contains different sections of the app
│   │-- landing.py          # Landing page
│   │-- network.py          # Network analysis page
│   │-- ai_assistant.py     # AI-based optimization page
│-- utils/
│   │-- api_fetchers.py     # API fetching utilities
│-- Images/
│   │-- ai-visual.jpg       # Image for landing page
│-- README.md               # Project documentation
```

## 📌 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/network-optimizer.git
cd network-optimizer
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application
```bash
streamlit run app.py
```

## 🔑 API Keys Required
Before running the app, ensure you have valid API keys:
- **OpenCelliD API Key** (for network tower data)
- **OpenWeatherMap API Key** (for weather conditions)

These keys should be entered in the **sidebar** when running the app.

## 🎨 UI Sections
- **Landing Page**: Introduction to the app and user guide.
- **Network Analysis**: Fetches network towers and weather data.
- **AI Assistant**: Provides AI-driven recommendations for network optimization.

## 🎥 Video Integration (Optional)
To enhance the user experience, you can replace static images with videos using:
```python
st.video("Videos/network_analysis.mp4")
```

## 🛠️ Future Improvements
- **More AI-powered predictions**
- **Enhanced data visualizations**
- **Mobile-friendly UI**

## 🤝 Contributing
Contributions are welcome! Feel free to submit issues and pull requests.

## 📜 License
This project is open-source under the **MIT License**.

---
🚀 **Built with Python, Streamlit & AI for Network Optimization**

"# network-optimizer" 
