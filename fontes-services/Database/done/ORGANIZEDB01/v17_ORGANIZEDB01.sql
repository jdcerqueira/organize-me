--##Commit Cria a view [app].[vTemplateComplementoFormaPagamento] e a function [app].[fTemplateItemComplementoFormaPagamento];
PRINT 'Inicio do script v17. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB01;
CREATE VIEW [app].[vTemplateComplementoFormaPagamento]
AS
SELECT identificador, descricao FROM [fontes].[TemplateComplementoFormaPagamento];
PRINT 'v17 - 001 - Criacao da view [app].[vTemplateComplementoFormaPagamento].';
CREATE FUNCTION [app].[fTemplateItemComplementoFormaPagamento](@template UNIQUEIDENTIFIER)
RETURNS TABLE
AS RETURN(
	SELECT I.chave
	FROM fontes.TemplateComplementoFormaPagamento T
		INNER JOIN fontes.TemplateItemComplementoFormaPagamento TI ON TI.template = T.codigo
		INNER JOIN fontes.ItemComplementoFormaPagamento I ON I.codigo = TI.chave
	WHERE T.identificador = @template
);
PRINT 'v17 - 002 - Criacao da function [app].[vTemplateItemComplementoFormaPagamento].';
PRINT 'Fim do script v17. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';