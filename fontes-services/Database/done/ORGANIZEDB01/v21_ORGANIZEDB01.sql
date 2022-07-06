--##Commit Cria as procedures de insercao e exclusao da tabela [fontes].[FormaPagamento];
PRINT 'Inicio do script v21. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB01;
CREATE PROCEDURE [app].[insereFormaPagamento]
	@banco			INT,
	@tipoPagamento	UNIQUEIDENTIFIER,
	@nome			VARCHAR(100)
AS
BEGIN
	SET NOCOUNT ON

	DECLARE @codTipoPagamento	INT = (SELECT codigo FROM [fontes].[TipoFormaPagamento] WHERE identificador = @tipoPagamento)

	INSERT INTO [fontes].[FormaPagamento]
		(banco, tipoPagamento, nome)
	OUTPUT inserted.identificador, inserted.nome
	VALUES
		(@banco, @codTipoPagamento, @nome)

	SET NOCOUNT OFF
END;
PRINT 'v21 - 001 - Criacao da procedure [app].[insereFormaPagamento].';
CREATE PROCEDURE [app].[apagaFormaPagamento]
	@formaPagamento	UNIQUEIDENTIFIER
AS
BEGIN
	SET NOCOUNT ON

	DELETE [fontes].[FormaPagamento]
	OUTPUT deleted.identificador, deleted.nome
	WHERE identificador = @formaPagamento

	SET NOCOUNT OFF
END;
PRINT 'v21 - 002 - Criacao da procedure [app].[apagaFormaPagamento].';
PRINT 'Fim do script v21. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';