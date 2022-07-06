--##Commit Cria as tabelas [fontes].[FormaPagamento] e [fontes].[ComplementoFormaPagamento];
PRINT 'Inicio do script v19. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB01;
CREATE TABLE [fontes].[FormaPagamento](
	codigo			INT 				NOT NULL 	IDENTITY 			PRIMARY KEY,
	identificador	UNIQUEIDENTIFIER	NOT NULL	DEFAULT(NEWID())	UNIQUE,
	banco			INT					NOT NULL,
	tipoPagamento	INT					NOT NULL,
	nome			VARCHAR(100)		NOT NULL	UNIQUE
);
PRINT 'v19 - 001 - Criacao da tabela [fontes].[FormaPagamento].';
ALTER TABLE [fontes].[FormaPagamento] ADD FOREIGN KEY (banco) REFERENCES [fontes].[Bancos](codigo);
PRINT 'v19 - 002 - Criacao do relacionamento [fontes].[Bancos] -> [fontes].[FormaPagamento].';
ALTER TABLE [fontes].[FormaPagamento] ADD FOREIGN KEY (tipoPagamento) REFERENCES [fontes].[TipoFormaPagamento](codigo);
PRINT 'v19 - 003 - Criacao do relacionamento [fontes].[TipoFormaPagamento] -> [fontes].[FormaPagamento].';
CREATE TABLE [fontes].[ComplementoFormaPagamento](
	formaPagamento	INT	NOT NULL,
	itemComplemento	INT	NOT NULL,
	valor			VARCHAR(8000),
	PRIMARY KEY(formaPagamento,itemComplemento)
);
PRINT 'v19 - 004 - Criacao da tabela [fontes].[ComplementoFormaPagamento].';
ALTER TABLE [fontes].[ComplementoFormaPagamento] ADD FOREIGN KEY (formaPagamento) REFERENCES [fontes].[FormaPagamento](codigo);
PRINT 'v19 - 005 - Criacao do relacionamento [fontes].[FormaPagamento] -> [fontes].[ComplementoFormaPagamento].';
ALTER TABLE [fontes].[ComplementoFormaPagamento] ADD FOREIGN KEY (itemComplemento) REFERENCES [fontes].[ItemComplementoFormaPagamento](codigo);
PRINT 'v19 - 006 - Criacao do relacionamento [fontes].[ItemComplementoFormaPagamento] -> [fontes].[ComplementoFormaPagamento].';
PRINT 'Fim do script v19. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';