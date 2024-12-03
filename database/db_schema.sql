-- Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS db_ip;
USE db_ip;

-- Crear la tabla ip_analysis
CREATE TABLE IF NOT EXISTS ip_analysis (
    ip_address VARCHAR(45) PRIMARY KEY,
    country VARCHAR(100),
    city VARCHAR(100),
    latitude FLOAT,
    longitude FLOAT,
    risk_score INT,
    classification VARCHAR(15)
);
