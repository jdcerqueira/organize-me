--##Commit Cria procedures de insercao e exclusao da tabela [fontes].[ComplementoFormaPagamento].
PRINT 'Inicio do script v23. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB01;
CREATE PROCEDURE [app].[insereComplementoFormaPagamento]
	@formaPagamento	UNIQUEIDENTIFIER,
	@chave			VARCHAR(8000),
	@valor			VARCHAR(8000)
AS
BEGIN
	SET NOCOUNT ON
	
	DECLARE @codFormaPagamento 	INT = (SELECT codigo FROM [fontes].[FormaPagamento] WHERE identificador = @formaPagamento)
	DECLARE @codItemComplemento INT = (SELECT codigo FROM [fontes].[ItemComplementoFormaPagamento] WHERE chave = @chave)

	INSERT INTO [fontes].[ComplementoFormaPagamento]
		(formaPagamento, itemComplemento, valor)
	VALUES
		(@codFormaPagamento, @codItemComplemento, @valor)

	SET NOCOUNT OFF
END;
PRINT 'v23 - 001 - Criacao da procedure [app].[insereComplementoFormaPagamento].';
CREATE PROCEDURE [app].[apagaComplementoFormaPagamento]
	@formaPagamento	UNIQUEIDENTIFIER,
	@chave			VARCHAR(8000)
AS
BEGIN
	SET NOCOUNT ON
	
	DECLARE @codFormaPagamento 	INT = (SELECT codigo FROM [fontes].[FormaPagamento] WHERE identificador = @formaPagamento)
	DECLARE @codItemComplemento INT = (SELECT codigo FROM [fontes].[ItemComplementoFormaPagamento] WHERE chave = @chave)

	DELETE [fontes].[ComplementoFormaPagamento]
	OUTPUT deleted.valor
	WHERE formaPagamento = @codFormaPagamento
	AND itemComplemento = @codItemComplemento

	SET NOCOUNT OFF
END;
PRINT 'v23 - 002 - Criacao da procedure [app].[apagaComplementoFormaPagamento].';
PRINT 'Fim do script v23. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';