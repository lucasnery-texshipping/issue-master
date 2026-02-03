# Detalhamento do Projeto: IssueMaster

## 1. Detalhamento do Projeto

### Visão Geral
O **IssueMaster** é um agente de Inteligência Artificial desenvolvido para maximizar a qualidade das descrições de chamados de TI, atuando como um intermediário inteligente entre o usuário final e o sistema de abertura de chamados. O projeto tem como objetivo principal servir como um MVP acadêmico para um desafio de desenvolvimento de agentes de IA.

### Contexto do Problema
Atualmente, a empresa utiliza um sistema interno para abertura de chamados destinados ao setor de Tecnologia da Informação. Esses chamados são registrados por usuários de diferentes áreas, com variados níveis de conhecimento técnico.

Um problema recorrente é que muitos chamados são abertos com descrições vagas, incompletas ou imprecisas, dificultando o diagnóstico inicial por parte do time de suporte. Como consequência, os técnicos precisam entrar em contato com o usuário para coletar informações adicionais, o que gera:
* Aumento no tempo de atendimento
* Retrabalho para o suporte
* Frustração tanto para usuários quanto para técnicos

#### Exemplo de Descrição Inadequada
> *"Meu computador não funciona."*

Esse tipo de descrição não informa:
* Qual é o problema específico
* Quando o erro ocorre
* Se existe alguma mensagem de erro
* Qual impacto no trabalho do usuário

### Proposta de Solução
O IssueMaster propõe a criação de um agente de IA responsável por analisar, enriquecer e qualificar as descrições de chamados antes que eles sejam oficialmente abertos no sistema.

#### Funcionamento Geral do Agente
1.  O usuário descreve seu problema de forma livre.
2.  O agente avalia a descrição com base em uma estrutura padrão de chamado, previamente definida.
3.  A descrição é analisada quanto à clareza, completude e relevância das informações.
4.  O chamado recebe uma nota de **0 a 10**, indicando sua qualidade.

### Estrutura Padrão de Avaliação do Chamado
Para fins de avaliação, o agente verifica a presença (total ou parcial) dos seguintes elementos, quando aplicáveis:
* Tipo do chamado (incidente ou solicitação)
* Contexto/ambiente (equipamento, sistema, acesso)
* Descrição clara do problema
* Mensagens de erro ou evidências
* Momento ou frequência do problema
* Impacto no trabalho do usuário
* Ações já tentadas

Cada elemento contribui para a pontuação final, resultando em uma nota de 0 a 10, onde:
* **0–4:** Descrição insuficiente
* **5–7:** Descrição aceitável
* **8–10:** Descrição completa e bem estruturada

### Enriquecimento e Orientação ao Usuário
Com base na nota atribuída, o agente:
* Indica objetivamente quais informações precisam ser complementadas.
* Sugere melhorias na descrição do chamado.
* Quando aplicável, recomenda testes iniciais simples para tentativa de resolução.

Caso os testes não resolvam o problema, o usuário poderá prosseguir com a abertura do chamado já com as informações corretas.

**Tratamento de Casos Sem Ação do Usuário:** O agente identifica solicitações que não exigem testes ou ações do usuário (ex: criação de acessos ou usuários), ajustando os critérios de avaliação para não penalizar esse tipo de chamado.

### Benefícios Esperados
* Redução do tempo médio de atendimento.
* Melhoria na qualidade dos chamados.
* Menor necessidade de interação adicional entre suporte e usuário.
* Padronização das informações recebidas pelo time de TI.

### Arquitetura Proposta (MVP)
Para o escopo do desafio acadêmico, o IssueMaster será implementado com uma arquitetura simples, de baixo custo e focada em prova de conceito, composta pelas seguintes camadas:

1.  **Camada de Entrada:** Interface web simples, onde o usuário descreve o problema em um campo de texto e interage diretamente com o agente.
2.  **Backend Leve:** Responsável por receber a descrição, encaminhar o texto ao agente de IA, aplicar a lógica de avaliação e retornar a nota e orientações ao usuário.
3.  **Agente de IA:** Utilização de modelos de linguagem acessados via APIs gratuitas ou com créditos, responsáveis pela análise da descrição, identificação de lacunas e atribuição da nota do chamado.
4.  **Persistência de Dados:** Banco de dados leve e gratuito (ex: SQLite) para armazenamento básico de descrições, notas e histórico de interações, quando necessário.

Essa arquitetura permite validar o funcionamento do agente de IA sem dependência de infraestrutura complexa ou custos elevados.

---

## 2. Tecnologias

### Frontend
🔹 **HTML + CSS + JavaScript + Bootstrap**
Utilizados para o desenvolvimento da interface web simples do sistema, responsável pela interação direta com o usuário, permitindo a entrada da descrição do chamado e a exibição da nota e do feedback gerado pelo agente de IA.

### Backend
🔹 **Python + FastAPI + Flask**
Responsável por receber as requisições da interface web, centralizar a lógica do sistema, orquestrar a comunicação com o agente de IA e gerenciar a persistência dos dados no banco.
*(Obs.: Flask pode ser citado como alternativa, porém o FastAPI é a opção
