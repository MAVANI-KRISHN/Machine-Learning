import pandas as pd
import joblib

# Load the model
housing_model = joblib.load('Day 2/linear_regression_model.pkl')

# Define the input data for prediction
input_data = pd.DataFrame({
    'area': [1500],
    'bedrooms': [3],
    'bathrooms': [2],
    'stories': [1],
    'parking': [2],
    'mainroad_yes': [1],
    'guestroom_yes': [0],
    'basement_yes': [1],
    'hotwaterheating_yes': [1],
    'airconditioning_yes': [0],
    'prefarea_yes': [1],
    'furnishingstatus_semi-furnished': [1],
    'furnishingstatus_unfurnished': [0]
})

# Make the prediction and print the result
predicted_price = housing_model.predict(input_data)[0]
# print(predicted_price)

# Only run if script is executed directly
if __name__ == "__main__":
    print(f"The predicted price for the house is: {predicted_price}")
