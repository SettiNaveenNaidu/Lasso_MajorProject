from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('lasso.pkl', 'rb'))
@app.route('/',methods=['GET'])

def Home():
    return render_template('lasso.html')

standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Feed = float(request.form['Feed'])
        Speed=float(request.form['Speed'])
        Doc=float(request.form['Doc'])
        Woc=float(request.form['Woc'])
        Dir=float(request.form['Dir'])
        Coolant=float(request.form['Coolant'])
        
        prediction=model.predict([[Feed,Speed,Doc,Woc,Dir,Coolant]])
        output=round(prediction[0],6)
        
        return render_template('lasso.html',prediction_text="The value of roughness is {}".format(output))
    else:
        return render_template('lasso.html')

if __name__=="__main__":
    app.run(debug=True)
