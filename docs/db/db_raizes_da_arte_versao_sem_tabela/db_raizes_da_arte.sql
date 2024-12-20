DROP DATABASE IF EXISTS db_raizes_da_arte;
CREATE DATABASE IF NOT EXISTS db_raizes_da_arte;

CREATE TABLE IF NOT EXISTS db_raizes_da_arte.user(
    id INTEGER PRIMARY KEY AUTO_INCREMENT ,
    idPostagem INTEGER,
    nome INTEGER NOT NULL,
    email VARCHAR(50) NOT NULL,
    senha  VARCHAR(500),
    descricao TEXT,
    imagemPerfil TEXT,
    categoria VARCHAR(50)
);
CREATE TABLE IF NOT EXISTS db_raizes_da_arte.postagem(
    id INTEGER PRIMARY KEY ,
    idUsuario INTEGER,
    idComentario INTEGER,
    idImagem INTEGER,
    curtida INTEGER,
    descricao TEXT,
    titulo VARCHAR(50)

);
CREATE TABLE IF NOT EXISTS db_raizes_da_arte.comentario(
    id INTEGER PRIMARY KEY,
    idPostagem INTEGER
);
CREATE TABLE IF NOT EXISTS db_raizes_da_arte.imagem(
    id INTEGER PRIMARY KEY,
    idPostagem INTEGER,
    urlImagem TEXT
);

ALTER TABLE db_raizes_da_arte.user ADD CONSTRAINT fk_usuario_postagem FOREIGN KEY (idPostagem)
REFERENCES db_raizes_da_arte.postagem(id);
ALTER TABLE db_raizes_da_arte.postagem ADD CONSTRAINT fk_postagem_usuario FOREIGN KEY (idUsuario)
REFERENCES db_raizes_da_arte.user(id);
ALTER TABLE db_raizes_da_arte.postagem ADD CONSTRAINT fk_postagem_imagem FOREIGN KEY (idImagem)
REFERENCES db_raizes_da_arte.imagem(id);
ALTER TABLE db_raizes_da_arte.imagem ADD CONSTRAINT fk_imagem_postagem FOREIGN KEY (idPostagem)
REFERENCES db_raizes_da_arte.postagem(id);
ALTER TABLE db_raizes_da_arte.comentario ADD CONSTRAINT fk_postagem_comentario FOREIGN KEY (idPostagem)
REFERENCES db_raizes_da_arte.postagem(id);
ALTER TABLE db_raizes_da_arte.postagem ADD CONSTRAINT fk_comentario_postagem FOREIGN KEY (idComentario)
REFERENCES db_raizes_da_arte.comentario(id);
