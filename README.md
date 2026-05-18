# Car Resale Price Predictor

This project provides a Streamlit web application that predicts the resale price of cars based on key features such as the year of manufacture, kilometers driven, fuel type, seller type, transmission, and the number of previous owners.

The app is powered by two pre-trained machine learning models:
1. **Linear Regression** (`car_price_lin.pkl`)
2. **Lasso Regression** (`car_price_lass.pkl`)

## Features Used
- `year`: The year the car was purchased/manufactured.
- `km_driven`: Total kilometers the car has been driven.
- `fuel`: Fuel type (Petrol, Diesel, CNG, LPG, or Electric).
- `seller_type`: Who is selling the car (Individual, Dealer, or Trustmark Dealer).
- `transmission`: Transmission type (Manual or Automatic).
- `owner`: History of previous owners (First, Second, Third, Fourth & Above, Test Drive Car).

## Installation & Setup

1. **Clone the repository:**
   If this project is in a GitHub repository, clone it to your local machine.

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   conda create -n tf python=3.10
   conda activate tf
   ```
   *(Note: The environment is named `tf`, matching the standard project configuration.)*

3. **Install the dependencies:**
   Make sure you are in the project directory where the `requirements.txt` is located.
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```

## Usage

- Once the command is run, Streamlit will provide a local server link (usually `http://localhost:8501`).
- Open the link in your web browser.
- Use the sidebar to choose between the **Linear Regression** and **Lasso Regression** models.
- Input the car details into the main form on the page.
- Click the **Predict Price** button to see the estimated resale value.

## Files Structure

- `app.py`: Main application code for the Streamlit UI and ML model inference.
- `requirements.txt`: List of required Python packages to run the app.
- `README.md`: Project documentation and setup instructions for visitors.
- `car_price.ipynb`: Jupyter notebook containing data exploration and model training logic.
- `car_price_lin.pkl` / `car_price_lass.pkl`: Serialized pre-trained machine learning models.
- `car.csv`: Original dataset used to train the models.
