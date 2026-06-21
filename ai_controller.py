import firebase_admin
from firebase_admin import credentials, db
import joblib
import numpy as np
from datetime import datetime
import time

# ==========================================
# 1. SETUP & INITIALIZATION
# ==========================================
print("Loading Machine Learning Model...")
model = joblib.load('agri_pump_model.pkl')

print("Connecting to Firebase...")
# Make sure your firebase_key.json is in the same folder!
cred = credentials.Certificate("firebase_key.json")

# REPLACE THIS URL with your actual databaseURL from your web dashboard
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://sensorlogs-d4f82-default-rtdb.europe-west1.firebasedatabase.app'
})

print("✅ AI Controller Online. Listening for live farm data...\n")

# ==========================================
# 2. REAL-TIME AI PREDICTION LOGIC
# ==========================================
def analyze_farm_data(event):
    # This function triggers the millisecond a new reading hits Firebase
    
    # Ignore initial load or empty data
    if event.data is None or not isinstance(event.data, dict):
        return
        
    latest_reading = event.data
    
    try:
        # Extract the exact 5 variables the model was trained on
        soil_moisture = latest_reading['soil_raw']
        soil_temp = latest_reading['soil_temp']
        amb_temp = latest_reading['amb_temp']
        humidity = latest_reading['humidity']
        
        # Get the current hour (0-23)
        current_hour = datetime.now().hour

        # Format it exactly how the model expects it: 
        # [Soil Moisture, Soil Temp, Amb Temp, Humidity, Hour]
        ai_input = np.array([[soil_moisture, soil_temp, amb_temp, humidity, current_hour]])
        
        # Run the Prediction!
        prediction = model.predict(ai_input)[0]
        
        # Send the command to the ESP32 via Firebase
        command_ref = db.reference('control/pump_command')
        command_ref.set(int(prediction))

        # Print the log to your computer screen
        action = "TURN ON" if prediction == 1 else "LEAVE OFF"
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Farm Status: Moisture={soil_moisture}, Temp={amb_temp}°C")
        print(f"🤖 AI Decision: {action}\n")

    except Exception as e:
        print(f"Error processing data: {e}")

# ==========================================
# 3. START LISTENING TO HARDWARE
# ==========================================
# Point to the specific folder where the ESP32 uploads its data
sensor_ref = db.reference('sensor_logs')

# Listen for the newest data added to the logs
sensor_ref.limit_to_last(1).listen(analyze_farm_data)

# Keep the script running forever
while True:
    time.sleep(1)