# 🚨 AI-Powered Fraud Detection System

An end-to-end Machine Learning-based Fraud Detection System that predicts fraudulent transactions, calculates fraud risk scores, stores transaction records in a PostgreSQL database, and provides an interactive analytics dashboard using Streamlit.

---

## 📌 Project Overview

This project uses a Machine Learning model to analyze transaction details and classify them as either:

- ✅ Genuine Transaction
- 🚨 Fraudulent Transaction

The system provides:

- Real-time fraud prediction
- Fraud probability scoring
- Risk assessment (Low / Medium / High)
- Transaction logging
- Interactive analytics dashboard
- Cloud database integration

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Machine Learning
- Scikit-Learn
- Random Forest Classifier

### Database
- PostgreSQL
- Neon PostgreSQL (Cloud)

### Dashboard & Visualization
- Streamlit
- Plotly

### Deployment
- GitHub
- Streamlit Cloud

---

## ✨ Features

### 🔍 Fraud Prediction
Predicts whether a transaction is fraudulent or genuine.

### 📊 Risk Assessment
Provides:
- Low Risk
- Medium Risk
- High Risk

based on fraud probability.

### 📈 Interactive Dashboard
Displays:
- Total Predictions
- Fraud Transactions
- Genuine Transactions
- Fraud Distribution
- Risk Distribution
- Fraud Trends

### 🚨 Top Risky Transactions
Shows the highest-risk transactions for quick analysis.

### 📋 Transaction History
Stores and displays transaction records from PostgreSQL.

### 📥 Report Generation
Download transaction data as CSV reports.

### ☁️ Cloud Deployment
Accessible online through Streamlit Cloud.

---

## 📂 Project Structure

```text
FRAUD_DETECTION_SYSTEM
│
├── api/
├── dashboard/
│   └── app.py
│
├── data/
│
├── models/
│   ├── business_fraud_model.pkl
│   └── encoders.pkl
│
├── src/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Heroicpartha/fraud-detection-dashboard.git

cd fraud-detection-dashboard
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate Environment:

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / Mac

```bash
source .venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ Database Setup

Create a PostgreSQL database.

Run:

```sql
CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    amount FLOAT,
    transaction_type VARCHAR(50),
    merchant_category VARCHAR(50),
    device_type VARCHAR(50),
    location VARCHAR(50),
    hour INT,
    customer_age INT,
    transaction_frequency INT,
    fraud_probability FLOAT,
    prediction INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🔐 Environment Variable

Create a Streamlit Secret or environment variable:

```text
DATABASE_URL=your_postgresql_connection_string
```

Example:

```text
postgresql://username:password@host/database?sslmode=require
```

---

## ▶️ Running the Application

Start Streamlit Dashboard:

```bash
streamlit run dashboard/app.py
```

Open browser:

```text
http://localhost:8501
```

---

## 📊 Dashboard Screens

### Dashboard Includes

- KPI Cards
- Fraud Risk Assessment
- Fraud Distribution Pie Chart
- Risk Distribution Chart
- Fraud Trend Analysis
- Top Risky Transactions
- Recent Transactions Table

---

## 🚀 Deployment

### GitHub

Push project to GitHub:

```bash
git add .
git commit -m "Project Update"
git push
```

### Streamlit Cloud

1. Connect GitHub Repository
2. Add DATABASE_URL in Secrets
3. Deploy Application

---

## 🎯 Future Scope

- Advanced ML Models
- User Authentication
- Email Alerts
- Real-time Transaction Streaming
- Fraud Heatmap Visualization

---

## 👨‍💻 Author

### Parthasarathi Mohanty

B.Tech CSE (IoT)  
Vellore Institute of Technology

**Skills:** Python, SQL, Power BI, Machine Learning, Data Analytics, Full Stack Development

GitHub:
https://github.com/Heroicpartha

LinkedIn:
(Add your LinkedIn profile link)

---

## ⭐ If you found this project useful, consider giving it a star on GitHub.