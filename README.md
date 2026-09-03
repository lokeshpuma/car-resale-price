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

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install the dependencies:**
   Make sure you are in the project directory where the `requirements.txt` is located.
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify model files are present:**
   Ensure the following files exist in the project root:
   - `car_price_lin.pkl`
   - `car_price_lass.pkl`

5. **Run the Streamlit application:**
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

## Notes & Troubleshooting

- If the app fails to load models, confirm the `.pkl` files exist and were created with a compatible scikit-learn version.
- If predictions raise an error about input columns, the model may expect a different set of feature column names — check `car_price.ipynb` for the training preprocessing pipeline.
- For development, you can run the notebook `car_price.ipynb` to retrain or inspect feature engineering.

## Results

- **What the app shows:** The app displays the "Predicted Selling Price" in Indian Rupees (₹) formatted to two decimal places.
- **Model choice:** Select either **Linear Regression** or **Lasso Regression** from the sidebar; both use the same input features but may produce different estimates.
- **Non-negative outputs:** Predictions are clamped to zero in the UI (negative predicted values are shown as ₹ 0.00).
- **Interpreting a result:** Treat the prediction as an estimate — use it as a guide alongside market research, vehicle condition, and maintenance history.
- **Example:** For a 2015 petrol manual car with 50,000 km, sold by an individual (First Owner), the app may show a predicted selling price like `₹ 3,45,000.00` (actual values depend on the trained model).

If you'd like, I can add an automated example input section in the app or include a small set of sample inputs and expected outputs in `car_price.ipynb` for reproducibility.
