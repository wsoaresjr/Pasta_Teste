from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Deploy automático funcionando! Código atualizado com sucesso."

if __name__ == '__main__':
    # Inicia o servidor Flask escutando em todas as interfaces na porta 5000
    app.run(host='0.0.0.0', port=5000)


# Teste 1
# Novo Teste
