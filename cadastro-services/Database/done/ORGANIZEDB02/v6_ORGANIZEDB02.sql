--##Commit Cria tabela [cadastro].[Generos], e procedures de inclusao e exclusao e view de listagem;
PRINT 'Inicio do script v6. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB02;
CREATE TABLE [cadastro].[Responsaveis](
    codigo          INT                 NOT NULL    IDENTITY        PRIMARY KEY,
    identificador   UNIQUEIDENTIFIER    NOT NULL    DEFAULT NEWID(),
    genero          INT                 NOT NULL,
    nome            VARCHAR(70)         NOT NULL,
    data_nascimento DATE                NOT NULL
);
PRINT 'v6 - 001 - Cria tabela [cadastro].[Responsaveis].';
CREATE INDEX [IDX01] ON [cadastro].[Responsaveis](identificador)
PRINT 'v6 - 002 - Cria indice [IDX01] na tabela [cadastro].[Responsaveis].';
CREATE INDEX [IDX02] ON [cadastro].[Responsaveis](genero)
PRINT 'v6 - 003 - Cria indice [IDX02] na tabela [cadastro].[Responsaveis].';
CREATE INDEX [IDX03] ON [cadastro].[Responsaveis](nome)
PRINT 'v6 - 004 - Cria indice [IDX03] na tabela [cadastro].[Responsaveis].';
CREATE INDEX [IDX04] ON [cadastro].[Responsaveis](data_nascimento)
PRINT 'v6 - 005 - Cria indice [IDX04] na tabela [cadastro].[Responsaveis].';
ALTER TABLE [cadastro].[Responsaveis] ADD FOREIGN KEY (genero) REFERENCES [cadastro].[Generos](codigo);
PRINT 'v6 - 006 - Cria relacionamento [cadastro].[Responsaveis] -> [cadastro].[Generos].';

CREATE VIEW [app].[vResponsaveis]
AS
SELECT R.identificador, R.nome, R.data_nascimento, G.identificador genero, G.nome nomeGenero
FROM [cadastro].[Responsaveis] R
    INNER JOIN [cadastro].[Generos] G ON G.codigo = R.genero;
PRINT 'v6 - 007 - Cria view [app].[vResponsaveis].';

CREATE PROCEDURE [app].[insereResponsavel]
    @genero             UNIQUEIDENTIFIER,
    @nome               VARCHAR(100),
    @data_nascimento    DATE
AS
BEGIN
    SET NOCOUNT ON
    DECLARE @codGenero INT = (SELECT codigo FROM [cadastro].[Generos] WHERE identificador = @genero)

    INSERT INTO [cadastro].[Responsaveis]
        (genero, nome, data_nascimento)
    OUTPUT inserted.identificador, inserted.nome, inserted.data_nascimento
    VALUES
        (@codGenero, @nome, @data_nascimento)

    SET NOCOUNT OFF
END;
PRINT 'v6 - 008 - Cria procedure [app].[insereResponsavel].';

CREATE PROCEDURE [app].[apagaResponsavel]
    @responsavel   UNIQUEIDENTIFIER
AS
BEGIN
    SET NOCOUNT ON

    DELETE [cadastro].[Responsaveis]
    OUTPUT deleted.identificador, deleted.nome, deleted.data_nascimento
    WHERE identificador = @responsavel

    SET NOCOUNT OFF
END;
PRINT 'v6 - 009 - Cria procedure [app].[apagaResponsavel].';
PRINT 'Fim do script v6. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';