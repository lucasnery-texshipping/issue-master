from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Inicializa a API
app = FastAPI(title="IssueMaster API")

# --- CONFIGURAÇÃO DE CORS ---
# Isso permite que o seu Frontend (que roda no navegador) converse com este Backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, restringe-se ao domínio do site. Para MVP, "*" libera geral.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- MODELOS DE DADOS (Pydantic) ---
# Define O QUE esperamos receber do Frontend. 
# Se vier algo diferente disso, o FastAPI rejeita automaticamente (Validação).
class ChamadoInput(BaseModel):
    descricao: str

# --- ROTAS ---

@app.get("/")
def health_check():
    """Rota apenas para verificar se o servidor está de pé."""
    return {"status": "online", "mensagem": "IssueMaster Backend rodando!"}

@app.post("/analisar_chamado")
def analisar_chamado(chamado: ChamadoInput):
    """
    Recebe a descrição, valida e retorna uma análise (Simulada por enquanto).
    """
    texto = chamado.descricao.strip()

    # 1. Validação Básica de Regra de Negócio
    if len(texto) < 10:
        raise HTTPException(status_code=400, detail="A descrição é muito curta. Detalhe mais o problema.")

    # 2. LOG: Mostra no terminal o que chegou (útil para debug)
    print(f"Recebido: {texto}")

    # 3. MOCK (Simulação da IA)
    # Na próxima etapa, substituiremos isso pela chamada ao Google Gemini.
    # Por enquanto, devolvemos uma resposta fixa para testar a conexão com o Front.
    
    return {
        "nota": 7.5,
        "feedback": "Resposta simulada do Backend! Recebemos seu texto com sucesso. A descrição parece boa, mas ainda não estamos usando a IA real.",
        "sugestoes": [
            "Verificar se o cabo de rede está conectado.",
            "Testar acesso via Wi-Fi.",
            "Reiniciar o equipamento."
        ]
    }

# Bloco para rodar via python backend/main.py (opcional, pois usaremos uvicorn via terminal)
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)