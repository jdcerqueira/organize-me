PRINT 'Inicio do script v1. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';

USE master;

IF EXISTS(SELECT TOP 1 1 FROM sys.databases WHERE name = 'ORGANIZE_DB')
BEGIN
	ALTER DATABASE ORGANIZE_DB SET RESTRICTED_USER WITH ROLLBACK IMMEDIATE
	PRINT 'v1 - 001 - Exclusao da base existente - alterando para modo restrito de usuario.'
	DROP DATABASE ORGANIZE_DB
	PRINT 'v1 - 002 - Exclusao da base existente - excluindo a base existente.'
END;


CREATE DATABASE ORGANIZE_DB;
PRINT 'v1 - 003 - Criacao da base ORGANIZE_DB.';

ALTER DATABASE ORGANIZE_DB SET ALLOW_SNAPSHOT_ISOLATION ON;
PRINT 'v1 - 004 - Alteracao de permissao do modo SNAPSHOT.';

IF EXISTS(SELECT TOP 1 1 FROM sys.syslogins WHERE name = 'aplicacao')
BEGIN
	DROP LOGIN aplicacao
	PRINT 'v1 - 005 - Encontrou o login [aplicacao] e removeu.'
END;

CREATE LOGIN aplicacao WITH 
	PASSWORD = 'aplicacao', 
	CHECK_POLICY = OFF, 
	CHECK_EXPIRATION = OFF, 
	DEFAULT_DATABASE = ORGANIZE_DB;
PRINT 'v1 - 006 - Criou o login [aplicacao].';

PRINT 'Fim do script v1. - (' + CONVERT(VARCHAR,GETDATE(),120) + ' ' + CONVERT(VARCHAR,GETDATE(),114) + ')';