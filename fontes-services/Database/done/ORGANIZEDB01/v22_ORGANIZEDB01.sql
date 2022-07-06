--##Commit Cria a funcao [app].[fComplementoFormaPagamento].
PRINT 'Inicio do script v22. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB01;
CREATE FUNCTION [app].[fComplementoFormaPagamento](@formaPagamento	UNIQUEIDENTIFIER)
RETURNS TABLE
RETURN
(
	SELECT IC.chave, CF.valor
	FROM [fontes].[ComplementoFormaPagamento] CF
		INNER JOIN [fontes].[FormaPagamento] F ON F.codigo = CF.formaPagamento
		INNER JOIN [fontes].[ItemComplementoFormaPagamento] IC ON IC.codigo = CF.itemComplemento
	WHERE F.identificador = @formaPagamento
);
PRINT 'v22 - 001 - Criacao da funcao [app].[fComplementoFormaPagamento].';
PRINT 'Fim do script v22. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';