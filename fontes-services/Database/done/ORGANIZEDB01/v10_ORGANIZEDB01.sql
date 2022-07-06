--##Commit Cria a view [app].[vTipoFormaPagamento];
PRINT 'Inicio do script v10. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB01;
IF EXISTS(SELECT TOP 1 1 FROM sys.views WHERE name = 'vTipoFormaPagamento' AND schema_id = SCHEMA_ID('app'))
BEGIN
	DROP VIEW [app].[vTipoFormaPagamento]
	PRINT 'v10 - 001 - Exclusao da view [app].[vTipoFormaPagamento].'
END;
CREATE VIEW app.vTipoFormaPagamento
AS
SELECT identificador, nome, aceitaComplemento FROM [fontes].[TipoFormaPagamento];
PRINT 'v10 - 002 - Criação da view [app].[vTipoFormaPagamento].'
PRINT 'Fim do script v10. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';