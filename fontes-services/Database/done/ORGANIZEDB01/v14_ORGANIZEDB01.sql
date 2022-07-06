--##Commit Cria a view [app].[vItemComplementoFormaPagamento];
PRINT 'Inicio do script v14. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB01;
CREATE VIEW [app].[vItemComplementoFormaPagamento]
AS
SELECT chave, tipagem, infoConversao FROM fontes.ItemComplementoFormaPagamento;
PRINT 'v14 - 001 - Criacao da view [app].[vItemComplementoFormaPagamento].';
PRINT 'Fim do script v14. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';