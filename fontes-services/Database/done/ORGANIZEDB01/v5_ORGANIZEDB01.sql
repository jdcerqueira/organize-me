--##Commit Cria a sequence [fontes].[seqBancosPersonalizados] e a procedure [app].[insereBanco];
PRINT 'Inicio do script v5. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB01;
IF EXISTS(SELECT TOP 1 1 FROM sys.sequences WHERE name = 'seqBancosPersonalizados' AND schema_id = SCHEMA_ID('fontes'))
BEGIN
	DROP SEQUENCE [fontes].[seqBancosPersonalizados]
	PRINT 'v5 - 001 - Exclusao da sequence [fontes].[seqBancosPersonalizados].'
END;
IF OBJECT_ID('app.insereBanco','P') IS NOT NULL
BEGIN
	DROP PROCEDURE app.insereBanco
	PRINT 'v5 - 002 - Exclusao da procedure [app].[insereBanco]'
END;
CREATE SEQUENCE fontes.seqBancosPersonalizados
	AS INT
	START WITH -1
	INCREMENT BY -1
	NO MINVALUE
	MAXVALUE -1
	CYCLE
	NO CACHE;
PRINT 'v5 - 003 - Criacao da sequence [fontes].[seqBancosPersonalizados].';
/*
Nome:app.insereBanco
Definicao: Inclusao de vinculos de bancos no sistema.
Data: 16-06-2022
Autor: J.
****************************************
Manuten��es:
*/
CREATE PROCEDURE app.insereBanco
	@codigo	INT,
	@nome	VARCHAR(100)
AS
BEGIN
	IF @codigo IS NULL
		INSERT INTO fontes.Bancos
			(codigo, nome)
		OUTPUT inserted.codigo
		VALUES
			(NEXT VALUE FOR fontes.seqBancosPersonalizados, @nome)
	ELSE
		INSERT INTO fontes.Bancos
			(codigo, nome)
		OUTPUT inserted.codigo
		VALUES
			(@codigo, @nome)
		
END;
PRINT 'v5 - 004 - Criacao da procedure [app].[insereBanco].';
PRINT 'Fim do script v5. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';