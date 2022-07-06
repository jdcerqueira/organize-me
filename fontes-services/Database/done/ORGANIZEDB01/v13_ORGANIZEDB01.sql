--##Commit Cria a tabela [fontes].[ItemComplementoFormaPagamento];
PRINT 'Inicio do script v13. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB01;
CREATE TABLE [fontes].[ItemComplementoFormaPagamento] (
  [codigo] int PRIMARY KEY NOT NULL IDENTITY(1, 1),
  [chave] varchar(8000) NOT NULL,
  [tipagem] char(30) NOT NULL,
  [infoConversao] varchar(1024) NOT NULL,
  CONSTRAINT CHK01 CHECK(LOWER(tipagem) LIKE 'varchar%' OR LOWER(tipagem) IN('int', 'float'))
);
PRINT 'v13 - 001 - Criacao da tabela [fontes].[ItemComplementoFormaPagamento].';
CREATE UNIQUE INDEX [UQ01] ON [fontes].[ItemComplementoFormaPagamento] ("chave");
PRINT 'v13 - 002 - Criacao do indice [UQ01].';
PRINT 'Fim do script v13. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';