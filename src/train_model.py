from preprocessing import preprocess_data

from sklearn.model_selection import train_test_split

from xgboost import XGBClassifier

import joblib
X, y = preprocess_data(
    "data/creditcard.csv"
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = XGBClassifier()

model.fit(X_train, y_train)

joblib.dump(
    model,
    "models/fraud_model.pkl"
)