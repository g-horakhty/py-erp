from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Cliente(Base):
    __tablename__ = "clientes"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    cpf_cnpj = Column(String, unique=True, index=True)
    telefone = Column(String)
    email = Column(String)
    endereco = Column(String)
    
    vendas = relationship("Venda", back_populates="cliente")
