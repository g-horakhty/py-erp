from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services import vendas_service, cupom_fiscal
from app.database import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/nova-venda/")
async def criar_venda(venda_data: dict, db: Session = Depends(get_db)):
    try:
        venda = vendas_service.criar_venda(db, venda_data)
        
        # Gerar cupom fiscal
        cupom_pdf = cupom_fiscal.gerar_cupom_pdf(venda)
        cupom_fiscal.imprimir_cupom(venda)
        
        return {
            "message": "Venda realizada com sucesso",
            "venda_id": venda.id,
            "cupom_pdf": cupom_pdf
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
