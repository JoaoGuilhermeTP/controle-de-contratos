import sqlite3

# Conecta ao banco de dados. Se o arquivo não existir, ele será criado.
connection = sqlite3.connect('database.db')

# Cria um "cursor", que é o objeto que usamos para executar comandos SQL
cursor = connection.cursor()

# O comando SQL para criar nossa tabela
# IF NOT EXISTS previne um erro caso a gente rode o script mais de uma vez
create_table_sql = """
CREATE TABLE IF NOT EXISTS secretarias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    sigla TEXT NOT NULL,
    secretario TEXT NOT NULL
);
"""

# Executa o comando SQL
cursor.execute(create_table_sql)

# Grava (commita) as alterações no banco de dados
connection.commit()

# Fecha a conexão
connection.close()

print("Banco de dados e tabela 'secretarias' criados com sucesso.")