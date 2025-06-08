from flask import Flask
from .config import Config
from .extensions import db, migrate, jwt, cors

# Importações de blueprints
from .blueprints.auth.routes import auth_bp
from .blueprints.public.routes import public_bp
from .blueprints.private.routes import private_bp


import os


###########################################################################
###########################################################################

# PRECISO RESOLVER DEPOIS
#from .blueprints.calculosderede.routes import calculos_bp

###########################################################################
###########################################################################



def create_app():
    app = Flask(__name__)

    # Carrega configurações
    app.config.from_object(Config)


    # Inicializa extensões
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})  # permite CORS nas rotas /api/*

    # Registrar Blueprints
    # 1. Rotas de autenticação (ex.: /api/auth/login, /api/auth/register)
    app.register_blueprint(auth_bp, url_prefix="/api/auth")

    # 2. Rotas públicas (ex.: /, /sobre, etc)
    app.register_blueprint(public_bp)

    # 3. Rotas privadas (protegidas por JWT) /privado, /privado/dashboard, etc
    app.register_blueprint(private_bp, url_prefix="/privado")


    ###########################################################################
    ################### RESOLVER DEPOIS COMO CHAMAR OS CALCULOS ###############
    ###########################################################################

    # 4. Rotas da API de cálculos (endereços tipo /api/calculos/...)
    #app.register_blueprint(calculos_bp, url_prefix="/api/calculos")

    return app
