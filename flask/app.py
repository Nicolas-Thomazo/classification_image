import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import joblib
import pandas as pd
app = Flask(__name__)

filename = "knn_light.pkl"
model=joblib.load(filename)

def number_to_class(number):
    classes = ["red soil","cotton crop","grey soil","damp grey soil","soil with vegetation stubble","mixture class (all types present)","very damp grey soil"]
    return classes[number-1]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    print("on va predire")
    print(request.form)
    print(type(request))
    int_features = [int(x) for x in request.form.values()]
    print(int_features)
    #final_features = [np.array(int_features)]
    final_features = {
            "col1": int_features[0],
            "col2": int_features[1],
            "col3": int_features[2],
            "col4":int_features[3]
        }
    final_features = pd.DataFrame(final_features, index=[0])
    prediction = model.predict(final_features)
    output = prediction[0]#round(prediction[0], 2)
    classe = number_to_class(output)

    proba_prediction = model.predict_proba(final_features)
    max_proba =np.max(proba_prediction)
    max_proba = round(max_proba,2)

    return render_template('index.html', prediction_text=f'Le pixel correspond à {classe} (classe {output}) avec un probabilité de {max_proba}')

#def predict2():
 #   return "ok"

@app.route('/predict_api',methods=['POST'])
def ppp():
    print(request.form)
    return "ok"

if __name__ == "__main__":
    app.run(debug=True)