from flask import Blueprint, jsonify

public_bp = Blueprint("public", __name__)

@public_bp.route("/")
def home():
    return jsonify({"msg": "Bem-vindo ao site sergio. vai começar a festa"})

@public_bp.route("/sobre")
def sobre():
    return jsonify({"app": "site sergio.", "versão": "1.0.0"})
