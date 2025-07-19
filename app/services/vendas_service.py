from sqlalchemy.orm import Session
from app.models import produto, venda, cliente
from datetime import datetime

def criar_venda(db: Session, venda_data: dict):
    try:
        # Verificar se cliente existe ou criar novo
        if 'cliente_id' in venda_data:
            db_cliente = db.query(cliente.Cliente).filter(cliente.Cliente.id == venda_data['cliente_id']).first()
            if not db_cliente:
                raise ValueError("Cliente não encontrado")
        else:
            db_cliente = cliente.Cliente(
                nome=venda_data.get('cliente_nome', 'CONSUMIDOR FINAL'),
                cpf_cnpj=venda_data.get('cliente_documento', '')
            )
            db.add(db_cliente)
            db.commit()
            db.refresh(db_cliente)

        # Criar a venda
        nova_venda = venda.Venda(
            data=datetime.now(),
            cliente_id=db_cliente.id,
            total=0,
            forma_pagamento=venda_data.get('forma_pagamento', 'Dinheiro')
        )
        db.add(nova_venda)
        db.commit()
        db.refresh(nova_venda)

        # Adicionar itens da venda
        total_venda = 0
        for item in venda_data['itens']:
            db_produto = db.query(produto.Produto).filter(produto.Produto.id == item['produto_id']).first()
            if not db_produto:
                raise ValueError(f"Produto ID {item['produto_id']} não encontrado")

            if db_produto.estoque < item['quantidade']:
                raise ValueError(f"Estoque insuficiente para o produto {db_produto.nome}")

            # Atualizar estoque
            db_produto.estoque -= item['quantidade']
            db.commit()

            # Calcular total do item
            total_item = db_produto.preco * item['quantidade']
            total_venda += total_item

            # Criar item da venda
            novo_item = venda.ItemVenda(
                venda_id=nova_venda.id,
                produto_id=db_produto.id,
                quantidade=item['quantidade'],
                preco_unitario=db_produto.preco,
                total=total_item
            )
            db.add(novo_item)

        # Atualizar total da venda
        nova_venda.total = total_venda
        db.commit()
        db.refresh(nova_venda)

        return nova_venda

    except Exception as e:
        db.rollback()
        raise e
