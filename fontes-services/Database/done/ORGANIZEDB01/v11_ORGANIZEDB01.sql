--##Commit Cria a procedure [app].[insereTipoFormaPagamento];
PRINT 'Inicio do script v11. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB01;
IF EXISTS(SELECT TOP 1 1 FROM sys.procedures WHERE name = 'insereTipoFormaPagamento' AND schema_id = SCHEMA_ID('app'))
BEGIN
	DROP PROCEDURE [app].[insereTipoFormaPagamento]
	PRINT 'v11 - 001 - Exclusao da procedure [app].[insereTipoFormaPagamento].'
END;
CREATE PROCEDURE app.insereTipoFormaPagamento
	@nome				VARCHAR(100),
	@aceitaComplemento	BIT
AS
BEGIN
	SET NOCOUNT ON

	INSERT INTO fontes.TipoFormaPagamento
		(nome, aceitaComplemento)
	OUTPUT inserted.identificador
	VALUES
		(@nome, @aceitaComplemento)

	SET NOCOUNT OFF
END;
PRINT 'v11 - 002 - Criação da procedure [app].[insereTipoFormaPagamento].'
PRINT 'Fim do script v11. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';