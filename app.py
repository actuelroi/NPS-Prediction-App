from flask import Flask, render_template, request
import pandas as pd
import joblib


app = Flask(__name__)
pipeline = joblib.load("pipeline.pkl")


# Load dataset (optional, for customer lookup)
customers = pd.read_excel("merged_data.xlsx")

labels = {
    0: "Detractor",
    1: "Passive",
    2: "Promoter"
}

@app.route("/")
def home():
    return render_template(
        "index.html",
        customer_ids=customers.index.tolist()
    )



@app.route("/predict", methods=["POST"])
def predict():

    customer_id = request.form.get("customer_id")

    if customer_id != "":

        row = customers.iloc[int(customer_id)]

        X = row.drop(labels=["NPS_Label"], errors="ignore").to_frame().T

    else:
        X = pd.DataFrame([{

        "Gender": request.form["Gender"],

        "Partner": request.form["Partner"],

        "SeniorCitizen": request.form["SeniorCitizen"],

        "Dependents": request.form["Dependents"],

        "PhoneService": request.form["PhoneService"],

        "MultipleLines": request.form["MultipleLines"],

        "InternetService": request.form["InternetService"],

        "OnlineSecurity": request.form["OnlineSecurity"],

        "OnlineBackup": request.form["OnlineBackup"],

        "DeviceProtection": request.form["DeviceProtection"],

        "TechSupport": request.form["TechSupport"],

        "StreamingTV": request.form["StreamingTV"],

        "StreamingMovies": request.form["StreamingMovies"],

        "Contract": request.form["Contract"],

        "PaperlessBilling": request.form["PaperlessBilling"],

        "PaymentMethod": request.form["PaymentMethod"],

        "TenureMonths": int(request.form["TenureMonths"]),

        "MonthlyCharges": float(request.form["MonthlyCharges"]),

        "TotalCharges": float(request.form["TotalCharges"])

    }])
    prediction = pipeline.predict(X)[0]

    probabilities = pipeline.predict_proba(X)[0]

    return render_template(
        "index.html",
        prediction=labels[prediction],
        probabilities=zip(labels.values(), probabilities),
        customer_ids=customers.index.tolist()
    )




if __name__ == "__main__":
    app.run(debug=True)