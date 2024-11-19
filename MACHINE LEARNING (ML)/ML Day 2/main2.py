import pandas as pd
import joblib

class HousingPricePredictor:
    def __init__(self, model_path):
        # Load the trained model
        self.model = joblib.load(model_path)
    
    def predict_price(self, area, bedrooms, bathrooms, stories, parking, mainroad, guestroom, basement, hotwaterheating, airconditioning, prefarea, furnishingstatus):
        # Create a DataFrame with the input values
        input_data = pd.DataFrame({
            'area': [area],
            'bedrooms': [bedrooms],
            'bathrooms': [bathrooms],
            'stories': [stories],
            'parking': [parking],
            'mainroad_yes': [1 if mainroad else 0],
            'guestroom_yes': [1 if guestroom else 0],
            'basement_yes': [1 if basement else 0],
            'hotwaterheating_yes': [1 if hotwaterheating else 0],
            'airconditioning_yes': [1 if airconditioning else 0],
            'prefarea_yes': [1 if prefarea else 0],
            'furnishingstatus_semi-furnished': [1 if furnishingstatus == 'semi-furnished' else 0],
            'furnishingstatus_unfurnished': [1 if furnishingstatus == 'unfurnished' else 0]
        })
        # Predict the price
        predicted_price = self.model.predict(input_data)[0]
        return predicted_price

    def get_user_input(self):
        # Collect user input
        area = float(input("Enter the area (in sq ft): "))
        bedrooms = int(input("Enter the number of bedrooms: "))
        bathrooms = int(input("Enter the number of bathrooms: "))
        stories = int(input("Enter the number of stories: "))
        parking = int(input("Enter the number of parking spaces: "))
        
        mainroad = input("Is the house on the main road? (yes/no): ").strip().lower() == 'yes'
        guestroom = input("Does the house have a guestroom? (yes/no): ").strip().lower() == 'yes'
        basement = input("Does the house have a basement? (yes/no): ").strip().lower() == 'yes'
        hotwaterheating = input("Does the house have hot water heating? (yes/no): ").strip().lower() == 'yes'
        airconditioning = input("Does the house have air conditioning? (yes/no): ").strip().lower() == 'yes'
        prefarea = input("Is the house in a preferred area? (yes/no): ").strip().lower() == 'yes'
        
        furnishingstatus = input("Enter the furnishing status (semi-furnished/unfurnished): ").strip().lower()

        return (area, bedrooms, bathrooms, stories, parking, mainroad, guestroom, basement, hotwaterheating, airconditioning, prefarea, furnishingstatus)

    def run(self):
        # Get user input
        inputs = self.get_user_input()
        # Predict the price
        price = self.predict_price(*inputs)
        # Print the predicted price
        print(f"The predicted price for the house is: ${price:.2f}")

# Run the script if executed directly
if __name__ == "__main__":
    predictor = HousingPricePredictor('Day 2/linear_regression_model.pkl')
    predictor.run()
