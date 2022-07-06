--##Commit Cria as procedures [app].[insereItemComplementoFormaPagamento] e [app].[insereItemComplementoFormaPagamento];
PRINT 'Inicio do script v15. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB01;
CREATE PROCEDURE [app].[insereItemComplementoFormaPagamento]
    @chave VARCHAR(8000),
    @tipagem CHAR(30),
    @infoConversao VARCHAR(1024)
AS
BEGIN
    SET NOCOUNT ON

    INSERT INTO fontes.ItemComplementoFormaPagamento
        (chave, tipagem, infoConversao)
    OUTPUT inserted.chave, inserted.tipagem, inserted.infoConversao
    VALUES
        (@chave, @tipagem, @infoConversao)

    SET NOCOUNT OFF
END;
PRINT 'v15 - 001 - Criacao da procedure [app].[insereItemComplementoFormaPagamento].';
CREATE PROCEDURE [app].[apagaItemComplementoFormaPagamento]
    @chave VARCHAR(8000)
AS
BEGIN
    SET NOCOUNT ON

    DELETE fontes.ItemComplementoFormaPagamento
    OUTPUT deleted.chave, deleted.tipagem, deleted.infoConversao
    WHERE chave = @chave

    SET NOCOUNT OFF
END;
PRINT 'v15 - 002 - Criacao da procedure [app].[apagaItemComplementoFormaPagamento].';
PRINT 'Fim do script v15. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';