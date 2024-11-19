from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

@app.route('/test', methods=['GET'])
def hello():
    return "Hello! Welcome to the Flask API!"


@app.route('/ml', methods=['GET'])
def ml_fun():
    return "We are Data Science Students, Name Is Deven, Yadav, Divyaraj And Me Krishn"

# if __name__ == '_main_':
app.run(debug=True)