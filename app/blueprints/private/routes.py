from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ...models.user import User

# Exatamente assim:
private_bp = Blueprint("private", __name__)

@private_bp.route("/dashboard")
@jwt_required()
def dashboard():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return jsonify({"msg": "Usuário não encontrado"}), 404
    return jsonify({
        "msg": f"Bem-vindo, {user.username}!",
        "perfil": user.to_dict()
    })
