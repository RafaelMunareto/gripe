# Projeto de Previsão de Incidência de Síndrome Respiratória Aguda Grave

Este projeto utiliza dados de casos de Síndrome Respiratória Aguda Grave hospitalizados fornecidos pelo Ministério da Saúde para prever a incidência dessa condição por mês em diferentes regiões do Brasil. O objetivo é auxiliar no planejamento de respostas rápidas e prevenção de endemias.

## Fonte dos Dados

Os dados foram obtidos do portal OpenDataSUS para os anos de 2021, 2022 e 2023 e estão disponíveis [aqui](https://opendatasus.saude.gov.br/dataset/srag-2021-a-2023).

## Metodologia

O projeto segue a metodologia CRISP-DM, dividida nas seguintes etapas:

### 1. Entendimento do Negócio

Objetivo é prever a incidência de síndrome respiratória por um determinado período (mês) numa determinada região para auxiliar no planejamento de respostas a potenciais endemias.

### 2. Entendimento dos Dados

Análise realizada utilizando dados de 2021 a 2023 com as seguintes variáveis principais:

- DT_NOTIFICA (Data da Notificação)
- ANO (Extraído de DT_NOTIFICA)
- MES (Extraído de DT_NOTIFICA)
- SG_UF_NOT (Estado)
- CO_REGIONA (Código da Região)
- CO_MUN_NOT (Código do Município)
- CS_SEXO (Sexo do Paciente)
- DT_NASC (Data de Nascimento)
- NU_IDADE_N (Idade do Paciente)
- CS_GESTANT (Gestação em meses)
- CS_RACA (Raça do Paciente)

### 3. Preparação dos Dados

Unificação dos dados de três anos em um único DataFrame, tratamento de valores ausentes/nulos, criação de metadados, e categorização de variáveis categóricas.

### 4. Modelagem

- Aplicação de Random Forest e Gradient Boosting para métodos baseados em árvores.
- Utilização do KNN para explorar a influência de casos similares.
- Emprego da Rede Neural MLP para análise de relações complexas.
- Experimentação com Regressão Logística.
- Desenvolvimento de modelos híbridos a partir dos mais eficazes.

### 5. Avaliação

- Utilização do F1 Score, Matriz de Confusão e Acurácia.
- Avaliação qualitativa das previsões para validar a eficácia do modelo.

### 6. Implantação

- Desenvolvimento de um relatório ou dashboard interativo para visualização das projeções.
- Discussão sobre a aplicabilidade prática do modelo.

## Contato

Para mais informações, colaborações ou dúvidas, sinta-se à vontade para contatar o mantenedor do projeto rafael.munareto@icloud.com
