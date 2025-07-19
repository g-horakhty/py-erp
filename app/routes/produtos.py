from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import produto
from app.database import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def criar_produto(produto_data: dict, db: Session = Depends(get_db)):
    try:
        novo_produto = produto.Produto(
            codigo=produto_data['codigo'],
            nome=produto_data['nome'],
            descricao=produto_data.get('descricao', ''),
            preco=produto_data['preco'],
            estoque=produto_data.get('estoque', 0),
            unidade_medida=produto_data.get('unidade_medida', 'UN'),
            codigo_barras=produto_data.get('codigo_barras', '')
        )
        db.add(novo_produto)
        db.commit()
        db.refresh(novo_produto)
        return novo_produto
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/")
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(produto.Produto).all()

@router.get("/{produto_id}")
def obter_produto(produto_id: int, db: Session = Depends(get_db)):
    db_produto = db.query(produto.Produto).filter(produto.Produto.id == produto_id).first()
    if not db_produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return db_produto

@router.put("/{produto_id}")
def atualizar_produto(produto_id: int, produto_data: dict, db: Session = Depends(get_db)):
    db_produto = db.query(produto.Produto).filter(produto.Produto.id == produto_id).first()
    if not db_produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    try:
        for key, value in produto_data.items():
            setattr(db_produto, key, value)
        db.commit()
        db.refresh(db_produto)
        return db_produto
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{produto_id}")
def remover_produto(produto_id: int, db: Session = Depends(get_db)):
    db_produto = db.query(produto.Produto).filter(produto.Produto.id == produto_id).first()
    if not db_produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    try:
        db.delete(db_produto)
        db.commit()
        return {"message": "Produto removido com sucesso"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
