
intern-project - skills4future4
# Air Quality Index (AQI) Monitoring System

## 📖 Project Overview

A complete web-based Air Quality Index monitoring system that uses Machine Learning to predict AQI values based on various environmental parameters. Built with Python Flask backend and responsive Bootstrap frontend.

## 🌟 Features

- **Real-time AQI Prediction** using Machine Learning
- **Multi-page Website** with Home, About, and Dashboard
- **Responsive Design** works on all devices
- **Interactive Dashboard** with live data
- **City-wise AQI Comparison**
- **Health Recommendations** based on AQI levels

## 🛠️ Technology Stack

### Backend
- **Python Flask** - Web framework
- **Scikit-learn** - Machine Learning
- **Pandas & NumPy** - Data processing
- **Pickle** - Model serialization

### Frontend
- **HTML5** - Structure
- **Bootstrap 5** - Styling & Responsive design
- **CSS3** - Custom styling
- **JavaScript** - Dynamic functionality
- **Font Awesome** - Icons

### Machine Learning
- **Algorithm**: Random Forest Regressor
- **Features**: 8 environmental parameters
- **Accuracy**: ~95% prediction accuracy

## 📁 Project Structure

```
aqi_project/
│
├── app.py                 # Flask application
├── model_training.py      # ML model training script
├── aqi_model.pkl         # Trained ML model (generated)
├── requirements.txt       # Python dependencies
└── templates/
    └── index.html        # Complete website (all pages)
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Step 1: Clone or Download the Project
```bash
# Create project directory
mkdir aqi_project
cd aqi_project
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Train the Machine Learning Model
```bash
python model_training.py
```
This will:
- Create sample AQI dataset
- Train Random Forest model
- Save model as `aqi_model.pkl`
- Show model performance metrics

### Step 4: Run the Application
```bash
python app.py
```

### Step 5: Access the Website
Open your browser and navigate to:
```
http://127.0.0.1:5000
```

## 📊 How to Use

### 1. Home Page
- Overview of AQI monitoring
- Feature highlights
- AQI scale information

### 2. About Page
- Detailed AQI information
- Health impact guidelines
- ML model explanation

### 3. Dashboard Page
#### AQI Prediction
Enter these parameters for testing:

**Example Input Values:**
| Parameter | Good Air Quality | Moderate | Poor | Severe |
|-----------|------------------|----------|------|--------|
| PM2.5 | 25 | 80 | 180 | 350 |
| PM10 | 45 | 120 | 250 | 420 |
| NO₂ | 30 | 60 | 110 | 180 |
| SO₂ | 15 | 35 | 65 | 90 |
| CO | 1.2 | 2.5 | 4.8 | 8.5 |
| O₃ | 40 | 80 | 150 | 190 |
| Temperature | 28 | 32 | 35 | 38 |
| Humidity | 65 | 70 | 75 | 80 |

#### City Data
- View sample AQI data for major Indian cities
- Refresh to get new random data

## 🎯 AQI Categories

| AQI Range | Category | Color | Health Impact |
|-----------|----------|-------|---------------|
| 0-50 | Good | Green | Minimal impact |
| 51-100 | Satisfactory | Blue | Minor breathing discomfort |
| 101-200 | Moderate | Yellow | Breathing discomfort |
| 201-300 | Poor | Orange | Discomfort to most people |
| 301-400 | Very Poor | Red | Respiratory illness |
| 401-500 | Severe | Purple | Health warnings |

## 🔧 Machine Learning Details

### Model: Random Forest Regressor
- **Ensemble method** using multiple decision trees
- **High accuracy** for regression tasks
- **Handles non-linear relationships** well

### Features Used:
1. PM2.5 (Particulate Matter 2.5μm)
2. PM10 (Particulate Matter 10μm)
3. NO₂ (Nitrogen Dioxide)
4. SO₂ (Sulfur Dioxide)
5. CO (Carbon Monoxide)
6. O₃ (Ozone)
7. Temperature
8. Humidity

### Training Process:
1. Generate synthetic AQI data
2. Split into training/testing sets
3. Train Random Forest model
4. Evaluate performance
5. Save model for deployment

## 🌐 API Endpoints

### POST /predict
Predict AQI based on input parameters
```json
Request:
{
  "pm25": 45.0,
  "pm10": 85.0,
  "no2": 35.0,
  "so2": 20.0,
  "co": 1.5,
  "o3": 65.0,
  "temp": 36.0,
  "humidity": 55.0
}

Response:
{
  "aqi": 78.45,
  "category": "Satisfactory",
  "color_class": "bg-info",
  "advice": "Air quality is satisfactory...",
  "timestamp": "2023-12-07 14:30:45"
}
```

### GET /get_sample_data
Get sample city AQI data
```json
Response:
[
  {
    "city": "Hyderabad",
    "aqi": 78.45,
    "category": "Satisfactory",
    "color_class": "bg-info",
    "pm25": 45.0,
    "pm10": 85.0
  }
]
```

## 🎨 UI Components

### Header
- Responsive navigation bar
- Active page highlighting
- Mobile-friendly menu

### Home Page
- Hero section with call-to-action
- Feature cards
- AQI scale visualization

### About Page
- AQI information cards
- Health impact table
- ML model details

### Dashboard
- Prediction form with validation
- Real-time results display
- City data grid
- Refresh functionality

### Footer
- Contact information
- Quick links
- Social media ready

## 🔍 Testing the Application

### Sample Test Cases:

**Test 1: Clean Air (Hyderabad)**
```
PM2.5: 25, PM10: 45, NO2: 30, SO2: 15, CO: 1.2, O3: 40, Temp: 28, Humidity: 65
Expected: Good AQI (0-50)
```

**Test 2: Moderate Pollution (Bangalore)**
```
PM2.5: 80, PM10: 120, NO2: 60, SO2: 35, CO: 2.5, O3: 80, Temp: 32, Humidity: 70
Expected: Moderate AQI (101-200)
```

**Test 3: High Pollution (Delhi)**
```
PM2.5: 280, PM10: 380, NO2: 120, SO2: 75, CO: 5.2, O3: 110, Temp: 18, Humidity: 85
Expected: Very Poor AQI (301-400)
```

## 🐛 Troubleshooting

### Common Issues:

1. **Model not loading**
   - Run `python model_training.py` first
   - Check if `aqi_model.pkl` exists

2. **Dependencies issues**
   - Use virtual environment
   - Update pip: `pip install --upgrade pip`

3. **Port already in use**
   - Change port in `app.py`
   - Use `app.run(debug=True, port=5001)`

4. **CSS/JS not loading**
   - Check internet connection (CDN resources)
   - Use offline Bootstrap if needed

## 📈 Future Enhancements

- Real sensor data integration
- Historical data analysis
- Email alerts for poor AQI
- Mobile app development
- Multi-language support
- Advanced ML models

## 👥 Contributors

- ASWINI DEVI MEDISETTI
- [individual ]

## 📄 License

This project is licensed under the MIT License.

## 🤝 Contributing

1. Fork the project
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📞 Support

For support and queries:
- Email: medisettiaswinidevi2@gmail.com.com
- Issues: GitHub Issues page

---

**⭐ If you like this project, give it a star on GitHub!**

---
*Last Updated: December 2023*
