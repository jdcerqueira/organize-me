--##Commit Cria o schema [fontes];
PRINT 'Inicio do script v3. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB01;
CREATE SCHEMA fontes AUTHORIZATION [dbo];
PRINT 'v3 - 001 - Criando o schema [fontes].';
GRANT EXECUTE ON SCHEMA :: fontes TO [Cliente];
PRINT 'v3 - 014 - atribuindo permissao de consulta ao schema [fontes] para a regra [Cliente].';
PRINT 'Fim do script v3. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';