-- Active: 1745342258940@@127.0.0.1@3306@esp_data
CREATE DATABASE esp_data;

USE esp_data;

CREATE TABLE sensor_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    temperature FLOAT,
    humidity FLOAT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);


