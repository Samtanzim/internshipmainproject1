CREATE TABLE transactions(

id SERIAL PRIMARY KEY,

amount INT,

velocity INT,

location_risk INT,

device_change INT,

fraud_prediction INT,

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);