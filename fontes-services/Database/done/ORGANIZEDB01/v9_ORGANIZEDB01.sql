--##Commit Cria a tabela [fontes].[TipoFormaPagamento];
PRINT 'Inicio do script v9. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB01;
IF EXISTS(SELECT TOP 1 1 FROM sys.tables WHERE name = 'TipoFormaPagamento' AND schema_id = SCHEMA_ID('fontes'))
BEGIN
	DROP TABLE [fontes].[TipoFormaPagamento]
	PRINT 'v9 - 001 - Exclusao da tabela [fontes].[TipoFormaPagamento].'
END;
CREATE TABLE [fontes].[TipoFormaPagamento] (
  [codigo] 				int 				PRIMARY KEY IDENTITY(1, 1),
  [identificador] 		uniqueidentifier 	UNIQUE DEFAULT newid(),
  [nome] 				varchar(100) 		UNIQUE,
  [aceitaComplemento] 	bit 				DEFAULT (0)
);
PRINT 'v9 - 002 - Criacao da tabela [fontes].[TipoFormaPagamento].'
PRINT 'Fim do script v9. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';