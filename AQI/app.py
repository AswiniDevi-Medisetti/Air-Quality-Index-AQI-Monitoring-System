from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd
from datetime import datetime
import json

app = Flask(__name__)

# Load the trained model
try:
    with open('aqi_model.pkl', 'rb') as f:
        model = pickle.load(f)
    model_loaded = True
    features = ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3', 'Temperature', 'Humidity']
except:
    model_loaded = False
    features = []

def get_aqi_category(aqi):
    if aqi <= 50:
        return 'Good', 'bg-success'
    elif aqi <= 100:
        return 'Satisfactory', 'bg-info'
    elif aqi <= 200:
        return 'Moderate', 'bg-warning'
    elif aqi <= 300:
        return 'Poor', 'bg-orange'
    elif aqi <= 400:
        return 'Very Poor', 'bg-danger'
    else:
        return 'Severe', 'bg-purple'

def get_health_advice(aqi):
    if aqi <= 50:
        return "Air quality is good. Perfect for outdoor activities."
    elif aqi <= 100:
        return "Air quality is satisfactory. Minor breathing discomfort to sensitive people."
    elif aqi <= 200:
        return "Air quality is moderate. Breathing discomfort to people with lung disease."
    elif aqi <= 300:
        return "Air quality is poor. Breathing discomfort to most people on prolonged exposure."
    elif aqi <= 400:
        return "Air quality is very poor. Respiratory illness on prolonged exposure."
    else:
        return "Air quality is severe. Affects healthy people and seriously impacts those with existing diseases."

@app.route('/')
def home():
    return render_template('index.html', page='home')

@app.route('/about')
def about():
    return render_template('index.html', page='about')

@app.route('/dashboard')
def dashboard():
    return render_template('index.html', page='dashboard')

@app.route('/predict', methods=['POST'])
def predict():
    if not model_loaded:
        return jsonify({'error': 'Model not loaded'})
    
    try:
        # Get data from form
        data = {
            'PM2.5': float(request.form['pm25']),
            'PM10': float(request.form['pm10']),
            'NO2': float(request.form['no2']),
            'SO2': float(request.form['so2']),
            'CO': float(request.form['co']),
            'O3': float(request.form['o3']),
            'Temperature': float(request.form['temp']),
            'Humidity': float(request.form['humidity'])
        }
        
        # Create feature array
        feature_array = np.array([[data[feature] for feature in features]])
        
        # Make prediction
        aqi_prediction = model.predict(feature_array)[0]
        
        # Get AQI category and advice
        category, color_class = get_aqi_category(aqi_prediction)
        advice = get_health_advice(aqi_prediction)
        
        result = {
            'aqi': round(aqi_prediction, 2),
            'category': category,
            'color_class': color_class,
            'advice': advice,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/get_sample_data')
def get_sample_data():
    # Generate sample data for dashboard
    cities = ['Hyderabad', 'Bangalore', 'Chennai', 'Mumbai', 'Delhi', 'Kolkata']
    data = []
    
    for city in cities:
        aqi = np.random.uniform(50, 400)
        category, color_class = get_aqi_category(aqi)
        data.append({
            'city': city,
            'aqi': round(aqi, 2),
            'category': category,
            'color_class': color_class,
            'pm25': round(np.random.uniform(20, 300), 2),
            'pm10': round(np.random.uniform(30, 400), 2)
        })
    
    return jsonify(data)

if __name__ == '__main__':
    print("Starting AQI Monitoring System...")
    if model_loaded:
        print("Model loaded successfully!")
    else:
        print("Warning: Model not loaded. Please run model_training.py first.")
    app.run(debug=True)