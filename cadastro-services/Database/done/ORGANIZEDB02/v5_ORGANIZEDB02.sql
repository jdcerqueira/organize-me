--##Commit Cria tabela [cadastro].[Generos], e procedures de inclusao e exclusao e view de listagem;
PRINT 'Inicio do script v5. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB02;
CREATE TABLE [cadastro].[Generos](
    codigo          INT                 NOT NULL    IDENTITY        PRIMARY KEY,
    identificador   UNIQUEIDENTIFIER    NOT NULL    DEFAULT NEWID(),
    nome            VARCHAR(70)         NOT NULL    UNIQUE
);
PRINT 'v5 - 001 - Cria tabela [cadastro].[Generos].';
CREATE VIEW [app].[vGeneros]
AS
SELECT identificador, nome FROM [cadastro].[Generos];
PRINT 'v5 - 002 - Cria view [app].[vGeneros].';
CREATE PROCEDURE [app].[insereGenero]
    @nome   VARCHAR(70)
AS
BEGIN
    SET NOCOUNT ON

    INSERT INTO [cadastro].[Generos]
        (nome)
    OUTPUT inserted.identificador, inserted.nome
    VALUES
        (@nome)

    SET NOCOUNT OFF
END;
PRINT 'v5 - 003 - Cria procedure [app].[insereGenero].';
CREATE PROCEDURE [app].[apagaGenero]
    @genero   UNIQUEIDENTIFIER
AS
BEGIN
    SET NOCOUNT ON

    DELETE [cadastro].[Generos]
    OUTPUT deleted.identificador, deleted.nome
    WHERE identificador = @genero

    SET NOCOUNT OFF
END;
PRINT 'v5 - 004 - Cria procedure [app].[apagaGenero].';
PRINT 'Fim do script v5. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';