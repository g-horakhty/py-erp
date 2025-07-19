import uvicorn
from app.main import app

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",  # Permite acesso na rede local
        port=8000,
        reload=True,      # Recarrega automaticamente durante o desenvolvimento
        workers=1         # Adequado para uso local
    )
