import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(path):

    df = pd.read_csv(path)

    scaler = StandardScaler()

    df["Amount"] = scaler.fit_transform(
        df[["Amount"]]
    )

    X = df.drop("Class", axis=1)
    y = df["Class"]

    return X, y