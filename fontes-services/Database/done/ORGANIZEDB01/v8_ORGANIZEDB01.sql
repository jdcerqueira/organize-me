--##Commit Cria a procedure [app].[apagaBanco];
PRINT 'Inicio do script v8. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB01;
IF EXISTS(SELECT TOP 1 1 FROM sys.procedures WHERE name = 'apagaBanco' AND schema_id = SCHEMA_ID('app'))
BEGIN
	DROP PROCEDURE [app].[apagaBanco]
	PRINT 'v8 - 001 - Exclusao da procedure [app].[apagaBanco].'
END;
CREATE PROCEDURE app.apagaBanco
	@codigo	INT
AS
BEGIN
	SET NOCOUNT ON

	DELETE fontes.Bancos OUTPUT deleted.codigo, deleted.nome WHERE codigo = @codigo

	SET NOCOUNT OFF
END;
PRINT 'v8 - 002 - Criacao da procedure [app].[apagaBanco].'
PRINT 'Fim do script v8. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';