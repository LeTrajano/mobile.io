from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name)

# Rota para obter a data e hora atual em formato JSON
@app.route('/tempo', methods=['GET'])
def get_tempo():
    dynamic_date = datetime.now()
    return jsonify({'date': dynamic_date.strftime('%Y-%m-%d %H:%M:%S')})

if __name__ == '__main__':
    app.run(debug=True)
