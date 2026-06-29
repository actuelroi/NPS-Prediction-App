# NPS-Prediction-App
This repository guides you through the process launch the flask app for the challenge

# NPS Prediction System

A machine learning web application that predicts a customer's **Net Promoter Score (NPS) category** based on customer information.

The application allows a retention manager to:

- Predict whether a customer is a **Detractor**, **Passive**, or **Promoter**
- View the prediction probabilities for each NPS category
- Understand the main factors influencing the prediction
- (Optional) Submit a customer interaction note to see how the prediction changes

---

## Project Structure

```
NPS-Prediction-App/
│
├── app.py                  # Flask application
├── train_model.py          # Train and save the model
├── pipeline.pkl            # Trained ML pipeline
├── customer_data.csv       # Dataset
├── requirements.txt
├── README.md
│
├── templates/
│     └── index.html
│
├── static/
│     └── style.css
│
└── screenshots/
```

---

## Requirements

- Python 3.10 or later
- Git
- Visual Studio Code (recommended)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/actu/NPS-Prediction-App.git
```

Go to the project folder:

```bash
cd NPS-Prediction-App
```

---

### 2. Create a virtual environment

#### Windows

```bash
python -m venv venv
```

#### macOS / Linux

```bash
python3 -m venv venv
```

---

### 3. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

You should now see:

```
(venv)
```

at the beginning of your terminal.

---

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is unavailable, install the required packages manually:

```bash
pip install flask pandas numpy scikit-learn xgboost joblib matplotlib shap openpyxl
```

---

## Running the Application

Start the Flask server:

```bash
python app.py
```

You should see something similar to:

```
 * Running on http://127.0.0.1:5000
```

Open your browser and navigate to:

```
http://127.0.0.1:5000
```

---

## Training the Model

If you want to retrain the model:

```bash
python train_model.py
```

This script will:

- Load the dataset
- Preprocess the features
- Train the machine learning model
- Save the trained model as `pipeline.pkl`

---

## Features

The application includes:

- Customer attribute input
- Existing customer selection
- NPS prediction
- Prediction probabilities
- Customer-specific explanation of the prediction
- Optional customer verbatim analysis

---

## Technologies Used

- Python
- Flask
- scikit-learn
- XGBoost / TabPFN
- Pandas
- NumPy
- HTML
- CSS

---

## Example Output

```
Prediction

Promoter

Prediction Probabilities

Detractor : 3%

Passive : 14%

Promoter : 83%
```

---

## Repository

```text
https://github.com/actu/NPS-Prediction-App
```

---

## Author

Developed as part of a Machine Learning project for customer NPS prediction.
