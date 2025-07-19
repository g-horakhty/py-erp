from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from app.routes import produtos, vendas, relatorios, web
from app.database import engine, Base

app = FastAPI(title="ERP de Vendas Local", version="2.0")

# Configuração CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar arquivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates
templates = Jinja2Templates(directory="app/templates")

# Criar tabelas
Base.metadata.create_all(bind=engine)

# Rotas API
app.include_router(produtos.router, prefix="/api/produtos")
app.include_router(vendas.router, prefix="/api/vendas")
app.include_router(relatorios.router, prefix="/api/relatorios")

# Rotas Web
app.include_router(web.router)

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})