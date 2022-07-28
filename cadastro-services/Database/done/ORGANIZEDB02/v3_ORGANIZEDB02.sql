--##Commit Cria o schema [cadastro];
PRINT 'Inicio do script v3. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB02;
CREATE SCHEMA [cadastro] AUTHORIZATION [dbo];
PRINT 'v3 - 001 - Criando o schema [cadastro].';
PRINT 'Fim do script v3. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';