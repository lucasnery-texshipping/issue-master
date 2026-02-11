import requests
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from dotenv import load_dotenv

# 1. Carrega variáveis de ambiente
load_dotenv()

# Pega a URL do n8n
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")

# --- INICIALIZAÇÃO DA API ---
app = FastAPI(title="IssueMaster Proxy -> n8n")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChamadoInput(BaseModel):
    descricao: str

# --- ROTA PRINCIPAL ---
@app.post("/analisar_chamado")
def analisar_chamado(chamado: ChamadoInput):
    print(f"📥 Recebido do Front: {chamado.descricao}")

    # Validação de segurança básica
    if not N8N_WEBHOOK_URL:
        raise HTTPException(status_code=500, detail="URL do n8n não configurada no servidor.")

    try:
        # 1. Envia o texto para o n8n (POST)
        print("📡 Enviando para o n8n...")
        
        # Enviamos um JSON simples: {"descricao": "texto do usuario"}
        response = requests.post(
            N8N_WEBHOOK_URL, 
            json={"descricao": chamado.descricao},
            timeout=40 # Tempo limite de espera (40s) para a IA pensar
        )
        
        # Verifica se o n8n retornou erro (ex: 404, 500)
        response.raise_for_status()
        
        # 2. Pega a resposta do n8n (que já deve vir no formato JSON correto)
        dados_n8n = response.json()
        print("🤖 Resposta recebida do n8n:", dados_n8n)

        # 3. Devolve direto para o Frontend
        return dados_n8n

    except requests.exceptions.Timeout:
        raise HTTPException(status_code=504, detail="O n8n demorou muito para responder.")
    except requests.exceptions.ConnectionError:
        raise HTTPException(status_code=502, detail="Não foi possível conectar ao n8n. Verifique se ele está rodando.")
    except Exception as e:
        print(f"Erro: {e}")
        raise HTTPException(status_code=500, detail="Erro interno ao processar solicitação.")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)