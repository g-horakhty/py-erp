import pdfkit
from jinja2 import Environment, FileSystemLoader
import os
from app.config import settings
from app.services.impressora import imprimir_cupom_direto

def gerar_cupom_pdf(venda):
    # Configurar ambiente de templates
    env = Environment(loader=FileSystemLoader('app/templates'))
    template = env.get_template('cupom.html')
    
    # Renderizar template com dados da venda
    html = template.render(venda=venda)
    
    # Caminho para salvar o PDF
    pdf_path = os.path.join(settings.CUPONS_DIR, f"cupom_{venda.id}.pdf")
    
    # Converter HTML para PDF
    pdfkit.from_string(html, pdf_path)
    
    return pdf_path

def imprimir_cupom(venda):
    # Gerar texto formatado para impressora de 40 colunas
    texto_cupom = formatar_cupom_40colunas(venda)
    
    # Enviar para impressora
    imprimir_cupom_direto(texto_cupom)

def formatar_cupom_40colunas(venda):
    # Formatar o cupom para impressão em 40 colunas
    lines = []
    lines.append("=" * 40)
    lines.append(f"{'LOJA XYZ':^40}")
    lines.append(f"{'CNPJ: 12.345.678/0001-99':^40}")
    lines.append(f"{'CUPOM FISCAL':^40}")
    lines.append("-" * 40)
    lines.append(f"Data: {venda.data:%d/%m/%Y %H:%M}")
    lines.append(f"Cliente: {venda.cliente.nome[:30]}")
    lines.append("-" * 40)
    
    for item in venda.itens:
        linha_produto = f"{item.quantidade}x {item.produto.nome[:20]}".ljust(30)
        linha_prodito += f" {item.total:.2f}".rjust(10)
        lines.append(linha_produto)
    
    lines.append("-" * 40)
    lines.append(f"TOTAL:".ljust(30) + f" {venda.total:.2f}".rjust(10))
    lines.append("=" * 40)
    lines.append(f"{'OBRIGADO VOLTE SEMPRE!':^40}")
    lines.append("=" * 40)
    
    return "\n".join(lines)
