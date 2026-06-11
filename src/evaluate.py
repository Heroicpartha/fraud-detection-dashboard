from preprocessing import preprocess_data

from sklearn.model_selection import train_test_split

from sklearn.metrics import classification_report

import joblib

# Load Data
X, y = preprocess_data(
    "data/creditcard.csv"
)

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Load Model
model = joblib.load(
    "models/fraud_model.pkl"
)

# Predict
pred = model.predict(X_test)

# Evaluation
print(
    classification_report(
        y_test,
        pred
    )
)