--##Commit Cria function para consulta de estabelecimentos por categoria;
PRINT 'Inicio do script v13. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB02;

CREATE FUNCTION [app].[fEstabelecimentos]
(
	@categoria	UNIQUEIDENTIFIER
)
RETURNS TABLE
RETURN(
	SELECT E.identificador estabelecimento, E.nome
	FROM [cadastro].[Estabelecimentos] E
		INNER JOIN [cadastro].[Categorias] C ON C.codigo = E.categoria
	WHERE C.identificador = @categoria
);
PRINT 'v13 - 001 - Cria function [app].[fEstabelecimentos].'
PRINT 'Fim do script v13. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';