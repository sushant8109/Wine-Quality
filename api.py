from flask import Flask,request,jsonify
import numpy as np
import pickle

filename = "model.pkl"
model = pickle.load(open(filename, 'rb'))

app = Flask(__name__)


@app.route('/',methods=['GET'])
def home():
    return {"Welcome":"This is a Wine Quality ML model"}

@app.route('/predict',methods = ['POST'])
def predict():
    fixed_acidity = request.form['fixed_acidity']
    volatile_acidity = request.form['volatile_acidity']
    citric_acid = request.form['citric_acid']
    residual_sugar = request.form['residual_sugar']
    chlorides = request.form['chlorides']
    free_sulfur_dioxide = request.form['free_sulfur_dioxide']
    total_sulfur_dioxide = 	request.form['total_sulfur_dioxide']
    density = request.form['density']
    pH = request.form['pH']
    sulphates = request.form['sulphates']
    alcohol	= request.form['alcohol']
    X = np.array([[fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,
    total_sulfur_dioxide,density,pH,sulphates,alcohol]])
    prediction = int(model.predict(X)[0])
    output = {"Prediction" : prediction}
    return jsonify(output)

if __name__=='__main__':
    app.run(debug=True)
