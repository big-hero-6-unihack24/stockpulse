from dotenv import load_dotenv
load_dotenv()
import os

# Load environment variables
cors_allowed_origins = os.getenv(
    'CORS_ALLOWED_ORIGINS',
    'http://localhost;http://localhost:8081;http://localhost:3000;https://big-hero-6-unihack24.github.io;https://big-hero-6-unihack24.github.io/;https://big-hero-6-unihack24.github.io/stockpulse;https://big-hero-6-unihack24.github.io/stockpulse/'
)
cors_allowed_origins_list = cors_allowed_origins.split(';')

cors_allowed_hosts = os.getenv(
    'CORS_ALLOWED_HOSTS',
    'localhost;127.0.0.1;stockpulse-api.azurewebsites.net'
)

cors_allowed_hosts_list = cors_allowed_hosts.split(';')