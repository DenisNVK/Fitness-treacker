import time
import random
import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    host="db",
    database="fitness",
    user="fitness",
    password="fitness"
)

activities = ["walking", "running", "cycling", "rest"]

cursor = conn.cursor()

while True:
    timestamp = datetime.now()
    activity = random.choice(activities)

    if activity == "rest":
        steps = 0
        heart_rate = random.randint(60, 75)
        calories = random.uniform(0.5, 1.0)
    elif activity == "walking":
        steps = random.randint(20, 60)
        heart_rate = random.randint(80, 100)
        calories = random.uniform(2.0, 4.0)
    elif activity == "running":
        steps = random.randint(80, 120)
        heart_rate = random.randint(120, 160)
        calories = random.uniform(6.0, 10.0)
    else:
        steps = 0
        heart_rate = random.randint(100, 140)
        calories = random.uniform(5.0, 8.0)

    cursor.execute(
        """
        INSERT INTO fitness_data (timestamp, steps, heart_rate, calories, activity_type)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (timestamp, steps, heart_rate, calories, activity)
    )

    conn.commit()
    print("Inserted:", timestamp, activity)
    time.sleep(1)