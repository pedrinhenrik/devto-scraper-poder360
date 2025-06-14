from dotenv import load_dotenv
import os

# Carrega as variáveis
load_dotenv()

# Conexão ao banco de dados
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

