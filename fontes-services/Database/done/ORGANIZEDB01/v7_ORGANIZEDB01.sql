--##Commit Cria a view [app].[vBancos];
PRINT 'Inicio do script v7. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB01;
IF EXISTS(SELECT TOP 1 1 FROM sys.views WHERE name = 'vBancos' AND schema_id = SCHEMA_ID('app'))
BEGIN
	DROP VIEW [app].[vBancos]
	PRINT 'v7 - 001 - Exclusao da view [app].[vBancos].'
END;
CREATE VIEW [app].[vBancos]
AS
  SELECT codigo, nome FROM fontes.Bancos;
PRINT 'v7 - 002 - Criacao da view [app].[vBancos].';
PRINT 'Fim do script v7. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';