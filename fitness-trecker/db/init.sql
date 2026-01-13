CREATE TABLE fitness_data (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    steps INTEGER,
    heart_rate INTEGER,
    calories FLOAT,
    activity_type VARCHAR(50)
);