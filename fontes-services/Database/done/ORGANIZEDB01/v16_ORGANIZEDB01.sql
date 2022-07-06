--##Commit Cria as tabelas [fontes].[TemplateComplementoFormaPagamento] e [fontes].[TemplateItemComplementoFormaPagamento];
PRINT 'Inicio do script v16. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB01;
CREATE TABLE [fontes].[TemplateComplementoFormaPagamento](
  codigo        INT IDENTITY NOT NULL PRIMARY KEY,
  descricao     VARCHAR(100) NOT NULL UNIQUE,
  identificador UNIQUEIDENTIFIER DEFAULT NEWID()
);
PRINT 'v16 - 001 - Criacao da tabela [fontes].[TemplateComplementoFormaPagamento].';
CREATE TABLE [fontes].[TemplateItemComplementoFormaPagamento](
    template    INT NOT NULL,
    chave       INT NOT NULL,
    PRIMARY KEY(template, chave)
);
PRINT 'v16 - 002 - Criacao da tabela [fontes].[TemplateItemComplementoFormaPagamento].';
ALTER TABLE [fontes].[TemplateItemComplementoFormaPagamento] ADD FOREIGN KEY ([template]) REFERENCES [fontes].[TemplateComplementoFormaPagamento] ([codigo]);
PRINT 'v16 - 003 - Criacao da FK [fontes].[TemplateItemComplementoFormaPagamento].[template].';
ALTER TABLE [fontes].[TemplateItemComplementoFormaPagamento] ADD FOREIGN KEY ([chave]) REFERENCES [fontes].[ItemComplementoFormaPagamento] ([codigo]);
PRINT 'v16 - 004 - Criacao da FK [fontes].[TemplateItemComplementoFormaPagamento].[chave].';
PRINT 'Fim do script v16. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';