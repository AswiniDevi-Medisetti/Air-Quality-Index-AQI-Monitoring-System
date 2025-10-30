import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import pickle
import warnings
warnings.filterwarnings('ignore')

# Sample AQI data creation - in real scenario, you'd use actual dataset
def create_sample_data():
    np.random.seed(42)
    n_samples = 1000
    
    data = {
        'PM2.5': np.random.uniform(0, 500, n_samples),
        'PM10': np.random.uniform(0, 500, n_samples),
        'NO2': np.random.uniform(0, 200, n_samples),
        'SO2': np.random.uniform(0, 100, n_samples),
        'CO': np.random.uniform(0, 10, n_samples),
        'O3': np.random.uniform(0, 200, n_samples),
        'Temperature': np.random.uniform(10, 40, n_samples),
        'Humidity': np.random.uniform(20, 90, n_samples)
    }
    
    df = pd.DataFrame(data)
    
    # Calculate AQI based on Indian AQI standards (simplified)
    def calculate_aqi(row):
        # Simplified AQI calculation - in reality, it's more complex
        pm25_aqi = (row['PM2.5'] / 60) * 100
        pm10_aqi = (row['PM10'] / 100) * 100
        no2_aqi = (row['NO2'] / 80) * 100
        so2_aqi = (row['SO2'] / 80) * 100
        co_aqi = (row['CO'] / 4) * 100
        o3_aqi = (row['O3'] / 100) * 100
        
        aqi = max(pm25_aqi, pm10_aqi, no2_aqi, so2_aqi, co_aqi, o3_aqi)
        return min(aqi, 500)  # Cap at 500
    
    df['AQI'] = df.apply(calculate_aqi, axis=1)
    
    return df

def train_aqi_model():
    print("Creating sample AQI data...")
    df = create_sample_data()
    
    print("Data Summary:")
    print(f"Dataset shape: {df.shape}")
    print(f"AQI Range: {df['AQI'].min():.2f} - {df['AQI'].max():.2f}")
    
    # Prepare features and target
    features = ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3', 'Temperature', 'Humidity']
    X = df[features]
    y = df['AQI']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    print("\nTraining Random Forest model...")
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate model
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"\nModel Performance:")
    print(f"Mean Absolute Error: {mae:.2f}")
    print(f"R² Score: {r2:.4f}")
    
    # Save model
    with open('aqi_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    print("\nModel saved as 'aqi_model.pkl'")
    
    # Feature importance
    importance = pd.DataFrame({
        'feature': features,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    print("\nFeature Importance:")
    print(importance)
    
    return model, features

if __name__ == "__main__":
    train_aqi_model()