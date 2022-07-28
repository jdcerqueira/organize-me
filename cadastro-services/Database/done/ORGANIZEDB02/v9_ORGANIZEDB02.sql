--##Commit Cria insercoes de endereço: paises, estados, cidades, bairros e logradouros;
PRINT 'Inicio do script v9. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB02;

CREATE PROCEDURE [app].[inserePais]
    @nome   VARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON

    INSERT INTO [cadastro].[Paises]
        (nome)
    OUTPUT inserted.identificador
    VALUES
        (@nome)

    SET NOCOUNT OFF
END;
PRINT 'v9 - 001 - Cria procedure [app].[inserePais].';


CREATE PROCEDURE [app].[insereEstado]
    @nome   VARCHAR(100),
    @uf     CHAR(2),
    @pais   UNIQUEIDENTIFIER
AS
BEGIN
    SET NOCOUNT ON
    DECLARE @codPais INT = (SELECT codigo FROM [cadastro].[Paises] WHERE identificador = @pais)

    INSERT INTO [cadastro].[Estados]
        (nome, uf, pais)
    OUTPUT inserted.uf
    VALUES
        (@nome, @uf, @codPais)

    SET NOCOUNT OFF
END;
PRINT 'v9 - 002 - Cria procedure [app].[insereEstado].';

CREATE PROCEDURE [app].[insereCidade]
    @nome   VARCHAR(100),
    @uf     CHAR(2)
AS
BEGIN
    SET NOCOUNT ON
    DECLARE @codEstado INT = (SELECT codigo FROM [cadastro].[Estados] WHERE uf = @uf)

    INSERT INTO [cadastro].[Cidades]
        (nome, estado)
    OUTPUT inserted.identificador
    VALUES
        (@nome, @codEstado)

    SET NOCOUNT OFF
END;
PRINT 'v9 - 003 - Cria procedure [app].[insereCidade].';

CREATE PROCEDURE [app].[insereBairro]
    @nome   VARCHAR(100),
    @cidade UNIQUEIDENTIFIER
AS
BEGIN
    SET NOCOUNT ON
    DECLARE @codCidade INT = (SELECT codigo FROM [cadastro].[Cidades] WHERE identificador = @cidade)

    INSERT INTO [cadastro].[Bairros]
        (nome, cidade)
    OUTPUT inserted.identificador
    VALUES
        (@nome, @codCidade)

    SET NOCOUNT OFF
END;
PRINT 'v9 - 004 - Cria procedure [app].[insereBairro].';

CREATE PROCEDURE [app].[insereLogradouro]
    @cep            CHAR(9),
    @nome           VARCHAR(200),
    @complemento    VARCHAR(200),
    @bairro         UNIQUEIDENTIFIER
AS
BEGIN
    SET NOCOUNT ON
    DECLARE @codBairro INT = (SELECT codigo FROM [cadastro].[Bairros] WHERE identificador = @bairro)

    INSERT INTO [cadastro].[Logradouros]
        (cep, nome, complemento, bairro)
    OUTPUT inserted.cep
    VALUES
        (@cep, @nome, @complemento, @codBairro)

    SET NOCOUNT OFF
END;
PRINT 'v9 - 005 - Cria procedure [app].[insereLogradouro].';

PRINT 'Fim do script v9. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';