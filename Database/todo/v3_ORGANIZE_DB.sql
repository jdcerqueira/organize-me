PRINT 'Inicio do script v3. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZE_DB;
CREATE SCHEMA fontes AUTHORIZATION [dbo];
PRINT 'v3 - 001 - Criando o schema [fontes].';
CREATE SCHEMA despesas AUTHORIZATION [dbo];
PRINT 'v3 - 002 - Criando o schema [despesas].';
CREATE SCHEMA efetuados AUTHORIZATION [dbo];
PRINT 'v3 - 003 - Criando o schema [efetuados].';
CREATE SCHEMA sugeridos AUTHORIZATION [dbo];
PRINT 'v3 - 004 - Criando o schema [sugeridos].';
CREATE SCHEMA movimentacoes AUTHORIZATION [dbo];
PRINT 'v3 - 005 - Criando o schema [movimentacoes].';
CREATE SCHEMA receitas AUTHORIZATION [dbo];
PRINT 'v3 - 006 - Criando o schema [receitas].';
CREATE SCHEMA consultas AUTHORIZATION [dbo];
PRINT 'v3 - 007 - Criando o schema [receitas].';
GRANT EXECUTE ON SCHEMA :: despesas TO [Cliente];
PRINT 'v3 - 008 - atribuindo permissao de execucao ao schema [despesas] para a regra [Cliente].';
GRANT EXECUTE ON SCHEMA :: efetuados TO [Cliente];
PRINT 'v3 - 009 - atribuindo permissao de execucao ao schema [efetuados] para a regra [Cliente].';
GRANT EXECUTE ON SCHEMA :: sugeridos TO [Cliente];
PRINT 'v3 - 010 - atribuindo permissao de execucao ao schema [sugeridos] para a regra [Cliente].';
GRANT EXECUTE ON SCHEMA :: movimentacoes TO [Cliente];
PRINT 'v3 - 011 - atribuindo permissao de execucao ao schema [movimentacoes] para a regra [Cliente].';
GRANT EXECUTE ON SCHEMA :: receitas TO [Cliente];
PRINT 'v3 - 012 - atribuindo permissao de execucao ao schema [receitas] para a regra [Cliente].';
GRANT SELECT ON SCHEMA :: consultas TO [Cliente];
PRINT 'v3 - 013 - atribuindo permissao de consulta ao schema [consultas] para a regra [Cliente].';
GRANT EXECUTE ON SCHEMA :: fontes TO [Cliente];
PRINT 'v3 - 014 - atribuindo permissao de consulta ao schema [fontes] para a regra [Cliente].';
PRINT 'Fim do script v3. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';