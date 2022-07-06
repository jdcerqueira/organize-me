--##Commit Cria o schema [app];
PRINT 'Inicio do script v4. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB01;
CREATE SCHEMA app AUTHORIZATION [dbo];
PRINT 'v4 - 001 - Criando o schema [app].';
GRANT EXECUTE ON SCHEMA :: app TO [Cliente];
PRINT 'v4 - 002 - atribuindo permissao de execucao ao schema [app] para a regra [Cliente].';
GRANT SELECT ON SCHEMA :: app TO [Cliente];
PRINT 'v4 - 003 - atribuindo permissao de consulta ao schema [app] para a regra [Cliente].';
PRINT 'Fim do script v3. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';