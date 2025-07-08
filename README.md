# real-estate-price-prediction
# 🏠 Real Estate Price Prediction Web App

This project is a **Machine Learning-powered web application** that predicts real estate prices based on user inputs such as location, square footage, number of bathrooms, and number of bedrooms (BHK). The app is built using **Python**, **Flask**, and **Scikit-Learn**, and uses a **Ridge Regression model** for price prediction.

---

## 🚀 Features

- Predicts house prices in **lakhs** based on key parameters.
- Uses **pre-trained Ridge Regression model** (`RidgeModel.pkl`).
- Interactive web interface built with **Flask**.
- Loads pre-cleaned data from **`cleaned_data.csv`**.
- Achieves an **R² score of 0.82**, indicating strong predictive performance.

---

## 📂 Project Structure

├── cleaned_data.csv
├── RidgeModel.pkl
├── app.ipynb # Model training & evaluation notebook
├── main.py # Flask web app
├── templates/
│ └── index.html # HTML frontend
└── README.md


---

## ⚙️ Tech Stack

- **Python 3.x**
- **Flask**
- **Pandas**
- **Scikit-learn**
- **Pickle**

---

## 📊 Model Overview

- Model: **Ridge Regression**
- R² Score: **0.822 (82.2%)**
- Target: House prices (in lakhs)
- Features used:
  - Location
  - Total Square Footage
  - Number of Bathrooms
  - Number of Bedrooms (BHK)

---
real-estate-price-prediction
