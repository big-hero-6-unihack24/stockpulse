from dotenv import load_dotenv

load_dotenv()
import os

# Load environment variables
cors_allowed_origins = os.getenv(
    'CORS_ALLOWED_ORIGINS',
    'http://localhost;http://localhost:8081;http://localhost:3000;'
)
cors_allowed_origins_list = cors_allowed_origins.split(';')

cors_allowed_hosts = os.getenv(
    'CORS_ALLOWED_HOSTS',
    'localhost;127.0.0.1'
)

cors_allowed_hosts_list = cors_allowed_hosts.split(';')