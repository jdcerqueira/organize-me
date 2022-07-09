--##Commit Cria tabela [cadastro].[Categorias], e procedures de inclusao e exclusao e view de listagem;
PRINT 'Inicio do script v10. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB02;
CREATE TABLE [cadastro].[Categorias](
    codigo          INT                 NOT NULL    IDENTITY        PRIMARY KEY,
    identificador   UNIQUEIDENTIFIER    NOT NULL    DEFAULT NEWID() UNIQUE,
    nome            VARCHAR(100)        NOT NULL    UNIQUE
);
PRINT 'v10 - 001 - Cria tabela [cadastro].[Categorias].';

CREATE VIEW [app].[vCategorias]
AS
SELECT identificador categoria, nome
FROM [cadastro].[Categorias];
PRINT 'v10 - 002 - Cria view [app].[vCategorias].';

CREATE PROCEDURE [app].[insereCategoria]
    @nome VARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON

    INSERT INTO [cadastro].[Categorias]
        (nome)
    OUTPUT inserted.identificador, inserted.nome
    VALUES
        (@nome)

    SET NOCOUNT OFF
END;
PRINT 'v10 - 003 - Cria procedure [app].[insereCategoria].';

CREATE PROCEDURE [app].[apagaCategorias]
    @categoria UNIQUEIDENTIFIER
AS
BEGIN
    SET NOCOUNT ON

    DELETE [cadastro].[Categorias]
    OUTPUT deleted.identificador, deleted.nome
    WHERE identificador = @categoria

    SET NOCOUNT OFF
END;
PRINT 'v10 - 004 - Cria procedure [app].[apagaCategorias].';
PRINT 'Fim do script v10. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';