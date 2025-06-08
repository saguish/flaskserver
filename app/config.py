import os
from dotenv import load_dotenv

# Carrega o .env
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, os.pardir, ".env"))

class Config:
    # Chaves principais
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # para evitar warnings

    # Opções JWT (exemplo de expiração)
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # segundos (1h)
    JWT_REFRESH_TOKEN_EXPIRES = 86400  # segundos (24h)
