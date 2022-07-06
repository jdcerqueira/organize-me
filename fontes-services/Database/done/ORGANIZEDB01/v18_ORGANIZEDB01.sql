--##Commit Cria as procedures de controle do template (insere e apaga), para templates e itens;
PRINT 'Inicio do script v18. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB01;

CREATE PROCEDURE [app].[insereTemplateComplementoFormaPagamento]
	@descricao	VARCHAR(100)
AS
BEGIN
	SET NOCOUNT ON

	INSERT INTO [fontes].[TemplateComplementoFormaPagamento]
		(descricao)
	OUTPUT inserted.identificador, inserted.descricao
	VALUES
		(@descricao)

	SET NOCOUNT OFF
END;
PRINT 'v18 - 001 - Criacao da procedure [app].[insereTemplateComplementoFormaPagamento].';
CREATE PROCEDURE [app].[insereTemplateItemComplementoFormaPagamento]
	@chave		VARCHAR(8000),
	@template	UNIQUEIDENTIFIER
AS
BEGIN
	SET NOCOUNT ON

	DECLARE @codChave 		INT = (SELECT codigo FROM [fontes].[ItemComplementoFormaPagamento] WHERE chave = @chave)
	DECLARE @codTemplate	INT = (SELECT codigo FROM [fontes].[TemplateComplementoFormaPagamento] WHERE identificador = @template)

	INSERT INTO [fontes].[TemplateItemComplementoFormaPagamento]
		(chave, template)
	VALUES
		(@codChave, @codTemplate)

	SET NOCOUNT OFF
END;
PRINT 'v18 - 002 - Criacao da procedure [app].[insereTemplateComplementoFormaPagamento].';
CREATE PROCEDURE [app].[apagaTemplateItemComplementoFormaPagamento]
	@chave		VARCHAR(8000),
	@template	UNIQUEIDENTIFIER
AS
BEGIN
	SET NOCOUNT ON

	DECLARE @codChave 		INT = (SELECT codigo FROM [fontes].[ItemComplementoFormaPagamento] WHERE chave = @chave)
	DECLARE @codTemplate	INT = (SELECT codigo FROM [fontes].[TemplateComplementoFormaPagamento] WHERE identificador = @template)

	DELETE [fontes].[TemplateItemComplementoFormaPagamento]
	WHERE chave = @codChave
		AND template = @codTemplate

	SET NOCOUNT OFF
END;
PRINT 'v18 - 003 - Criacao da procedure [app].[apagaTemplateItemComplementoFormaPagamento].';
CREATE PROCEDURE [app].[apagaTemplateComplementoFormaPagamento]
	@template	UNIQUEIDENTIFIER
AS
BEGIN
	SET NOCOUNT ON

	DELETE [fontes].[TemplateComplementoFormaPagamento]
	OUTPUT deleted.identificador, deleted.descricao
	WHERE identificador = @template

	SET NOCOUNT OFF
END;
PRINT 'v18 - 004 - Criacao da procedure [app].[apagaTemplateComplementoFormaPagamento].';
PRINT 'Fim do script v18. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';