# 🤖 IssueMaster

> **MVP Acadêmico** - Agente de Inteligência Artificial para Qualificação de Chamados de TI.

## 📋 Visão Geral

O **IssueMaster** é um agente de Inteligência Artificial desenvolvido para maximizar a qualidade das descrições de chamados de TI, atuando como um intermediário inteligente entre o usuário final e o sistema de abertura de chamados.

O objetivo deste MVP é validar a viabilidade de um agente autônomo capaz de avaliar descrições textuais, aplicar critérios de qualidade e orientar usuários *antes* da abertura oficial do chamado, reduzindo o retrabalho do time de suporte.

---

## 🎯 O Problema

Atualmente, muitos chamados são abertos com descrições vagas (ex: *"Meu computador não funciona"*), o que gera:
* ⏳ **Aumento no tempo de atendimento:** Técnicos precisam contatar o usuário para entender o erro.
* 🔄 **Retrabalho:** Diagnósticos iniciais incorretos.
* 😫 **Frustração:** Tanto para usuários quanto para a equipe de TI.

## 💡 A Solução

O IssueMaster analisa o texto do usuário em tempo real, verificando clareza, completude e relevância.

1.  **Entrada:** O usuário descreve o problema livremente.
2.  **Análise:** A IA avalia o texto com base em uma estrutura padrão (Sintomas, Contexto, Erros, Impacto).
3.  **Pontuação:** O chamado recebe uma nota de **0 a 10**.
4.  **Feedback:** O agente sugere complementos ou testes iniciais (ex: reiniciar, verificar cabos) antes de submeter o chamado.

---

## 🧠 Critérios de Avaliação (IA)

O agente utiliza o **Google Gemini** para verificar a presença dos seguintes elementos:

* [x] Tipo do chamado (Incidente ou Solicitação)
* [x] Contexto/Ambiente (Equipamento, Sistema, Acesso)
* [x] Descrição clara do problema
* [x] Mensagens de erro ou evidências
* [x] Momento ou frequência da ocorrência
* [x] Impacto no trabalho
* [x] Ações já tentadas pelo usuário

### Escala de Qualidade
| Nota | Classificação | Ação do Sistema |
| :--- | :--- | :--- |
| **0 – 4** | Insuficiente | Bloqueia/Alerta e pede informações vitais. |
| **5 – 7** | Aceitável | Sugere melhorias para agilizar o atendimento. |
| **8 – 10** | Completa | Descrição ideal, pronto para envio. |

---

## 🛠️ Tecnologias Utilizadas

### Frontend
* **HTML5, CSS3, JavaScript** (Vanilla)
* **Bootstrap 5** (Layout e Responsividade)

### Backend
* **Python 3.x**
* **FastAPI** (Framework principal de API)
* **Uvicorn** (Servidor ASGI)

### Inteligência Artificial
* **Google Gemini API** (Modelos: Gemini 1.5 Flash ou Pro)

### Persistência (Opcional no MVP)
* **SQLite** (Histórico de análises e logs)

---

## 🏗️ Arquitetura do Sistema

O sistema segue uma arquitetura leve focada em Prova de Conceito (PoC):

1.  **Interface Web:** Campo de texto simples para interação direta.
2.  **Backend (FastAPI):** Recebe o texto, valida e orquestra a chamada à IA.
3.  **Agente de IA:** Processa o texto via Prompt Engineering e retorna JSON estruturado (Nota + Feedback).
4.  **Banco de Dados:** Registra a interação para métricas futuras.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

### 1. Clonar o repositório
```bash
git clone [https://github.com/seu-usuario/issuemaster.git](https://github.com/seu-usuario/issuemaster.git)
cd issuemaster

* **Python 3.8+** instalado.
* **Chave de API do Google Gemini** (Obtida no [Google AI Studio](https://aistudio.google.com/)).

---

## 🚀 Guia de Instalação e Execução

Siga os passos abaixo sequencialmente no seu terminal para configurar o ambiente.

### 1. Clonar o repositório
Baixe o código para sua máquina e entre na pasta do projeto:

```bash
git clone [https://github.com/seu-usuario/issuemaster.git](https://github.com/seu-usuario/issuemaster.git)
cd issuemaster