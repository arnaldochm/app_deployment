from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import pickle
from myvalidation import data_validation


app = Flask(__name__)

@app.route('/') #Ruta Madre
def hello():
    return 'Hello World'

@app.route('/predict/<argument1>/<argument2>/<argument3>/<argument4>/<argument5>/<argument6>/<argument7>/<argument8>')
def predict(argument1,argument2,argument3,argument4,argument5,argument6,argument7,argument8):
    
    country_of_origin   = str(argument1)
    variety             = str(argument2)
    aroma               = float(argument3)
    aftertaste          = float(argument4)
    acidity	            = float(argument5)
    body                = float(argument6)
    balance	            = float(argument7)
    moisture            = float(argument8)

    pred_array = np.array([[country_of_origin, variety, aroma, aftertaste, acidity, body, balance, moisture]])

    df_api = pd.DataFrame(data=pred_array, columns=['country_of_origin', 'variety', 'aroma', 'aftertaste', 'acidity', 'body', 'balance', 'moisture'])

    if not data_validation(df_api):
        return 'Could not processed the prediction'

    try:
        prediction = list(model.predict(df_api))
        return jsonify({'prediction':prediction})
    except:
        return 'Could not processed the prediction'



if __name__ == '__main__':

    file_name = './coffee_model.pkl'

    model = pickle.load(open(file_name, 'rb'))

    app.run(debug = True)


