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

# execuções das queries
# adiciona uma pessoa com nome e senha na tabela person
cur.execute("insert into person (usuario, senha) values (%s, %s)", ("Daniel", 123))

# deleta uma pessoa com nome Daniel da tabela person
# cur.execute("delete from person where usuario = 'Daniel'")

# seleciona todas as pessoas da tabela person
cur.execute("select usuario, senha from person")

# pega todas as linhas da tabela
rows = cur.fetchall()

# printa todas as linhas
for r in rows:
    print(f"Nome: {r[0]}, Senha: {r[1]}")

# "atualiza" a transação
con.commit()

# fecha o cursor (sem memory leaks hehe!)
cur.close()

# termina a conexão com o banco
con.close()
