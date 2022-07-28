--##Commit Cria tabela de estabelecimentos e procedures de insercao e exclusao e view de consulta;
PRINT 'Inicio do script v12. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB02;

CREATE TABLE [cadastro].[Estabelecimentos](
	codigo			INT					NOT NULL	IDENTITY		PRIMARY KEY,
	identificador	UNIQUEIDENTIFIER	NOT NULL	DEFAULT NEWID()	UNIQUE,
	nome			VARCHAR(100)		NOT NULL,
	categoria		INT					NOT NULL
);
PRINT 'v12 - 001 - Cria tabela [cadastro].[Estabelecimentos]';
CREATE INDEX [IDX01] ON [cadastro].[Estabelecimentos](categoria);
PRINT 'v12 - 002 - Cria indice [cadastro].[Estabelecimentos].[IDX01]';
CREATE INDEX [IDX02] ON [cadastro].[Estabelecimentos](nome);
PRINT 'v12 - 003 - Cria indice [cadastro].[Estabelecimentos].[IDX02]';
ALTER TABLE [cadastro].[Estabelecimentos] ADD FOREIGN KEY (categoria) REFERENCES [cadastro].[Categorias](codigo);
PRINT 'v12 - 004 - Cria relacionamento [cadastro].[Estabelecimentos] -> [cadastro].[Categorias]';

CREATE VIEW [app].[vEstabelecimentos]
AS
SELECT
	E.identificador estabelecimento, E.nome,
	C.identificador categoria, C.nome nome_categoria
FROM [cadastro].[Estabelecimentos] E
	INNER JOIN [cadastro].[Categorias] C ON C.codigo = E.categoria;
PRINT 'v12 - 005 - Cria view [app].[vEstabelecimentos]';

CREATE PROCEDURE [app].[insereEstabelecimento]
	@nome		VARCHAR(100),
	@categoria	UNIQUEIDENTIFIER
AS
BEGIN
	SET NOCOUNT ON
	DECLARE @codCategoria INT = (SELECT codigo FROM [cadastro].[Categorias] WHERE identificador = @categoria)

	INSERT INTO [cadastro].[Estabelecimentos]
		(nome, categoria)
	OUTPUT inserted.identificador, inserted.nome
	VALUES
		(@nome, @codCategoria)

	SET NOCOUNT OFF
END;
PRINT 'v12 - 006 - Cria procedure [app].[insereEstabelecimento]';

CREATE PROCEDURE [app].[apagaEstabelecimento]
	@estabelecimento UNIQUEIDENTIFIER
AS
BEGIN
	SET NOCOUNT ON

	DELETE [cadastro].[Estabelecimentos]
	OUTPUT deleted.identificador, deleted.nome
	WHERE identificador = @estabelecimento

	SET NOCOUNT OFF
END;
PRINT 'v12 - 007 - Cria procedure [app].[apagaEstabelecimento]';
PRINT 'Fim do script v12. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';