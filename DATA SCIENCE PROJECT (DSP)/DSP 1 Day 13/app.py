# import joblib
# import pickle

# # Load the model using joblib
# model = joblib.load('random_forest_model.joblib')  # Replace with your actual joblib file

# # Save the model using pickle
# with open('random_forest_model.pkl', 'wb') as f:
#     pickle.dump(model, f)


from flask import Flask, request, jsonify
import joblib  # or pickle if you're using pickle to load the model
import pandas as pd

app = Flask(__name__)

# Load your model
model = joblib.load('random_forest_model.pkl')  # Replace with actual path to model file

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the request
        data = request.get_json(force=True)
        
        # Convert the data into a DataFrame
        input_data = pd.DataFrame([data])
        
        # Make predictions
        prediction = model.predict(input_data)
        
        # Format the response
        response = {'prediction': prediction[0]}
        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
