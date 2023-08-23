import psycopg2

# Faz a conexão com o Postgres 
con = psycopg2.connect(
    host = "localhost",
    database = "spotify_pbd",
    user = "postgres",
    password = ""
)  

# inicia o cursor para executar as queries
cur = con.cursor()

# cria a table usuario
cur.execute("""CREATE TABLE IF NOT EXISTS usuario (
            email VARCHAR(255) PRIMARY KEY,
            nome VARCHAR(255),
            senha VARCHAR(255),
            foto_perfil bytea);
            """)

# adiciona conteúdo na table usuario
cur.execute("""INSERT INTO usuario (email, nome, senha, foto_perfil) VALUES
            ('daniel@email.com', daniel, 123, foto_daniel.jpg),
            ('rafael@email.com, rafael, 123, foto_rafael.jpg),
            ('henrique@email.com', henrique, 123, foto_henrique.jpg);
            """)


# cria a table playlist
cur.execute("""CREATE TABLE IF NOT EXISTS playlist (
            id VARCHAR(255) PRIMARY KEY,
            nome VARCHAR(255),
            proprietario VARCHAR(255),
            duracao INT);
            """)

# adiciona conteúdo na table playlist
cur.execute("""INSERT INTO playlist (id, nome, proprietario, duracao) VALUES
            (1, melhores hip hop, daniel, 01:00:00),
            (2, melhores rock, rafael, 02:00:00),
            (3, melhores pop, henrique, 03:00:00);
            """)


# cria a table musica
cur.execute("""CREATE TABLE IF NOT EXISTS musica (
            id INT PRIMARY KEY,
            nome VARCHAR(255),
            duracao INT,
            visualizacoes INT,
            album_id INT);
            """)

# adiciona conteúdo na table musica
cur.execute("""INSERT INTO musica (id, nome, duracao, visualizacoes, album_id) VALUES
            (1, 'Chop Suey', 209, 1.291.068.872, 1),
            (2, 'Aerials', 244, 421.070.283, 1),
            (3, 'Lost in Hollywood', 323, 3.852.210, 2),
            (4, 'In The End', 218, 1.603.196.106, 3),
            (5, 'Numb', 187, 2.060.451.800, 4),
            (6, 'Crawling', 216, 391.029.620, 3),
            (7, 'Smells Like Teen Spirit', 278, 1.716.605.396, 5),
            (8, 'Heart-Shaped Box', 282, 243.919.896, 6),
            (9, 'Come As You Are', 224, 512.490.827, 5);
            """)


# cria a table artista
cur.execute("""CREATE TABLE IF NOT EXISTS artista (
            id VARCHAR(255) PRIMARY KEY,
            nome VARCHAR(255),
            descricao VARCHAR(255),
            foto bytea);
            """)

# adiciona conteúdo na table artista
cur.execute("""INSERT INTO artista (id, nome, descricao, foto) VALUES
            (1, 'System of a Down', 'System of a Down é uma banda de metal armeno-americana formada em Glendale, Califórnia em 1994. É composta por Serj Tankian (vocal, teclado, guitarra), Daron Malakian (guitarra, vocal), Shavo Odadjian (baixo, vocal) e John Dolmayan (bateria).', soad.jpg),
            (2, 'Linkin Park', 'Linkin Park é uma banda de rock dos Estados Unidos formada em 1996 em Agoura Hills, Califórnia. Desde a sua formação, a banda já vendeu pelo menos 70 milhões de álbuns pelo mundo todo e ganhou dois Grammy Awards.', lp.jpg),
            (3, 'Nirvana', 'Nirvana foi uma banda norte-americana de rock, formada pelo vocalista e guitarrista Kurt Cobain e pelo baixista Krist Novoselic em Aberdeen no ano de 1987, que obteve grande sucesso em meio ao movimento grunge de Seattle no início dos anos 90.', nirvana.jpg);
            """)


# cria a table album
cur.execute("""CREATE TABLE IF NOT EXISTS album (
            id VARCHAR(255) PRIMARY KEY,
            nome VARCHAR(255),
            capa bytea,
            artista_id VARCHAR(255));
            """)

# adiciona conteúdo na table album
cur.execute("""INSERT INTO album (id, nome, capa, artista_id) VALUES
            (1, 'Toxicity', toxicity.jpg, 1),
            (2, 'Hypnotize', hypnotize.jpg, 1),
            (3, 'Hybrid Theory', hybrid_theory.jpg, 2),
            (4, 'Meteora', meteora.jpg, 2),
            (5, 'Nevermind', nevermind.jpg, 3),
            (6, 'In Utero', in_utero.jpg, 3);
            """)


# cria a table genero
cur.execute("""CREATE TABLE IF NOT EXISTS genero (
            nome VARCHAR(255) PRIMARY KEY);
            """)

# adiciona conteúdo na table genero
cur.execute("""INSERT INTO genero (nome) VALUES
            (rock),
            (pop),
            (hip hop);
            """)

# falta criar: Playlist-Musica , Musica-Artista, Genero-Musica.


# adiciona uma pessoa com nome e senha na tabela person
#cur.execute("insert into person (usuario, senha) values (%s, %s)", ("Daniel", 123))

# deleta uma pessoa com nome Daniel da tabela person
# cur.execute("delete from person where usuario = 'Daniel'")

# seleciona todas as pessoas da tabela person
cur.execute("select usuario, senha from person")

# pega todas as linhas da tabela
rows = cur.fetchall()

# printa todas as linhas no console
for r in rows:
    print(f"Nome: {r[0]}, Senha: {r[1]}")

# "atualiza" a transação
con.commit()

# fecha o cursor (sem memory leaks hehe!)
cur.close()

# termina a conexão com o banco
con.close()
