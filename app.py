from flask import Flask, request, jsonify, render_template
from sklearn import preprocessing
import pickle
import numpy as np
import logging
import os

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Load the model
model_path = 'C:\web dev\Intern-DSR\model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)
app.logger.info(f"Model loaded from {model_path}")

# Check if template files exist
template_path_index = os.path.join(app.root_path, 'templates', 'index.html')
app.logger.info(f"Index.html exists: {os.path.exists(template_path_index)}")
template_path_result = os.path.join(app.root_path, 'templates', 'result.html')
app.logger.info(f"Result.html exists: {os.path.exists(template_path_result)}")

@app.route('/')
def index():
    app.logger.info('Rendering index.html')
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        app.logger.info('POST request received at /predict')
        
        # Reading input data from form
        input_features = [float(x) for x in request.form.values()]
        app.logger.info(f"Form data received: {input_features}")

        # Preparing input for prediction
        input_array = np.array(input_features).reshape(1, -1)
        
        # Normalize the input if needed (you might need to adjust this based on your model)
        input_normalized = preprocessing.normalize(input_array)
        
        # Predict using the loaded model
        prediction = model.predict(input_normalized)
        
        # Round the prediction (if your prediction is a single value, otherwise adjust accordingly)
        prediction_rounded = np.round(prediction, 2)
        app.logger.info(f"Predicted values: {prediction_rounded}")

        # Render result.html with the predicted values
        return render_template('result.html', 
                               a1=prediction_rounded[0][0], 
                               a2=prediction_rounded[0][1],
                               a3=prediction_rounded[0][2],
                               a4=prediction_rounded[0][3],
                               a5=prediction_rounded[0][4],
                               a6=prediction_rounded[0][5],
                               a7=prediction_rounded[0][6])
    else:
        app.logger.error('Method Not Allowed')
        return "Method Not Allowed", 405

@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error(f"An error occurred: {e}")
    return "An internal error occurred", 500

if __name__ == "__main__":
    app.run(debug=True, port=8000)
