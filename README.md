# Real Estate Price Predictor

This project is a machine learning-powered web app that predicts housing prices in Los Angeles based on property details like bedrooms, bathrooms, square footage, and geographic location (latitude & longitude).

Built with:
- Python
- Scikit-learn
- Streamlit
- Google Colab

---

## Features

- Scrapes real housing listings from Redfin  
- Cleans and preprocesses data using pandas  
- Trains a regression model to predict home prices  
- Web app interface using Streamlit  
- Allows real-time predictions based on user input  
- Plots geographic price predictions using lat/lon (future improvement)

---

## How It Works

### 1. Data Collection
Data is scraped from [Redfin](https://www.redfin.com/), and includes:
- Price
- Beds, Baths, SqFt
- Address
- Latitude, Longitude

### 2. Data Cleaning
Data is cleaned and transformed using pandas in a separate Colab notebook:
- Converted to numeric format
- Extracted ZIP codes
- Dropped missing values

### 3. Model Training
A regression model is trained using:
- Features: Beds, Baths, SqFt, Latitude, Longitude
- Target: Price
- Model: Linear Regression

### 4. Web App
The app takes user input and predicts a home’s price in real-time.

---

## Run It Yourself

### Option 1: Locally

```bash
git clone https://github.com/<your-username>/real-estate-price-predictor.git
cd real-estate-price-predictor
pip install -r requirements.txt
streamlit run app.py
```
### Option 2: Streamlit Cloud

https://aung-thu-real-estate-price-predictor.streamlit.app/

---

## Project Structure

```bash
├── app.py                                  # Streamlit app
├── requirements.txt                        # Dependencies
├── price_model.pkl                         # Trained ML model
├── scaler.pkl                              # Feature scaler
├── redfin_async_batched.csv                # Cleaned dataset
├── real_estate_scraper.ipynb               # Web scrapper
├── data_cleaning_and_ML_modeling.ipynb     # Data Cleaning process
└── README.md                               # This file
```
---

## Example Prediction

Input: 3 beds, 2 baths, 1500 sqft, Lat: 34.05, Lon: -118.24.  
Output: $825,000 predicted price

---

## To-Do (Future Enhancements)

- Add Google Maps or Folium map view of results
- Add ZIP code comparison chart
- Try advanced models (XGBoost, LightGBM)
- Cache scraped listings for speed