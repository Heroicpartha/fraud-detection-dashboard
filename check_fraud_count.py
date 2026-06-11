import pandas as pd

df = pd.read_csv("data/fraud_transactions.csv")

print(df["is_fraud"].value_counts())