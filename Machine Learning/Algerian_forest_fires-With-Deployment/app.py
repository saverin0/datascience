from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier  # Or your best model
from pymongo import MongoClient
import logging

# Logging setup
logging.basicConfig(filename='api.log', level=logging.INFO, 
                    format='%(asctime)s %(levelname)s: %(message)s')

class ModelAPI:
    def __init__(self, model_path, mongo_uri):
        try:
            self.model = RandomForestClassifier()  # Replace if needed
            # self.model.load(model_path)  # Uncomment if loading from file
            self.mongo_client = MongoClient(mongo_uri)
            self.db = self.mongo_client['your_database_name']  
            self.collection = self.db['your_collection_name']
        except Exception as e:
            logging.error(f"Error during initialization: {e}")
            raise

    def single_prediction(self, data):
        try:
            data = pd.DataFrame([data])
            prediction = self.model.predict(data)[0]
            return {"prediction": prediction}
        except Exception as e:
            logging.error(f"Error during single prediction: {e}")
            raise

    def bulk_prediction(self):
        try:
            data = pd.DataFrame(list(self.collection.find())) 
            data = data[['Temperature', 'RH', 'Ws', 'Rain', 'FFMC', 'DMC', 'DC', 'ISI', 'BUI', 'FWI']]  
            predictions = self.model.predict(data)
            return {"predictions": predictions.tolist()}
        except Exception as e:
            logging.error(f"Error during bulk prediction: {e}")
            raise

app = Flask(__name__)
api = ModelAPI(model_path='your_model.pkl', mongo_uri='mongodb://user:password@host:27017/database')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        prediction = api.single_prediction(data)
        return jsonify(prediction)
    except Exception as e:
        logging.error(f"Error in /predict route: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/bulk_predict', methods=['GET'])
def bulk_predict():
    try:
        predictions = api.bulk_prediction()
        return jsonify(predictions)
    except Exception as e:
        logging.error(f"Error in /bulk_predict route: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)