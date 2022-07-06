--##Commit Cria a procedure [app].[apagaTipoFormaPagamento];
PRINT 'Inicio do script v12. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB01;
IF EXISTS(SELECT TOP 1 1 FROM sys.procedures WHERE name = 'apagaTipoFormaPagamento' AND schema_id = SCHEMA_ID('app'))
BEGIN
	DROP PROCEDURE [app].[apagaTipoFormaPagamento]
	PRINT 'v12 - 001 - Exclusao da procedure [app].[apagaTipoFormaPagamento].'
END;
CREATE PROCEDURE app.apagaTipoFormaPagamento
	@identificador	UNIQUEIDENTIFIER
AS
BEGIN
	SET NOCOUNT ON

	DELETE fontes.TipoFormaPagamento
	OUTPUT deleted.identificador, deleted.nome, deleted.aceitaComplemento
	WHERE identificador = @identificador

	SET NOCOUNT OFF
END;
PRINT 'v12 - 002 - Criação da procedure [app].[apagaTipoFormaPagamento].'
PRINT 'Fim do script v12. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';