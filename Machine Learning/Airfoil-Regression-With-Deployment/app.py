import pickle
import os
import logging
from flask import Flask, request, jsonify, url_for, render_template
import numpy as np
import pandas as pd
from werkzeug.utils import secure_filename

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-dev-key')

# Load model once at startup
try:
    model = pickle.load(open('model.pkl', 'rb'))
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Error loading model: {str(e)}")
    model = None

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    try:
        if model is None:
            return jsonify({"success": False, "error": "Model not loaded"}), 500

        data = request.json['data']
        logger.info(f"API Input: {data}")

        # Validate input data
        if not all(isinstance(v, (int, float)) for v in data.values()):
            return jsonify({"success": False, "error": "All values must be numeric"}), 400

        new_data = [list(data.values())]
        output = model.predict(new_data)[0]

        # Format the output
        formatted_output = round(float(output), 2)

        logger.info(f"API Prediction: {formatted_output}")
        return jsonify({
            "success": True,
            "prediction": formatted_output,
            "prediction_unit": "dB"
        })
    except KeyError:
        return jsonify({"success": False, "error": "Missing 'data' key in request"}), 400
    except Exception as e:
        logger.error(f"API prediction error: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 400

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if model is None:
            return render_template('home.html',
                                  error_message="Model not loaded. Please contact the administrator.")

        data = [float(x) for x in request.form.values()]
        final_features = [np.array(data)]
        logger.info(f"Form Input: {data}")

        output = model.predict(final_features)[0]
        logger.info(f"Prediction: {output}")

        # Format the output to 2 decimal places for better readability
        formatted_output = round(float(output), 2)

        # Get the input parameter names for displaying in the result
        param_names = ["Frequency", "Angle of Attack", "Chord Length",
                       "Free-stream Velocity", "Suction Side"]

        # Add units to the displayed parameters with proper HTML entities
        units = ["Hz", "&#176;", "m", "m/s", "m"]

        # Create a dictionary of input parameters with units for display
        input_params = {name: f"{value} {unit}"
                       for name, value, unit in zip(param_names, data, units)}

        return render_template('home.html',
                              prediction_text=f"{formatted_output} dB",
                              show_result=True,
                              input_params=input_params)
    except ValueError as e:
        logger.error(f"Value error during prediction: {str(e)}")
        return render_template('home.html',
                              error_message="Please ensure all inputs are valid numbers.")
    except Exception as e:
        logger.error(f"Error during prediction: {str(e)}")
        return render_template('home.html',
                              error_message="An error occurred during prediction. Please check your inputs.")

@app.errorhandler(404)
def page_not_found(e):
    logger.warning(f"Page not found: {request.path}")
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    logger.error(f"Server error: {str(e)}")
    return render_template('500.html'), 500

# Add a health check endpoint
@app.route('/health')
def health_check():
    if model is None:
        return jsonify({"status": "error", "message": "Model not loaded"}), 500
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)