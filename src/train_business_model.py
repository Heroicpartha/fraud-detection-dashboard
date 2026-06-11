import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report

# Load Dataset
df = pd.read_csv(
    "data/fraud_transactions.csv"
)

# Create Encoders
encoders = {}

categorical_columns = [
    "transaction_type",
    "merchant_category",
    "device_type",
    "location"
]

for col in categorical_columns:

    le = LabelEncoder()

    df[col] = le.fit_transform(
        df[col]
    )

    encoders[col] = le

# Save Encoders
joblib.dump(
    encoders,
    "models/encoders.pkl"
)

# Features and Target

X = df.drop(
    "is_fraud",
    axis=1
)

y = df["is_fraud"]

# Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

# Save Model

joblib.dump(
    model,
    "models/business_fraud_model.pkl"
)

# Evaluation

pred = model.predict(
    X_test
)

print(
    classification_report(
        y_test,
        pred
    )
)

print(
    "\nBusiness Fraud Model Trained Successfully!"
)