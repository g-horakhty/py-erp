from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import venda
from datetime import datetime, timedelta
from fastapi.responses import FileResponse
import os
from app.config import settings

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/vendas-periodo/")
def relatorio_vendas_periodo(
    inicio: str, 
    fim: str, 
    db: Session = Depends(get_db)
):
    try:
        data_inicio = datetime.strptime(inicio, "%Y-%m-%d")
        data_fim = datetime.strptime(fim, "%Y-%m-%d") + timedelta(days=1)
        
        vendas = db.query(venda.Venda).filter(
            venda.Venda.data >= data_inicio,
            venda.Venda.data <= data_fim
        ).all()
        
        total_periodo = sum(v.total for v in vendas)
        
        return {
            "periodo": f"{inicio} a {fim}",
            "quantidade_vendas": len(vendas),
            "total_periodo": total_periodo,
            "vendas": vendas
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/cupom/{venda_id}")
def obter_cupom_venda(venda_id: int):
    cupom_path = os.path.join(settings.CUPONS_DIR, f"cupom_{venda_id}.pdf")
    if not os.path.exists(cupom_path):
        raise HTTPException(status_code=404, detail="Cupom não encontrado")
    return FileResponse(cupom_path, media_type='application/pdf', filename=f"cupom_{venda_id}.pdf")
