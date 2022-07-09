--##Commit Cria tabelas de endereço: paises, estados, cidades, bairros e logradouros;
PRINT 'Inicio do script v7. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB02;

CREATE TABLE [cadastro].[Paises](
    codigo          INT                 NOT NULL    IDENTITY        PRIMARY KEY,
    identificador   UNIQUEIDENTIFIER    NOT NULL    DEFAULT NEWID(),
    nome            VARCHAR(100)        NOT NULL
);
PRINT 'v7 - 001 - Cria tabela [cadastro].[Paises].';
CREATE INDEX [IDX01] ON [cadastro].[Paises](identificador);
PRINT 'v7 - 002 - Cria indice [IDX01].[cadastro].[Paises].';
CREATE INDEX [IDX02] ON [cadastro].[Paises](nome);
PRINT 'v7 - 003 - Cria indice [IDX02].[cadastro].[Paises].';

CREATE TABLE [cadastro].[Estados](
    codigo          INT                 NOT NULL    IDENTITY        PRIMARY KEY,
    nome            VARCHAR(100)        NOT NULL,
    uf              CHAR(2)             NOT NULL    UNIQUE,
    pais            INT                 NOT NULL
);
PRINT 'v7 - 004 - Cria tabela [cadastro].[Estados].';
CREATE INDEX [IDX01] ON [cadastro].[Estados](nome);
PRINT 'v7 - 006 - Cria indice [IDX01].[cadastro].[Estados].';
CREATE INDEX [IDX02] ON [cadastro].[Estados](pais);
PRINT 'v7 - 007 - Cria indice [IDX02].[cadastro].[Estados].';
ALTER TABLE [cadastro].[Estados] ADD FOREIGN KEY (pais) REFERENCES [cadastro].[Paises](codigo);
PRINT 'v7 - 008 - Cria relacionamento [cadastro].[Estados] -> [cadastro].[Paises].';

CREATE TABLE [cadastro].[Cidades](
    codigo          INT                 NOT NULL    IDENTITY        PRIMARY KEY,
    identificador   UNIQUEIDENTIFIER    NOT NULL    DEFAULT NEWID(),
    nome            VARCHAR(100)        NOT NULL,
    estado          INT                 NOT NULL
);
PRINT 'v7 - 009 - Cria tabela [cadastro].[Cidades].';
CREATE INDEX [IDX01] ON [cadastro].[Cidades](identificador);
PRINT 'v7 - 010 - Cria indice [IDX01].[cadastro].[Cidades].';
CREATE INDEX [IDX02] ON [cadastro].[Cidades](estado);
PRINT 'v7 - 011 - Cria indice [IDX02].[cadastro].[Cidades].';
CREATE INDEX [IDX03] ON [cadastro].[Cidades](nome);
PRINT 'v7 - 012 - Cria indice [IDX03].[cadastro].[Cidades].';
ALTER TABLE [cadastro].[Cidades] ADD FOREIGN KEY (estado) REFERENCES [cadastro].[Estados](codigo);
PRINT 'v7 - 013 - Cria relacionamento [cadastro].[Cidades] -> [cadastro].[Estados].';

CREATE TABLE [cadastro].[Bairros](
    codigo          INT                 NOT NULL    IDENTITY        PRIMARY KEY,
    identificador   UNIQUEIDENTIFIER    NOT NULL    DEFAULT NEWID(),
    nome            VARCHAR(100)        NOT NULL,
    cidade          INT                 NOT NULL
);
PRINT 'v7 - 014 - Cria tabela [cadastro].[Bairros].';
CREATE INDEX [IDX01] ON [cadastro].[Bairros](identificador);
PRINT 'v7 - 015 - Cria indice [IDX01].[cadastro].[Bairros].';
CREATE INDEX [IDX02] ON [cadastro].[Bairros](cidade);
PRINT 'v7 - 016 - Cria indice [IDX02].[cadastro].[Bairros].';
CREATE INDEX [IDX03] ON [cadastro].[Bairros](nome);
PRINT 'v7 - 017 - Cria indice [IDX03].[cadastro].[Bairros].';
ALTER TABLE [cadastro].[Bairros] ADD FOREIGN KEY (cidade) REFERENCES [cadastro].[Cidades](codigo);
PRINT 'v7 - 018 - Cria relacionamento [cadastro].[Bairros] -> [cadastro].[Cidades].';

CREATE TABLE [cadastro].[Logradouros](
    cep         CHAR(9)        NOT NULL    PRIMARY KEY,
    bairro      INT            NOT NULL,
    nome        VARCHAR(200)   NOT NULL,
    complemento VARCHAR(200)   NOT NULL
);
PRINT 'v7 - 019 - Cria tabela [cadastro].[Logradouros].';
CREATE INDEX [IDX01] ON [cadastro].[Logradouros](bairro);
PRINT 'v7 - 020 - Cria indice [IDX01].[cadastro].[Logradouros].';
CREATE INDEX [IDX02] ON [cadastro].[Logradouros](nome);
PRINT 'v7 - 021 - Cria indice [IDX02].[cadastro].[Logradouros].';
ALTER TABLE [cadastro].[Logradouros] ADD FOREIGN KEY (bairro) REFERENCES [cadastro].[Bairros](codigo);
PRINT 'v7 - 022 - Cria relacionamento [cadastro].[Logradouros] -> [cadastro].[Bairros].';

PRINT 'Fim do script v6. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';