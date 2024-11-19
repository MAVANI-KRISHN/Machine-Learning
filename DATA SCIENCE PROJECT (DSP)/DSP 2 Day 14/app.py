from flask import Flask, request, jsonify
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from joblib import load

# Initialize the Flask app
app = Flask(__name__)

# Load the saved model
try:
    model = tf.keras.models.load_model('sentiment_model.h5')
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")

# Load the tokenizer
try:
    tokenizer = load('tokenizer.joblib')
    print("Tokenizer loaded successfully.")
except Exception as e:
    print(f"Error loading tokenizer: {e}")

# Define the maximum sequence length (must match the value used during training)
max_length = 100

# Create a function to predict sentiment
def predict_sentiment(text):
    # Tokenize and pad the input text
    sequences = tokenizer.texts_to_sequences([text])
    if not sequences or all(len(seq) == 0 for seq in sequences):
        return {"error": "The input text could not be tokenized. Make sure the text contains valid words."}

    padded = pad_sequences(sequences, maxlen=max_length, truncating='post')

    # Predict the sentiment
    prediction = model.predict(padded)

    # Determine the sentiment based on the prediction
    sentiment = ["Negative", "Neutral", "Positive"][prediction.argmax()]
    return {
        "sentiment": sentiment,
        "prediction_scores": prediction[0].tolist()
    }

# Define the route for the API
@app.route('/predict', methods=['POST'])

def predict():
    try:
        # Get the input text from the JSON request
        data = request.get_json()
        user_input = data.get("text")

        if not user_input:
            return jsonify({"error": "No text provided."}), 400

        # Call the prediction function
        result = predict_sentiment(user_input)
        if "error" in result:
            return jsonify(result), 400

        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
