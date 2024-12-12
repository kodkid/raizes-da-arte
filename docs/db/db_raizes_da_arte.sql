DROP DATABASE IF EXISTS db_raizes_da_arte;
CREATE DATABASE IF NOT EXISTS db_raizes_da_arte;

CREATE TABLE IF NOT EXISTS db_raizes_da_arte.user(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    idPostagem INTEGER,
    nome INTEGER NOT NULL,
    email VARCHAR(50) NOT NULL,
    senha  VARCHAR(500),
    descricao TEXT,
    imagemPerfil TEXT,
    categoria VARCHAR(50)
);
CREATE TABLE IF NOT EXISTS db_raizes_da_arte.postagem(
    id INTEGER PRIMARY KEY AUTO_INCREMENT ,
    idUsuario INTEGER,
    ID_POSTAGEM_COMENTARIO INTEGER,
    idImagem INTEGER,
    curtida INTEGER,
    descricao TEXT,
    titulo VARCHAR(50)

);
CREATE TABLE IF NOT EXISTS db_raizes_da_arte.comentario(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    ID_POSTAGEM_COMENTARIO INTEGER,
    ID_USUARIO INTEGER
);
CREATE TABLE IF NOT EXISTS db_raizes_da_arte.imagem(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    idPostagem INTEGER,
    urlImagem TEXT
);
CREATE TABLE IF NOT EXISTS db_raizes_da_arte.postagem_comentario(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    idPostagem INTEGER,
    idComentario INTEGER,
    dataHora DATE
);

ALTER TABLE db_raizes_da_arte.user ADD CONSTRAINT fk_usuario_postagem FOREIGN KEY (idPostagem)
REFERENCES db_raizes_da_arte.postagem(id);
ALTER TABLE db_raizes_da_arte.postagem ADD CONSTRAINT fk_postagem_usuario FOREIGN KEY (idUsuario)
REFERENCES db_raizes_da_arte.user(id);
ALTER TABLE db_raizes_da_arte.postagem ADD CONSTRAINT fk_postagem_imagem FOREIGN KEY (idImagem)
REFERENCES db_raizes_da_arte.imagem(id);
ALTER TABLE db_raizes_da_arte.imagem ADD CONSTRAINT fk_imagem_postagem FOREIGN KEY (idPostagem)
REFERENCES db_raizes_da_arte.postagem(id);
ALTER TABLE db_raizes_da_arte.postagem_comentario ADD CONSTRAINT fk__comentarioPostagem_postagem FOREIGN KEY (idPostagem)
REFERENCES db_raizes_da_arte.postagem(id);
ALTER TABLE db_raizes_da_arte.postagem ADD CONSTRAINT fk__postagem_comentarioPostagem FOREIGN KEY (ID_POSTAGEM_COMENTARIO)
REFERENCES db_raizes_da_arte.postagem_comentario(id);
ALTER TABLE db_raizes_da_arte.comentario ADD CONSTRAINT fk__comentario_comentarioPostagem FOREIGN KEY (ID_POSTAGEM_COMENTARIO)
REFERENCES db_raizes_da_arte.postagem_comentario(id);
ALTER TABLE db_raizes_da_arte.postagem_comentario ADD CONSTRAINT fk__comentarioPostagem_comentario FOREIGN KEY (idComentario)
REFERENCES db_raizes_da_arte.comentario(id);


