from flask import Flask, request, jsonify, render_template
#import pickle 
import heart_disease_predictor
import numpy as np


app=Flask(__name__)

@app.route('/')
def form():
    return render_template('index.html')

@app.route("/",methods=["POST","Get"])
def hello():
    if request.method=="POST":
        v1=request.form["AGE"]
        v2=request.form["Sex"]
        v3=request.form["Chest_Pain"]
        v4=request.form["RestingBP"]
        v5=request.form["Cholestrol"]
        v6=request.form["FastingBS"]
        v7=request.form["RestingECG"]
        v8=request.form["MaxHR"]
        v9=request.form["ExerciseAngina"]
        v10=request.form["OldPeak"]
        v11=request.form["St_Slope"]

        final_features=[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11]
        
        w=heart_disease_predictor.disease_predictor(final_features)
        
    return render_template("index.html",prediction=w)
if __name__=="__main__":
    app.run(debug=True)
