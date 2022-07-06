--##Commit Cria a tabela [fontes].[Bancos];
PRINT 'Inicio do script v6. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB01;
IF EXISTS(SELECT TOP 1 1 FROM sys.tables WHERE name = 'Bancos' AND schema_id = SCHEMA_ID('fontes'))
BEGIN
	DROP TABLE [fontes].[Bancos]
	PRINT 'v6 - 001 - Exclusao da tabela [fontes].[Bancos].'
END;
CREATE TABLE [fontes].[Bancos] (
  [codigo] int PRIMARY KEY,
  [nome] varchar(100) UNIQUE NOT NULL
);
PRINT 'v6 - 002 - Criacao da tabela [fontes].[Bancos].';
EXEC sp_addextendedproperty
@name = N'Column_Description',
@value = 'Código informado pelo registro geral das instituições bancárias. Quando o código for negativo, representa um banco criado pelo usuário do sistema.',
@level0type = N'Schema', @level0name = 'fontes',
@level1type = N'Table',  @level1name = 'Bancos',
@level2type = N'Column', @level2name = 'codigo';
PRINT 'v6 - 003 - Aplicada propriedade de descrição da coluna [fontes].[Bancos].[codigo]';
EXEC sp_addextendedproperty
@name = N'Column_Description',
@value = 'Nome do banco.',
@level0type = N'Schema', @level0name = 'fontes',
@level1type = N'Table',  @level1name = 'Bancos',
@level2type = N'Column', @level2name = 'nome';
PRINT 'v6 - 004 - Aplicada propriedade de descrição da coluna [fontes].[Bancos].[nome]';
PRINT 'Fim do script v6. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';