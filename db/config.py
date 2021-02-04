import os
from dotenv import load_dotenv

load_dotenv()


class PostgresConfig:
    name = os.getenv('POSTGRES_DB', 'ads-db')
    user = os.getenv('POSTGRES_USER', 'postgres')
    password = os.getenv('POSTGRES_PASSWORD', '1')
    host = os.getenv('POSTGRES_HOST', 'localhost')
    port = os.getenv('POSTGRES_PORT', '5432')
    url = rf'postgres://{user}:{password}@{host}:{port}/{name}'
