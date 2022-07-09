--##Commit Cria views e functions de endereço: paises, estados, cidades, bairros e logradouros;
PRINT 'Inicio do script v8. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB02;

CREATE VIEW [app].[vPaises]
AS
SELECT identificador, nome FROM [cadastro].[Paises];
PRINT 'v8 - 001 - Cria view [app].[vPaises].';

CREATE FUNCTION [app].[fEstados]
(@pais  UNIQUEIDENTIFIER)
RETURNS TABLE
RETURN(
    SELECT E.uf, E.nome 
    FROM [cadastro].[Estados] E
        INNER JOIN [cadastro].[Paises] P ON P.codigo = E.pais 
    WHERE P.identificador = @pais
);
PRINT 'v8 - 002 - Cria function [app].[fEstados].';

CREATE FUNCTION [app].[fCidades]
(@uf CHAR(2))
RETURNS TABLE
RETURN(
    SELECT C.identificador, C.nome
    FROM [cadastro].[Cidades] C
        INNER JOIN [cadastro].[Estados] E ON E.codigo = C.estado
    WHERE E.uf = @uf
);
PRINT 'v8 - 003 - Cria function [app].[fCidades].';

CREATE FUNCTION [app].[fBairros]
(@cidade UNIQUEIDENTIFIER)
RETURNS TABLE
RETURN(
    SELECT B.identificador, B.nome
    FROM [cadastro].[Bairros] B
        INNER JOIN [cadastro].[Cidades] C ON C.codigo = B.cidade
    WHERE
        C.identificador = @cidade
);
PRINT 'v8 - 004 - Cria function [app].[fBairros].';

CREATE VIEW [app].[vLogradouros]
AS
SELECT L.cep, L.nome, L.complemento
FROM [cadastro].[Logradouros] L;
PRINT 'v8 - 005 - Cria view [app].[vLogradouros].';

CREATE FUNCTION [app].[fLogradouros]
(@bairro UNIQUEIDENTIFIER)
RETURNS TABLE
RETURN(
    SELECT L.cep, L.nome, L.complemento
    FROM [cadastro].[Logradouros] L
        INNER JOIN [cadastro].[Bairros] B ON B.codigo = L.bairro
    WHERE B.identificador = @bairro
);
PRINT 'v8 - 006 - Cria function [app].[fLogradouros].';
PRINT 'Fim do script v8. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';