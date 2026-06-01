# Mission Control AI

## GS2026.1 - Pensamento Computacional e Automação com Python

## 1. Título do projeto

**Mission Control AI: Sistema Inteligente de Monitoramento de Missão Espacial**

## 2. Nome da missão

**Ares Sentinel One**

## 3. Nome da equipe

**Equipe Mission Control**

> Substitua pelos nomes reais antes de entregar, se necessário.

## 4. Integrantes

- Nome do integrante 1 - RM: XXXXX
- Nome do integrante 2 - RM: XXXXX
- Nome do integrante 3 - RM: XXXXX

## 5. Problema

Missões espaciais dependem de sistemas capazes de monitorar continuamente informações operacionais importantes, como temperatura, comunicação, bateria, oxigênio e estabilidade geral.

Caso algum desses indicadores apresente falha, a missão pode entrar em estado de atenção ou até em estado crítico. Por isso, é necessário ter um sistema que organize os dados, analise riscos e gere recomendações automáticas para apoiar a tomada de decisão.

## 6. Proposta da solução

O **Mission Control AI** é um sistema desenvolvido em Python que simula o monitoramento inteligente de uma missão espacial experimental.

O programa utiliza uma matriz chamada `dados_missao`, onde cada linha representa um ciclo da missão e cada coluna representa uma informação monitorada.

Cada ciclo possui os seguintes dados:

```python
[temperatura, comunicacao, bateria, oxigenio, estabilidade]
```

O sistema analisa cada ciclo, classifica os indicadores como **NORMAL**, **ATENÇÃO** ou **CRÍTICO**, calcula a pontuação de risco e exibe um relatório final no terminal.

## 7. Estrutura dos dados

A matriz principal do sistema é:

```python
dados_missao = [
    [23, 95, 91, 97, 92],
    [26, 86, 78, 94, 84],
    [32, 68, 61, 91, 73],
    [37, 48, 43, 86, 59],
    [40, 26, 18, 77, 34],
    [35, 52, 29, 83, 51],
    [30, 64, 45, 88, 66],
    [27, 72, 58, 92, 74]
]
```

Cada linha representa um ciclo de monitoramento da missão.

## 8. Áreas monitoradas

O sistema monitora cinco áreas principais:

1. Temperatura interna
2. Comunicação com a base
3. Sistema de energia
4. Suporte de oxigênio
5. Estabilidade operacional

Essas áreas estão diretamente relacionadas às colunas da matriz `dados_missao`.

## 9. Regras de alerta

### Temperatura

| Condição | Classificação |
|---|---|
| Menor que 18 °C | ATENÇÃO |
| De 18 °C até 30 °C | NORMAL |
| Maior que 30 °C até 35 °C | ATENÇÃO |
| Maior que 35 °C | CRÍTICO |

### Comunicação

| Condição | Classificação |
|---|---|
| Menor que 30% | CRÍTICO |
| De 30% até 59% | ATENÇÃO |
| 60% ou mais | NORMAL |

### Bateria

| Condição | Classificação |
|---|---|
| Menor que 20% | CRÍTICO |
| De 20% até 49% | ATENÇÃO |
| 50% ou mais | NORMAL |

### Oxigênio

| Condição | Classificação |
|---|---|
| Menor que 80% | CRÍTICO |
| De 80% até 89% | ATENÇÃO |
| 90% ou mais | NORMAL |

### Estabilidade

| Condição | Classificação |
|---|---|
| Menor que 40% | CRÍTICO |
| De 40% até 69% | ATENÇÃO |
| 70% ou mais | NORMAL |

## 10. Pontuação de risco

Cada classificação gera uma pontuação:

| Classificação | Pontuação |
|---|---|
| NORMAL | 0 ponto |
| ATENÇÃO | 1 ponto |
| CRÍTICO | 2 pontos |

Como cada ciclo possui 5 informações monitoradas, a pontuação máxima de risco por ciclo é 10 pontos.

## 11. Classificação do ciclo

| Pontuação total | Classificação |
|---|---|
| 0 a 2 pontos | MISSÃO ESTÁVEL |
| 3 a 5 pontos | MISSÃO EM ATENÇÃO |
| 6 a 10 pontos | MISSÃO CRÍTICA |

## 12. Funcionalidades implementadas

O sistema possui:

- nome da missão;
- nome da equipe;
- matriz `dados_missao` com 8 ciclos;
- lista de áreas monitoradas;
- funções para analisar temperatura, comunicação, bateria, oxigênio e estabilidade;
- cálculo de risco por ciclo;
- classificação automática de cada ciclo;
- geração de recomendações automáticas;
- análise da tendência da missão;
- identificação da área mais afetada;
- relatório final exibido no terminal.

## 13. Principais funções

O arquivo `mission_control.py` contém as seguintes funções:

- `analisar_temperatura()`
- `analisar_comunicacao()`
- `analisar_bateria()`
- `analisar_oxigenio()`
- `analisar_estabilidade()`
- `classificar_ciclo()`
- `gerar_recomendacao()`
- `analisar_ciclo()`
- `analisar_tendencia()`
- `identificar_area_mais_afetada()`
- `calcular_medias()`
- `gerar_relatorio_final()`
- `executar_monitoramento()`

## 14. Como executar o projeto

### Pré-requisitos

É necessário ter o Python instalado na máquina.

O projeto não utiliza bibliotecas externas.

### Passo a passo

Clone ou baixe o repositório:

```bash
git clone https://github.com/SEU-USUARIO/mission-control-ai.git
```

Acesse a pasta do projeto:

```bash
cd mission-control-ai
```

Execute o arquivo principal:

```bash
python mission_control.py
```

ou, dependendo da instalação:

```bash
python3 mission_control.py
```

## 15. Saída esperada

Ao executar o sistema, o terminal exibirá:

- cabeçalho da missão;
- análise detalhada de cada ciclo;
- classificação dos indicadores;
- pontuação de risco;
- recomendação automática;
- relatório final da missão;
- médias dos indicadores;
- ciclo mais crítico;
- tendência da missão;
- área mais afetada;
- classificação final;
- conclusão.

## 16. Tecnologias utilizadas

- Python
- GitHub
- Lógica de programação
- Matrizes
- Listas
- Funções
- Estruturas condicionais
- Estruturas de repetição

## 17. Conclusão

O **Mission Control AI** simula um sistema básico de apoio ao controle de uma missão espacial. A solução utiliza regras lógicas para analisar dados simulados, identificar riscos e apresentar informações úteis para tomada de decisão.

Mesmo sem utilizar bibliotecas externas ou machine learning, o projeto demonstra como estruturas fundamentais de programação podem ser aplicadas em um cenário de monitoramento inteligente.
