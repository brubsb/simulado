-- ===============================================
-- CRIAÇÃO DO BANCO DE DADOS
-- ===============================================

CREATE DATABASE saep_db;
USE saep_db;

-- ===============================================
-- TABELA: usuarios_usuario
-- (Modelo: Usuario)
-- ===============================================

CREATE TABLE usuarios_usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    cargo VARCHAR(50) NOT NULL
);

-- Inserção de dados
INSERT INTO usuarios_usuario (nome, username, senha, cargo) VALUES
('Bruna Barbosa', 'bruna', '123', 'Admin'),
('João Silva', 'joao', 'abc', 'Gerente'),
('Mariana Souza', 'mariana', 'senha123', 'Operador');

-- ===============================================
-- TABELA: produtos_produto
-- (Modelo: Produto)
-- ===============================================

CREATE TABLE produtos_produto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    quantidade_estoque INTEGER DEFAULT 0,
    estoque_minimo INTEGER DEFAULT 0,
    descricao VARCHAR(255)
);

-- Inserção de dados
INSERT INTO produtos_produto
(nome, categoria, preco, quantidade_estoque, estoque_minimo, descricao)
VALUES
('Teclado Mecânico RGB', 'Periféricos', 249.90, 15, 5, 'Switch Blue RGB'),
('Mouse Gamer 7200 DPI', 'Periféricos', 129.90, 8, 3, 'RGB 7200 DPI'),
('Notebook Lenovo i5', 'Computadores', 3299.00, 3, 1, '8GB RAM, SSD 256GB');

-- ===============================================
-- TABELA: estoque_movimentacao
-- (Modelo: Movimentacao)
-- ===============================================

CREATE TABLE estoque_movimentacao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto_id INTEGER NOT NULL,
    tipo VARCHAR(10) NOT NULL,
    quantidade INTEGER NOT NULL,
    data DATE NOT NULL,
    FOREIGN KEY (produto_id)
        REFERENCES produtos_produto(id)
        ON DELETE CASCADE
);

-- Inserção de dados
INSERT INTO estoque_movimentacao (produto_id, tipo, quantidade, data) VALUES
(1, 'entrada', 10, '2025-05-01'),
(2, 'saida', 2, '2025-05-02'),
(3, 'entrada', 1, '2025-05-03');
