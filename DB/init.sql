CREATE USER IF NOT EXISTS 'api' IDENTIFIED BY 'apipassword';

CREATE DATABASE IF NOT EXISTS hubeducacional;

GRANT ALL PRIVILEGES ON hubeducacional.* TO 'api';

USE hubeducacional;

CREATE TABLE IF NOT EXISTS aluno(
    registro INTEGER PRIMARY KEY AUTO_INCREMENT,
    user VARCHAR(10) NOT NULL UNIQUE,
    senha VARCHAR(100) NOT NULL,
    nome VARCHAR(70) NOT NULL
);

CREATE TABLE IF NOT EXISTS doc_estudos(
    tema VARCHAR(100) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    area_conhecimento VARCHAR(20) NOT NULL,
    fonte VARCHAR(50) NOT NULL,
    file_path VARCHAR(100) PRIMARY KEY,
    registro INTEGER,
    FOREIGN KEY (registro) REFERENCES aluno(registro)
);