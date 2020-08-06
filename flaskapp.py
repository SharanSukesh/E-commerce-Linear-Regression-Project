import pickle
import numpy as np
from flask import Flask, redirect, url_for,render_template, request, jsonify

app = Flask(__name__)
model = pickle.load(open('lrmodel.pkl','rb'))

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/<name>")
def user(name):
    return render_template("index.html",content=name)

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

@app.route("/predict",methods=['POST'])
def predict():
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0],2)
    return render_template('index.html',prediction_text='Predicted yearly amount spent : $ {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)