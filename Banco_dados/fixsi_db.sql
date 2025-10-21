-- ========================
-- BANCO DE DADOS
-- ========================
CREATE DATABASE IF NOT EXISTS fixsi_db;
USE fixsi_db;

-- Desativa verificação temporária de chaves estrangeiras
SET FOREIGN_KEY_CHECKS = 0;

-- ========================
-- PERFIL (base)
-- ========================
CREATE TABLE IF NOT EXISTS perfil (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    cpf VARCHAR(14) UNIQUE,
    telefone VARCHAR(15),
    data_nascimento DATE,
    tipo ENUM('profissional', 'cliente') NOT NULL,
    descricao TEXT,
    imagem VARCHAR(255) NULL,
    visivel BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (user_id) REFERENCES auth_user(id) ON DELETE CASCADE
);

-- ========================
-- CLIENTE
-- ========================
CREATE TABLE IF NOT EXISTS cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    perfil_id INT NOT NULL UNIQUE,
    endereco VARCHAR(255),
    cidade VARCHAR(100),
    estado VARCHAR(50),
    bio TEXT NULL,
    FOREIGN KEY (perfil_id) REFERENCES perfil(id) ON DELETE CASCADE
);

-- ========================
-- PROFISSIONAL
-- ========================
CREATE TABLE IF NOT EXISTS profissional (
    id INT AUTO_INCREMENT PRIMARY KEY,
    perfil_id INT NOT NULL UNIQUE,
    area_atuacao VARCHAR(100),
    experiencia TEXT,
    nota_media DECIMAL(3,2) DEFAULT 0.0,
    bio TEXT,
    imagem_portfolio VARCHAR(255) NULL,
    FOREIGN KEY (perfil_id) REFERENCES perfil(id) ON DELETE CASCADE
);

-- ========================
-- PORTFÓLIO (imagens e vídeos)
-- ========================
CREATE TABLE IF NOT EXISTS portfolio (
    id INT AUTO_INCREMENT PRIMARY KEY,
    profissional_id INT NOT NULL,
    tipo_midia ENUM('imagem', 'video') NOT NULL,
    arquivo VARCHAR(255) NOT NULL,
    titulo VARCHAR(100),
    descricao TEXT,
    data_envio DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (profissional_id) REFERENCES profissional(id) ON DELETE CASCADE
);

-- ========================
-- CATÁLOGO DE SERVIÇOS
-- ========================
CREATE TABLE IF NOT EXISTS servico_catalogo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE,
    categoria VARCHAR(100),
    descricao TEXT
);

-- ========================
-- SERVIÇOS
-- ========================
CREATE TABLE IF NOT EXISTS servico (
    id INT AUTO_INCREMENT PRIMARY KEY,
    profissional_id INT NOT NULL,
    catalogo_id INT NULL,
    titulo VARCHAR(100) NOT NULL,
    descricao TEXT,
    categoria VARCHAR(100),
    preco DECIMAL(8,2),
    imagem VARCHAR(255),
    aprovado BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (profissional_id) REFERENCES profissional(id) ON DELETE CASCADE,
    FOREIGN KEY (catalogo_id) REFERENCES servico_catalogo(id) ON DELETE SET NULL
);

-- ========================
-- AGENDAMENTOS
-- ========================
CREATE TABLE IF NOT EXISTS agendamento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    servico_id INT NOT NULL,
    cliente_id INT NOT NULL,
    data DATE NOT NULL,
    horario TIME NOT NULL,
    status ENUM('Agendado','Concluído','Cancelado') DEFAULT 'Agendado',
    valor DECIMAL(8,2),
    FOREIGN KEY (servico_id) REFERENCES servico(id) ON DELETE CASCADE,
    FOREIGN KEY (cliente_id) REFERENCES cliente(id) ON DELETE CASCADE
);

-- ========================
-- AVALIAÇÕES (BIDIRECIONAIS)
-- ========================
CREATE TABLE IF NOT EXISTS avaliacao (
    id INT AUTO_INCREMENT PRIMARY KEY,
    avaliador_id INT NOT NULL,
    avaliado_id INT NOT NULL,
    agendamento_id INT NULL,
    nota INT NOT NULL,
    comentario TEXT,
    data DATE DEFAULT (CURRENT_DATE),
    tipo_avaliador ENUM('cliente','profissional') NOT NULL,
    FOREIGN KEY (avaliador_id) REFERENCES perfil(id) ON DELETE CASCADE,
    FOREIGN KEY (avaliado_id) REFERENCES perfil(id) ON DELETE CASCADE,
    FOREIGN KEY (agendamento_id) REFERENCES agendamento(id) ON DELETE SET NULL
);

-- ========================
-- FERRAMENTAS
-- ========================
CREATE TABLE IF NOT EXISTS ferramenta (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    preco_diaria DECIMAL(8,2),
    imagem VARCHAR(255),
    disponivel BOOLEAN DEFAULT TRUE
);

-- ========================
-- ALUGUÉIS DE FERRAMENTAS
-- ========================
CREATE TABLE IF NOT EXISTS aluguel_ferramenta (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    ferramenta_id INT NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    valor_total DECIMAL(8,2),
    status ENUM('Ativo','Concluído','Cancelado') DEFAULT 'Ativo',
    FOREIGN KEY (cliente_id) REFERENCES cliente(id) ON DELETE CASCADE,
    FOREIGN KEY (ferramenta_id) REFERENCES ferramenta(id) ON DELETE CASCADE
);

-- ========================
-- PAGAMENTOS
-- ========================
CREATE TABLE IF NOT EXISTS pagamento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo_pagamento ENUM('servico', 'aluguel') NOT NULL,
    referencia_id INT NOT NULL,
    metodo ENUM('cartao', 'pix', 'boleto') NOT NULL,
    valor DECIMAL(8,2),
    data_pagamento DATETIME DEFAULT CURRENT_TIMESTAMP,
    status ENUM('Pendente','Concluído','Cancelado') DEFAULT 'Pendente'
);

-- ========================
-- MENSAGENS
-- ========================
CREATE TABLE IF NOT EXISTS mensagem (
    id INT AUTO_INCREMENT PRIMARY KEY,
    remetente_id INT NOT NULL,
    destinatario_id INT NOT NULL,
    texto TEXT,
    data_envio DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (remetente_id) REFERENCES perfil(id) ON DELETE CASCADE,
    FOREIGN KEY (destinatario_id) REFERENCES perfil(id) ON DELETE CASCADE
);

-- Reativa a verificação de chaves estrangeiras
SET FOREIGN_KEY_CHECKS = 1;
