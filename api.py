from flask import Blueprint, jsonify
from datetime import datetime

api_blueprint = Blueprint('api', __name__)

# Dados de exemplo para o estabelecimento de comidas/lanches
estabelecimento_info = {
    "nome": "Gildo Lanches",
    "descricao": "Localizado na cidade de Recife, um ambiente para todos desfrutarem de deliciosos lanches.",
    "endereco": "123 Rua das Coxinhas",
    "telefone": "(11) 1234-5678",
    "horario_funcionamento": "Seg-Sex: 17h-21h, Sáb-Dom: 17h-03h",
}

# Rota para obter informações sobre o estabelecimento
@api_blueprint.route('/api/estabelecimento', methods=['GET'])
def get_estabelecimento_info():
    return jsonify(estabelecimento_info)