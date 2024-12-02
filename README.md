# Sistema-de-Cadastro-de-Ve-culo
Desenvolvendo o site para cadastro de veiculo com a linguagem python, html e css.
Banco de dados desenvolvido:
CREATE TABLE veiculos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    placa VARCHAR(7) NOT NULL UNIQUE,
    modelo VARCHAR(100) NOT NULL,
    marca VARCHAR(50) NOT NULL,
    ano_fabricacao INT,
    tipo VARCHAR(30), -- Ex: Carro, Moto, Caminhão, etc.
    chassi VARCHAR(17) NOT NULL UNIQUE
);
INSERT INTO veiculos (placa, modelo, marca, ano_fabricacao) 
VALUES ('ABC1234', 'Fusca', 'Volkswagen', 1975, 'Carro',);
