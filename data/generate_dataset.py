import pandas as pd
import random

rows = []

transaction_types = [
    "Online",
    "POS",
    "ATM"
]

merchant_categories = [
    "Electronics",
    "Grocery",
    "Food",
    "Luxury",
    "Travel"
]

device_types = [
    "Mobile",
    "Desktop",
    "Laptop"
]

locations = [
    "Bangalore",
    "Mumbai",
    "Delhi",
    "Chennai",
    "Hyderabad",
    "Pune"
]

for _ in range(10000):

    amount = random.randint(100, 50000)

    transaction_type = random.choice(
        transaction_types
    )

    merchant = random.choice(
        merchant_categories
    )

    device = random.choice(
        device_types
    )

    location = random.choice(
        locations
    )

    hour = random.randint(0, 23)

    customer_age = random.randint(
        18,
        70
    )

    transaction_frequency = random.randint(
        1,
        50
    )

    fraud = 0

    if (
        amount > 20000
        and hour > 22
        and transaction_frequency > 20
    ):
        fraud = 1

    rows.append([
        amount,
        transaction_type,
        merchant,
        device,
        location,
        hour,
        customer_age,
        transaction_frequency,
        fraud
    ])

df = pd.DataFrame(
    rows,
    columns=[
        "amount",
        "transaction_type",
        "merchant_category",
        "device_type",
        "location",
        "hour",
        "customer_age",
        "transaction_frequency",
        "is_fraud"
    ]
)

df.to_csv(
    "data/fraud_transactions.csv",
    index=False
)

print(
    "Dataset created successfully!"
)

print(df.head())