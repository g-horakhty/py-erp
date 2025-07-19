from escpos.printer import Network
from app.config import settings

def imprimir_cupom_direto(texto):
    try:
        # Configurar impressora de rede (substitua pelo IP da sua impressora)
        printer = Network(settings.IMPRESSORA_IP)
        
        # Configurar para 40 colunas
        printer.profile.profile_data['media']['width']['pixels'] = 40 * 8  # 8 pixels por coluna
        
        # Imprimir
        printer.text(texto)
        printer.cut()
        
    except Exception as e:
        print(f"Erro ao imprimir: {str(e)}")
        raise
