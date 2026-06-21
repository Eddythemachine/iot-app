# IoT-Based Precision Agriculture Monitoring & Predictive Irrigation System

## Abstract
This project presents an integrated IoT-based precision agriculture solution designed for automated crop monitoring and adaptive irrigation management. Utilizing an ESP32 microcontroller network, the system captures real-time environmental telemetry—including soil moisture, ambient and soil temperature, and atmospheric humidity. These data points are processed via a Firebase Realtime Database and analyzed by a Gradient Boosting Classifier, which facilitates predictive irrigation control to optimize water usage and resource allocation in agricultural environments.

## System Architecture
The system architecture follows a closed-loop feedback mechanism:
1. **Data Acquisition:** ESP32 sensors capture localized environmental data.
2. **Data Ingestion:** Telemetry is transmitted via Wi-Fi to a Firebase Realtime Database.
3. **Analytical Layer:** A Python-based controller implements a trained `GradientBoostingClassifier` to infer the optimal pump state.
4. **Actuation:** The AI-driven decision is relayed back to the Firebase control node, where the ESP32 executes the final irrigation command.

## Technical Stack
- **Hardware:** ESP32 Microcontroller, capacitive soil moisture sensors, DHT22 temperature/humidity sensors.
- **Backend:** Firebase Realtime Database.
- **Frontend:** HTML5/CSS3 Dashboard with Chart.js visualization.
- **Machine Learning:** Python (Scikit-Learn, Joblib, Pandas, Seaborn).

## Repository Structure
- `/dashboard`: Contains `index.html`, `style.css`, and Firebase integration scripts.
- `/model`: Contains the serialized `agri_pump_model.pkl` and training notebooks.
- `/controller`: Contains `ai_controller.py` for real-time inference and cloud communication.

---

## Data Analysis & Results
*(This section is reserved for your technical insights and findings)*

### 1. Exploratory Data Analysis (EDA)
[Insert your EDA observations here—e.g., discussion on bimodal distribution of humidity, thermal mass observations, and outlier handling]

### 2. Model Performance Evaluation
[Insert your performance metrics here—e.g., accuracy, confusion matrix analysis, and AUC-ROC score discussion]

---

## Implementation Guide
1. **Firebase Configuration:** Initialize your project in the Firebase Console and obtain your `firebaseConfig` keys.
2. **Deployment:** Ensure the `ai_controller.py` and `agri_pump_model.pkl` files are in the same directory.
3. **Environment Setup:** ```bash
   pip install firebase-admin joblib pandas scikit-learn numpy

## Execution: Configure the firebase_key.json and execute the controller:
Bash
python ai_controller.py
