--##Commit Cria tabela de endereco para estabelecimento e funcao de consulta e procedures de insert e delete;
PRINT 'Inicio do script v14. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';
USE ORGANIZEDB02;

CREATE TABLE [cadastro].[EnderecosEstabelecimento](
	cep					CHAR(9)				NOT NULL,
	estabelecimento		INT					NOT NULL,
	identificador		UNIQUEIDENTIFIER	NOT NULL	DEFAULT NEWID(),
	numero				CHAR(20)			NOT NULL	DEFAULT '',
	complemento			VARCHAR(50)			NOT NULL	DEFAULT '',
	ponto_referencia	VARCHAR(512)		NOT NULL	DEFAULT ''
	PRIMARY KEY (cep, estabelecimento)
);
PRINT 'v14 - 001 - Cria tabela [cadastro].[EnderecosEstabelecimento].';
ALTER TABLE [cadastro].[EnderecosEstabelecimento] ADD UNIQUE (cep, numero, complemento);
PRINT 'v14 - 002 - Cria unique [cadastro].[EnderecosEstabelecimento](cep, numero, complemento).';
CREATE INDEX [IDX01] ON [cadastro].[EnderecosEstabelecimento](identificador);
PRINT 'v14 - 003 - Cria indice [cadastro].[EnderecosEstabelecimento].[IDX01].';
ALTER TABLE [cadastro].[EnderecosEstabelecimento] ADD FOREIGN KEY(cep) REFERENCES [cadastro].[Logradouros](cep);
PRINT 'v14 - 004 - Cria relacionamento [cadastro].[EnderecosEstabelecimento] -> [cadastro].[Logradouros].';
ALTER TABLE [cadastro].[EnderecosEstabelecimento] ADD FOREIGN KEY(estabelecimento) REFERENCES [cadastro].[Estabelecimentos](codigo);
PRINT 'v14 - 005 - Cria relacionamento [cadastro].[EnderecosEstabelecimento] -> [cadastro].[Estabelecimentos].';

CREATE FUNCTION [app].[fEnderecosEstabelecimento]
(
	@estabelecimento UNIQUEIDENTIFIER
)
RETURNS TABLE
RETURN(
	SELECT
		E.cep, E.logradouro, EE.numero, EE.complemento, EE.ponto_referencia, 
		E.bairro, E.cidade, E.estado, E.uf, E.pais
	FROM [cadastro].[EnderecosEstabelecimento] EE
		INNER JOIN [app].[vEnderecos] E ON E.cep = EE.cep
		INNER JOIN [cadastro].[Estabelecimentos] ES ON ES.codigo = EE.estabelecimento
	WHERE ES.identificador = @estabelecimento
);
PRINT 'v14 - 006 - Cria function [app].[fEnderecosEstabelecimento].';

CREATE PROCEDURE [app].[insereEnderecoEstabelecimento]
	@cep				CHAR(9),
	@estabelecimento	UNIQUEIDENTIFIER,
	@numero				CHAR(20),
	@complemento		VARCHAR(50),
	@ponto_referencia	VARCHAR(512)
AS
BEGIN
	SET NOCOUNT ON
	DECLARE @codEstabelecimento	INT = (SELECT codigo FROM [cadastro].[Estabelecimentos] WHERE identificador = @estabelecimento)

	INSERT INTO [cadastro].[EnderecosEstabelecimento]
		(cep, estabelecimento, numero, complemento, ponto_referencia)
	OUTPUT inserted.identificador, inserted.cep, inserted.numero, inserted.complemento
	VALUES
		(@cep, @codEstabelecimento, @numero, @complemento, @ponto_referencia)

	SET NOCOUNT OFF
END;
PRINT 'v14 - 007 - Cria procedure [app].[insereEnderecoEstabelecimento].';

CREATE PROCEDURE [app].[apagaEnderecoEstabelecimento]
	@enderecoEstabelecimento UNIQUEIDENTIFIER
AS
BEGIN
	SET NOCOUNT ON

	DELETE [cadastro].[EnderecosEstabelecimento]
	OUTPUT deleted.identificador, deleted.cep, deleted.numero, deleted.complemento
	WHERE identificador = @enderecoEstabelecimento

	SET NOCOUNT OFF
END;
PRINT 'v14 - 008 - Cria procedure [app].[apagaEnderecoEstabelecimento].';
PRINT 'Fim do script v14. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';