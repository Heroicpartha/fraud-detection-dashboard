import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px
import joblib


# ==================================
# PAGE CONFIGURATION
# ==================================

st.set_page_config(
    page_title="AI Fraud Detection Dashboard",
    page_icon="🚨",
    layout="wide"
)

# Auto Refresh Every 5 Seconds


# ==================================
# LOAD MODELS
# ==================================

business_model = joblib.load(
    "models/business_fraud_model.pkl"
)

encoders = joblib.load(
    "models/encoders.pkl"
)

# ==================================
# DATABASE CONNECTION
# ==================================

import os

conn = psycopg2.connect(
    os.environ["DATABASE_URL"]
)

# ==================================
# LOAD DATA
# ==================================

df = pd.read_sql(
    "SELECT * FROM transactions",
    conn
)

if not df.empty:
    df["created_at"] = pd.to_datetime(
        df["created_at"]
    )

# ==================================
# TITLE
# ==================================

st.markdown(
    """
    <h1 style='text-align:center;color:#FF4B4B;'>
    🚨 AI-Powered Fraud Detection Dashboard
    </h1>
    """,
    unsafe_allow_html=True
)

st.info(
    "Enter transaction details below to assess fraud risk in real time."
)

# ==================================
# FRAUD PREDICTION FORM
# ==================================

st.subheader("🔍 Check Transaction Fraud Risk")

col1, col2 = st.columns(2)

with col1:

    amount = st.number_input(
        "Transaction Amount",
        min_value=0.0,
        value=1000.0
    )

    transaction_type = st.selectbox(
        "Transaction Type",
        ["Online", "POS", "ATM"]
    )

    merchant_category = st.selectbox(
        "Merchant Category",
        [
            "Electronics",
            "Grocery",
            "Food",
            "Luxury",
            "Travel"
        ]
    )

    device_type = st.selectbox(
        "Device Type",
        [
            "Mobile",
            "Desktop",
            "Laptop"
        ]
    )

with col2:

    location = st.selectbox(
        "Location",
        [
            "Bangalore",
            "Mumbai",
            "Delhi",
            "Chennai",
            "Hyderabad",
            "Pune"
        ]
    )

    hour = st.slider(
        "Transaction Hour",
        0,
        23,
        12
    )

    customer_age = st.slider(
        "Customer Age",
        18,
        70,
        25
    )

    transaction_frequency = st.slider(
        "Transaction Frequency",
        1,
        50,
        5
    )

# ==================================
# PREDICTION BUTTON
# ==================================

if st.button("🚨 Check Fraud"):

    features = [

        amount,

        encoders["transaction_type"].transform(
            [transaction_type]
        )[0],

        encoders["merchant_category"].transform(
            [merchant_category]
        )[0],

        encoders["device_type"].transform(
            [device_type]
        )[0],

        encoders["location"].transform(
            [location]
        )[0],

        hour,
        customer_age,
        transaction_frequency
    ]

    prediction = int(
        business_model.predict(
            [features]
        )[0]
    )

    fraud_probability = business_model.predict_proba(
        [features]
    )[0][1]

    # Save Prediction
    cursor = conn.cursor()

    cursor.execute(
    """
    INSERT INTO transactions(
        amount,
        transaction_type,
        merchant_category,
        device_type,
        location,
        hour,
        customer_age,
        transaction_frequency,
        fraud_probability,
        prediction
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """,
    (
        amount,
        transaction_type,
        merchant_category,
        device_type,
        location,
        hour,
        customer_age,
        transaction_frequency,
        float(fraud_probability),
        prediction
    )
)

    conn.commit()

    risk_percent = fraud_probability * 100

    st.markdown("---")

    st.subheader("📊 Risk Assessment")

    if risk_percent >= 80:

        st.error(
            f"🚨 HIGH RISK : {risk_percent:.2f}%"
        )

    elif risk_percent >= 50:

        st.warning(
            f"⚠️ MEDIUM RISK : {risk_percent:.2f}%"
        )

    else:

        st.success(
            f"✅ LOW RISK : {risk_percent:.2f}%"
        )

    st.progress(float(fraud_probability))

    m1, m2 = st.columns(2)

    with m1:

        st.metric(
            "Fraud Risk Score",
            f"{risk_percent:.2f}%"
        )

    with m2:

        st.metric(
            "Prediction",
            "Fraud" if prediction == 1 else "Genuine"
        )

# ==================================
# REFRESH DATA
# ==================================

df = pd.read_sql(
    "SELECT * FROM transactions",
    conn
)

if not df.empty:
    df["created_at"] = pd.to_datetime(
        df["created_at"]
    )

# ==================================
# KPI CARDS
# ==================================

st.markdown("---")

k1, k2, k3 = st.columns(3)

with k1:

    st.metric(
        "Total Predictions",
        len(df)
    )

with k2:

    st.metric(
        "Fraud Transactions",
        len(
            df[df["prediction"] == 1]
        )
    )

with k3:

    st.metric(
        "Genuine Transactions",
        len(
            df[df["prediction"] == 0]
        )
    )

# ==================================
# ALERT
# ==================================

st.subheader("🚨 Top Risky Transactions")

if not df.empty:

    risky_df = df.sort_values(
        by="fraud_probability",
        ascending=False
    )

    risky_df["Fraud Risk %"] = (
        risky_df["fraud_probability"] * 100
    ).round(2)

    st.dataframe(
        risky_df[
            [
                "amount",
                "transaction_type",
                "merchant_category",
                "location",
                "Fraud Risk %",
                "prediction",
                "created_at"
            ]
        ].head(5),
        use_container_width=True
    )
# ==================================
# CHART DATA
# ==================================

chart_df = pd.DataFrame({
    "Type": [
        "Genuine",
        "Fraud"
    ],
    "Count": [
        len(df[df["prediction"] == 0]),
        len(df[df["prediction"] == 1])
    ]
})

# ==================================
# PIE CHART
# ==================================

st.subheader("🥧 Fraud Distribution")

fig_pie = px.pie(
    chart_df,
    values="Count",
    names="Type"
)

st.plotly_chart(
    fig_pie,
    use_container_width=True
)
st.subheader("🎯 Risk Score Distribution")

fig_hist = px.histogram(
    df,
    x="fraud_probability",
    nbins=20,
    title="Fraud Probability Distribution"
)

st.plotly_chart(
    fig_hist,
    use_container_width=True
)

# ==================================
# BAR CHART
# ==================================

st.subheader("📊 Transaction Distribution")

fig_bar = px.bar(
    chart_df,
    x="Type",
    y="Count"
)

st.plotly_chart(
    fig_bar,
    use_container_width=True
)

# ==================================
# FRAUD TREND
# ==================================

if not df.empty:

    st.subheader(
        "📈 Fraud Trend Over Time"
    )

    trend_df = (
        df.groupby(
            df["created_at"].dt.date
        )["prediction"]
        .sum()
        .reset_index()
    )

    trend_df.columns = [
        "Date",
        "Fraud Count"
    ]

    fig_line = px.line(
        trend_df,
        x="Date",
        y="Fraud Count",
        markers=True
    )

    st.plotly_chart(
        fig_line,
        use_container_width=True
    )

# ==================================
# TRANSACTION TABLE
# ==================================

st.subheader(
    "📋 Recent Transactions"
)

if not df.empty:

    display_df = df.copy()

    display_df["Result"] = display_df[
        "prediction"
    ].apply(
        lambda x:
        "🔴 Fraud"
        if x == 1
        else "🟢 Genuine"
    )

    display_df["Fraud Risk %"] = (
        display_df["fraud_probability"] * 100
    ).round(2)

    display_df = display_df[
        [
            "amount",
            "transaction_type",
            "merchant_category",
            "location",
            "Fraud Risk %",
            "Result",
            "created_at"
        ]
    ]

    st.dataframe(
        display_df.sort_values(
            by="created_at",
            ascending=False
        ),
        use_container_width=True
    )

else:

    st.info(
        "No transactions available."
    )


# ==================================
# DOWNLOAD REPORT
# ==================================

csv = df.to_csv(
    index=False
)

st.download_button(
    "⬇ Download Report",
    csv,
    "fraud_report.csv",
    "text/csv"
)

# ==================================
# FOOTER
# ==================================

st.markdown("---")

st.markdown(
    "Built with ❤️ using Python, Random Forest, PostgreSQL, Streamlit and Plotly"
)