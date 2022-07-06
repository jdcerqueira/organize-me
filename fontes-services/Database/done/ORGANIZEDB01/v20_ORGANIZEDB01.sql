--##Commit Cria a view [app].[vFormaPagamento];
PRINT 'Inicio do script v20. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB01;
CREATE VIEW [app].[vFormaPagamento]
AS
SELECT
	FP.identificador, FP.nome,
	B.codigo codBanco, B.nome nomeBanco,
	TP.identificador idTipoPagamento, TP.nome nomeTipoPagamento, TP.aceitaComplemento
FROM fontes.FormaPagamento FP
	INNER JOIN fontes.Bancos B ON B.codigo = FP.banco
	INNER JOIN fontes.TipoFormaPagamento TP ON TP.codigo = FP.tipoPagamento;
PRINT 'v20 - 001 - Criacao da view [app].[vFormaPagamento].';
PRINT 'Fim do script v20. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';