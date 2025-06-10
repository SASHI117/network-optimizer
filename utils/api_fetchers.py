import requests  
import json  

def get_cell_towers(api_key, lat, lon, radius=5000):  
    url = "https://opencellid.org/api/cell/search"  
    params = {  
        "key": api_key,  
        "lat": lat,  
        "lon": lon,  
        "distance": radius,  
        "format": "json"  
    }  
    response = requests.get(url, params=params)  
    if response.status_code == 200:  
        return response.json()  
    else:  
        print("OpenCelliD Error:", response.text)  
        return None  

def get_weather(api_key, lat, lon):  
    url = "https://api.openweathermap.org/data/2.5/weather"  
    params = {  
        "lat": lat,  
        "lon": lon,  
        "appid": api_key,  
        "units": "metric"  
    }  
    response = requests.get(url, params=params)  
    if response.status_code == 200:  
        return response.json()  
    else:  
        print("Weather API Error:", response.text)  
        return None  