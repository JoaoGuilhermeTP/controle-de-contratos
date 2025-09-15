from flask import Flask, json, Response, request
from flask_cors import CORS
import sqlite3


# Funcção para conectar com o banco de dados
def get_db_connection():
    conn = sqlite3.connect('database.db')
    # Converte o resultado de tuplas para objetos tipo dicionário
    conn.row_factory = sqlite3.Row
    return conn


# Cria a nossa aplicação
app = Flask(__name__)
CORS(app)


# Define a primeira rota (a página inicial, ou "/")
@app.route('/')
def home():
  return "API de Contratos no ar!"


@app.route('/secretarias', methods=['GET'])
def get_secretarias():
    conn = get_db_connection()
    secretarias_rows = conn.execute('SELECT * FROM secretarias').fetchall()
    conn.close()
    secretarias_list = [dict(row) for row in secretarias_rows]
    json_string = json.dumps(secretarias_list, ensure_ascii=False)
    return Response(json_string, content_type="application/json; charset=utf-8")


@app.route('/secretarias', methods=['POST'])
def create_secretaria():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO secretarias (nome, sigla, secretario) VALUES (?, ?, ?)',
        (data['nome'], data['sigla'], data['secretario'])
    )
    
    new_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    nova_secretaria = {
        "id": new_id,
        "nome": data['nome'],
        "sigla": data['sigla'],
        "secretario": data['secretario']
    }

    return Response(
        json.dumps(nova_secretaria, ensure_ascii=False),
        status=201,
        content_type="application/json; charset=utf-8"
    )
    
    
# Roda a aplicação
# O host='0.0.0.0' é importante para funcionar no Replit
if __name__ == '__main__':
  app.run(host='0.0.0.0')