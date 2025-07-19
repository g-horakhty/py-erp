import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    CUPONS_DIR: str = os.path.join(os.path.dirname(__file__), "../cupons_fiscais")
    IMPRESSORA_IP: str = "192.168.1.100"  # Substitua pelo IP da sua impressora
    
    class Config:
        env_file = ".env"

settings = Settings()

# Criar diretório para cupons se não existir
os.makedirs(settings.CUPONS_DIR, exist_ok=True)
