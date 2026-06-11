import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="fraud_detection",
    user="postgres",
    password="partha@123",
    port="5433"
)

cursor = conn.cursor()

print("Database Connected Successfully!")