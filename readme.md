# Projeto: IssueMaster

# 1 - Detalhamento do Projeto

## Visão Geral

O **IssueMaster** é um agente de Inteligência Artificial desenvolvido para **maximizar a qualidade das descrições de chamados de TI**, atuando como um intermediário inteligente entre o usuário final e o sistema de abertura de chamados. O projeto tem como objetivo principal servir como um **MVP acadêmico** para um desafio de desenvolvimento de agentes de IA.

## Contexto do Problema

Atualmente, a empresa utiliza um sistema interno para abertura de chamados destinados ao setor de Tecnologia da Informação. Esses chamados são registrados por usuários de diferentes áreas, com variados níveis de conhecimento técnico.

Um problema recorrente é que muitos chamados são abertos com **descrições vagas, incompletas ou imprecisas**, dificultando o diagnóstico inicial por parte do time de suporte. Como consequência, os técnicos precisam entrar em contato com o usuário para coletar informações adicionais, o que gera:

- Aumento no tempo de atendimento
- Retrabalho para o suporte
- Frustração tanto para usuários quanto para técnicos

### Exemplo de Descrição Inadequada

> "Meu computador não funciona."
> 

Esse tipo de descrição não informa:

- Qual é o problema específico
- Quando o erro ocorre
- Se existe alguma mensagem de erro
- Qual impacto no trabalho do usuário

## Proposta de Solução

O **IssueMaster** propõe a criação de um **agente de IA** responsável por analisar, enriquecer e qualificar as descrições de chamados antes que eles sejam oficialmente abertos no sistema.

### Funcionamento Geral do Agente

1. O usuário descreve seu problema de forma livre.
2. O agente avalia a descrição com base em uma **estrutura padrão de chamado**, previamente definida.
3. A descrição é analisada quanto à clareza, completude e relevância das informações.
4. O chamado recebe uma **nota de 0 a 10**, indicando sua qualidade.

### Estrutura Padrão de Avaliação do Chamado

Para fins de avaliação, o agente verifica a presença (total ou parcial) dos seguintes elementos, quando aplicáveis:

- Tipo do chamado (incidente ou solicitação)
- Contexto/ambiente (equipamento, sistema, acesso)
- Descrição clara do problema
- Mensagens de erro ou evidências
- Momento ou frequência do problema
- Impacto no trabalho do usuário
- Ações já tentadas

Cada elemento contribui para a pontuação final, resultando em uma nota de **0 a 10**, onde:

- **0–4:** descrição insuficiente
- **5–7:** descrição aceitável
- **8–10:** descrição completa e bem estruturada

### Enriquecimento e Orientação ao Usuário

Com base na nota atribuída, o agente:

- Indica objetivamente quais informações precisam ser complementadas
- Sugere melhorias na descrição do chamado
- Quando aplicável, recomenda testes iniciais simples para tentativa de resolução

Caso os testes não resolvam o problema, o usuário poderá prosseguir com a abertura do chamado já com as informações corretas.

### Tratamento de Casos Sem Ação do Usuário

O agente identifica solicitações que não exigem testes ou ações do usuário (ex: criação de acessos ou usuários), ajustando os critérios de avaliação para não penalizar esse tipo de chamado.

## Benefícios Esperados

- Redução do tempo médio de atendimento
- Melhoria na qualidade dos chamados
- Menor necessidade de interação adicional entre suporte e usuário
- Padronização das informações recebidas pelo time de TI

## Arquitetura Proposta (MVP)

Para o escopo do desafio acadêmico, o IssueMaster será implementado com uma **arquitetura simplçes, de baixo custo e focada em prova de conceito**, composta pelas seguintes camadas:

- **Camada de Entrada:** interface web simples, onde o usuário descreve o problema em um campo de texto e interage diretamente com o agente.
- **Backend Leve:** responsável por receber a descrição, encaminhar o texto ao agente de IA, aplicar a lógica de avaliação e retornar a nota e orientações ao usuário.
- **Agente de IA:** utilização de modelos de linguagem acessados via **APIs gratuitas ou com créditos**, responsáveis pela análise da descrição, identificação de lacunas e atribuição da nota do chamado.
- **Persistência de Dados:** banco de dados leve e gratuito (ex: **SQLite**) para armazenamento básico de descrições, notas e histórico de interações, quando necessário.

Essa arquitetura permite validar o funcionamento do agente de IA sem dependência de infraestrutura complexa ou custos elevados, sendo adequada para um MVP acadêmico.

## Objetivo do MVP

Validar a viabilidade de um **agente de IA autônomo** capaz de avaliar descrições textuais, aplicar critérios de qualidade e orientar usuários antes da abertura de chamados, servindo como base para futuras evoluções e integrações com sistemas de ITSM.

# 2 - Tecnologias

## Frontend

**🔹 HTML + CSS + JavaScript + Bootstrap**

Utilizados para o desenvolvimento da interface web simples do sistema, responsável pela interação direta com o usuário, permitindo a entrada da descrição do chamado e a exibição da nota e do feedback gerado pelo agente de IA.

---

## Backend

**🔹 Python + FastAPI + Flask**

Responsável por receber as requisições da interface web, centralizar a lógica do sistema, orquestrar a comunicação com o agente de IA e gerenciar a persistência dos dados no banco.

> *Obs.: Flask pode ser citado como alternativa, porém o FastAPI é a opção principal.*
> 

---

## Agente de IA (LLM)

**🔹 Google Gemini**

- Modelos: **Gemini 1.5 Flash** ou **Gemini Pro**

Utilizado para análise da descrição do chamado, avaliação da qualidade das informações fornecidas, atribuição de nota e geração de orientações e sugestões ao usuário.

---

## Banco de Dados

**🔹 SQLite**

Banco de dados leve e gratuito, utilizado para armazenar as descrições dos chamados, as notas atribuídas e os feedbacks gerados pelo agente de IA, permitindo histórico e testes do MVP sem necessidade de infraestrutura adicional.

# 3 - Fluxo de Dados

- **Entrada do Usuário (Frontend)**
    
    O usuário acessa a interface web e insere livremente a descrição do problema no campo de texto destinado à abertura do chamado. Após finalizar a descrição, aciona o botão de análise.
    
- **Envio da Descrição ao Backend**
    
    A descrição é enviada do frontend para o backend por meio de uma requisição HTTP, iniciando o processo de análise.
    
- **Processamento no Backend**
    
    O backend recebe a descrição, realiza validações básicas (como verificação de texto vazio ou tamanho mínimo) e organiza os dados para envio ao agente de IA.
    
- **Análise pelo Agente de IA**
    
    A descrição é encaminhada ao agente de IA, que analisa o conteúdo textual com base nos critérios definidos, atribui uma nota de qualidade e gera feedbacks e sugestões de melhoria, quando aplicável.
    
- **Retorno do Resultado ao Backend**
    
    O agente de IA retorna ao backend a nota do chamado, o feedback gerado e as orientações sugeridas.
    
- **Persistência dos Dados (Opcional)**
    
    O backend armazena a descrição original, a nota e o feedback no banco de dados, possibilitando histórico, testes e análises futuras do MVP.
    
- **Exibição do Resultado ao Usuário (Frontend)**
    
    Por fim, o backend envia o resultado ao frontend, que exibe ao usuário, na mesma interface, a nota atribuída e o feedback do agente, sem necessidade de recarregar a página.
    

# 4 - Camadas do Sistema

- **Interface Web (Frontend)**
    - 1. Campo de Entrada (Descrição do Chamado)
    Campo onde o usuario digita o problema livremente como se estivesse abrindo um chamado real. Basicamente uma caixa de texto grande.
    Placeholder: “Descreva o problema com o máximo de detalhes possível”
    - 2. Ação de Envio
    Um botão simples, avaliar descrição. Após clicar no botão, um status sobre o processo como por exemplo "analisando descrição do chamado". O botão executa a funsao de enviar o texto ao backend e dispara o agente de IA.
    - 3. Área de Retorno (Resultado)
    Na mesma tela, o usuário recebe a nota do chamado de 0 a 10, um feedback do agente se está bom ou o que esta faltando e sugestões de melhorias ou testes(quando aplicavel). Tudo sem sair da mesma pagina.
- **Backend Leve**
    - **Receber a descrição do chamado** enviada pela interface web.
    - **Encaminhar a descrição ao agente de IA** para análise e avaliação.
    - **Receber a nota e o feedback** gerados pelo agente.
    - **Gerenciar a comunicação** entre frontend, agente de IA e banco de dados.
    - **Centralizar a lógica do sistema**, garantindo que cada etapa do fluxo ocorra na ordem correta.
- **Agente de IA**
    - O agente de IA é o **componente responsável pela inteligência do sistema**. Ele recebe a descrição do chamado enviada pelo backend e realiza a **análise do conteúdo textual**, avaliando a qualidade das informações fornecidas com base na estrutura definida para o chamado.
    - A partir dessa análise, o agente **atribui uma nota** que representa o nível de clareza e completude da descrição, além de **gerar orientações e sugestões** para que o usuário possa complementar ou melhorar o chamado antes de sua abertura.
- **Banco de Dados**
    - O banco de dados tem a função de **armazenar as descrições dos chamados, as notas atribuídas e as respostas geradas pelo agente de IA**. Seu uso no MVP é voltado principalmente para **registro e histórico das interações**, permitindo a realização de testes, validações e análises do funcionamento do sistema.
    - Por se tratar de um projeto acadêmico, é adotada uma solução **simples e gratuita**, suficiente para suportar o escopo do MVP sem adicionar complexidade desnecessária.

# 5 - Plano de Desenvolvimento

## Etapa 1 — Desenvolvimento do Frontend

- Criação da interface web simples
- Implementação:
    - Campo de texto para descrição do chamado
    - Botão de envio (“Avaliar descrição”)
    - Área de exibição da nota e feedback
- Integração básica com o backend via requisição HTTP
- Uso de Bootstrap para layout e usabilidade

---

## Etapa 2 — Desenvolvimento do Backend

- Criação da API utilizando FastAPI
- Implementação dos endpoints principais:
    - Recebimento da descrição do chamado
    - Encaminhamento ao agente de IA
    - Retorno da nota e feedback ao frontend
- Validações básicas da entrada
- Centralização da lógica do sistema

---

## Etapa 3 — Implementação do Agente de IA

- Integração com o modelo de linguagem escolhido (ex: Google Gemini)
- Definição do formato de entrada e saída do agente
- Implementação da lógica de:
    - Análise da descrição
    - Avaliação da qualidade
    - Atribuição de nota
    - Geração de feedback e sugestões
- Tratamento de casos que não exigem ação do usuário

---

## Etapa 4 — Persistência de Dados

- Configuração do banco de dados SQLite
- Definição da estrutura de armazenamento:
    - Descrição do chamado
    - Nota atribuída
    - Feedback gerado
    - Data/hora da análise
- Implementação do salvamento dos dados (quando necessário)

---

## Etapa 5 — Integração End-to-End

- Integração completa entre:
    - Frontend
    - Backend
    - Agente de IA
    - Banco de dados
- Testes do fluxo completo de dados
- Ajustes de comunicação entre as camadas

---

## Etapa 6 — Testes e Validação do MVP

- Testes com descrições de diferentes níveis de qualidade
- Avaliação da coerência das notas atribuídas
- Ajustes nos critérios de avaliação e feedbacks
- Validação do funcionamento geral do MVP
