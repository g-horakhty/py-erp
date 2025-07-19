from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import produto, venda, cliente
from datetime import datetime, timedelta

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/dashboard")
async def dashboard(request: Request, db: Session = Depends(get_db)):
    # Dados para o dashboard
    total_vendas = db.query(venda.Venda).count()
    total_produtos = db.query(produto.Produto).count()
    vendas_hoje = db.query(venda.Venda).filter(
        venda.Venda.data >= datetime.now().date()
    ).count()
    
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "total_vendas": total_vendas,
        "total_produtos": total_produtos,
        "vendas_hoje": vendas_hoje
    })

@router.get("/produtos")
async def listar_produtos(request: Request, db: Session = Depends(get_db)):
    produtos = db.query(produto.Produto).all()
    return templates.TemplateResponse("produtos.html", {
        "request": request,
        "produtos": produtos
    })

@router.get("/vendas")
async def listar_vendas(request: Request, db: Session = Depends(get_db)):
    vendas = db.query(venda.Venda).order_by(venda.Venda.data.desc()).limit(50).all()
    return templates.TemplateResponse("vendas.html", {
        "request": request,
        "vendas": vendas
    })
