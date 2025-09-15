from flask import Flask, json, Response, request
from flask_cors import CORS

# Cria a nossa aplicação
app = Flask(__name__)
CORS(app)

secretarias_data = [
    { "id": 1, "nome": "Secretaria Municipal de Educação", "sigla": "SME", "secretario": "João da Silva" },
    { "id": 2, "nome": "Secretaria Municipal de Saúde", "sigla": "SMS", "secretario": "Maria Oliveira" },
    { "id": 3, "nome": "Secretaria Municipal de Obras", "sigla": "SMO", "secretario": "José Santos" }
]

# Define a primeira rota (a página inicial, ou "/")
@app.route('/')
def home():
  return "API de Contratos no ar!"

@app.route('/secretarias', methods=['GET'])
def get_secretarias():
    json_string = json.dumps(secretarias_data, ensure_ascii=False)
    response = Response(json_string, content_type="application/json; charset=utf-8")
    return response

@app.route('/secretarias', methods=['POST'])
def create_secretaria():
    data = request.json
    nova_secretaria = {
        "id": len(secretarias_data) + 1,
        "nome": data['nome'],
        "sigla": data['sigla'],
        "secretario": data['secretario']
    }
    secretarias_data.append(nova_secretaria)
    return Response(
        json.dumps(nova_secretaria, ensure_ascii=False),
        status=201,
        content_type="application/json; charset=utf-8"
    )
    
# Roda a aplicação
# O host='0.0.0.0' é importante para funcionar no Replit
if __name__ == '__main__':
  app.run(host='0.0.0.0')