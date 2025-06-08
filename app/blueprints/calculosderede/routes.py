from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ...utils.calculos import calcular_carga_maxima

# VER PASSO 12 DO TUTORIAL CHATGPT
# DEPOIS DE RESOLVER, TIRAR COMENTÁRIO DO __init__.py e ativar blueprint

calculos_bp = Blueprint("calculos", __name__)

@calculos_bp.route("/docs", methods=["GET"])
def documentacao():
    return jsonify({
        "endpoints": {
            "POST /api/calculos/carga-maxima": {
                "descrição": "Calcula a carga máxima",
                "json_exemplo_req": {
                    "altura": 2.5,
                    "largura": 1.2,
                    "material": "aço"
                },
                "json_exemplo_resposta": {
                    "carga_maxima": 3000.0
                }
            }
        }
    })

@calculos_bp.route("/carga-maxima", methods=["POST"])
@jwt_required()
def rota_carga_maxima():
    data = request.get_json()
    if not data:
        return jsonify({"msg": "JSON body obrigatório"}), 400

    altura = data.get("altura")
    largura = data.get("largura")
    material = data.get("material")
    if altura is None or largura is None or material is None:
        return jsonify({"msg": "Parâmetros 'altura', 'largura' e 'material' obrigatórios"}), 400

    try:
        resultado = calcular_carga_maxima(float(altura), float(largura), material)
    except Exception as e:
        return jsonify({"msg": "Erro ao calcular", "erro": str(e)}), 500

    return jsonify(resultado), 200
