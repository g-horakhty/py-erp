# 🚀 py-erp - Sistema ERP Modular em Python

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

**py-erp** é um sistema ERP modular e leve, desenvolvido com **FastAPI** e **SQLite**, voltado para gestão comercial em redes locais. O projeto ainda está em estágio inicial e **não está pronto para ambientes de produção**.

## ⚠️ Aviso Importante

❗ **Status Experimental**  
Este software encontra-se em fase de desenvolvimento ativo, com funcionalidades parciais e instabilidade conhecida em ambientes concorrentes.

🔒 **Recomendações de Uso**:
- Apenas para **testes e desenvolvimento**
- **Não utilizar** em ambientes de produção
- Dados críticos devem ter **backup regular**

## 🌟 Principais Características

| Módulo         | Status       | Descrição                          |
|----------------|-------------|-----------------------------------|
| 💻 FastAPI Backend | ✅ Estável   | API moderna e assíncrona          |
| 🗃️ SQLite Database | ⚠️ Limitado | Ideal para desenvolvimento        |
| 📦 Módulo Estoque  | ⏳ Parcial   | Gestão básica de inventário       |
| 🛒 Módulo Vendas   | ⏳ Parcial   | Processo de vendas inicial        |
| 👥 Módulo Clientes | ⏳ Parcial   | Cadastro de clientes básico       |

## 🔍 Análise de Estabilidade
Pontos Fortes:

- ✅ Rápido desenvolvimento

- ✅ Fácil configuração

- ✅ Ideal para prototipagem

Limitações Atuais:

- ⚠️ SQLite não suporta alta concorrência

- ⚠️ Falta sistema de autenticação robusto

- ⚠️ Sem pooling de conexões

## 🚀 Começando
Pré-requisitos
- Python 3.10+

- pip

- Git (opcional)

### Instalação
```sh
# Clone o repositório
git clone https://github.com/g-horakhty/py-erp.git
cd py-erp

# Crie um ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt
```

## Execução
```sh
# Modo desenvolvimento (com reload)
uvicorn main:app --reload

# Modo produção (2 workers)
uvicorn main:app --workers 2 --host 0.0.0.0 --port 8000
```

### 👨💻 Autor
Gabriel Horakhty
![GitHub](https://img.shields.io/badge/github-%2523121011.svg?style=for-the-badge&logo=github&logoColor=white)
![LinkedIn](https://img.shields.io/badge/linkedin-%25230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)

# 📝 Licença
GNU AFFERO GENERAL PUBLIC LICENSE (AGPL-3.0)
