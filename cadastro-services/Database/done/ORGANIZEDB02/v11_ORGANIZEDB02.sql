--##Commit Cria consulta de enderecos por CEP;
PRINT 'Inicio do script v11. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB02;
CREATE VIEW [app].[vEnderecos]
AS
SELECT
	P.nome	pais,
	E.uf	uf, E.nome estado,
	C.nome	cidade,
	B.nome	bairro,
	L.cep, L.nome logradouro, L.complemento
FROM [app].vPaises P
	CROSS APPLY [app].[fEstados](P.identificador) E
	CROSS APPLY [app].[fCidades](E.uf) C
	CROSS APPLY [app].[fBairros](C.identificador) B
	CROSS APPLY [app].[fLogradouros](B.identificador) L;
PRINT 'v11 - 001 - Cria view [app].[vEnderecos].';
PRINT 'Fim do script v11. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';