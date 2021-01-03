# file backend/server/apps/ml/income_classifier/random_forest.py
import joblib
import pandas as pd
import os

class RandomForestClassifier:
    def __init__(self):
        #path_to_artifacts = "../../research/"
        #self.values_fill_missing =  joblib.load(path_to_artifacts + "train_mode.joblib")
        #self.encoders = joblib.load(path_to_artifacts + "encoders.joblib")
        #self.model = joblib.load("model_light.pkl")
        filename = "model_light.pkl"
        filename = os.path.join(os.getcwd(),'apps\\ml\\income_classifier', filename)
        self.model=joblib.load(filename)

    def preprocessing(self, input_data):
        # JSON to pandas DataFrame
        input_data = pd.DataFrame(input_data)#, index=[0]
        
        return input_data

    def predict(self, input_data):
        pred = self.model.predict(input_data)
        return pred

    def postprocessing(self, input_data):
        #label = "<=50K"
        #if input_data[1] > 0.5:
        #    label = ">50K"
        return {"Classe": input_data, "status": "OK"}

    def compute_prediction(self, input_data):
        try:
            input_data = self.preprocessing(input_data)
            prediction = self.predict(input_data) # only one sample
            prediction = self.postprocessing(prediction)
        except Exception as e:
            return {"status": "Error", "message": str(e)}

        return prediction