from flask import Flask, request, render_template, redirect, url_for
import pickle
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the trained RandomForest model
with open('crop_recommendation_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Route for the home page (form)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/CropWise')
def index():
    return render_template('index.html')

# Route for predicting the recommended crop (form submission)
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the form data from the request
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        # Create a NumPy array of the input features for the model
        input_features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

        # Use the trained model to make a prediction
        prediction = model.predict(input_features)

        # Render the result page with the predicted crop
        return render_template('result.html', crop=prediction[0])

    except Exception as e:
        return f"Error: {str(e)}"

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
