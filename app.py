from flask import Flask, jsonify
from api import api_blueprint
from datetime import datetime  # Importe datetime aqui

app = Flask(__name__)

# Registre o blueprint da API no aplicativo principal
app.register_blueprint(api_blueprint)

# Rota para obter a data e hora atual em formato JSON
@app.route('/tempo', methods=['GET'])
def get_tempo():
    dynamic_date = datetime.now()
    return jsonify({'date': dynamic_date.strftime('%Y-%m-d %H:%M:%S')})

if __name__ == '__main__':
    app.run(debug=True)
