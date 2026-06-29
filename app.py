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

        X = row.drop("NPS_Label").to_frame().T

    else:

        X = pd.DataFrame([{

            "SeniorCitizen":
                int(request.form["SeniorCitizen"]),

            "TenureMonths":
                int(request.form["TenureMonths"]),

            "Contract":
                request.form["Contract"],

            "MonthlyCharges":
                float(request.form["MonthlyCharges"]),

            "MultipleLines":
                request.form["MultipleLines"],

            "InternetService":
                request.form["InternetService"],

            "OnlineSecurity":
                request.form["OnlineSecurity"],

            "StreamingTV":
                request.form["StreamingTV"],

            "StreamingMovies":
                request.form["StreamingMovies"],

            "PaperlessBilling":
                request.form["PaperlessBilling"],

            "PaymentMethod":
                request.form["PaymentMethod"]

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