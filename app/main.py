from fastapi import FastAPI
from app.api.endpoints import auth

app = FastAPI()

# Inclui as rotas de autenticação com o prefixo e tags definidos
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
