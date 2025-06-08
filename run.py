from app import create_app

app = create_app()

if __name__ == "__main__":
    # Executa em modo debug por padrão (FLASK_ENV=development)
    app.run(host="0.0.0.0", port=5000)
