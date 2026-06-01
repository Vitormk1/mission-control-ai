# Roteiro do vídeo pitch - Mission Control AI

Tempo máximo recomendado: até 3 minutos.

## 0:00 a 0:20 - Apresentação

Olá, somos a Equipe Mission Control, e este é o projeto Mission Control AI, desenvolvido para a GS2026.1 de Pensamento Computacional e Automação com Python.

O objetivo do projeto é simular um sistema inteligente de monitoramento de uma missão espacial experimental.

## 0:20 a 0:50 - Problema

Durante uma missão espacial, vários sistemas precisam ser acompanhados o tempo todo.

Temperatura, comunicação, bateria, oxigênio e estabilidade operacional são fatores que podem afetar diretamente a segurança da missão.

Se uma dessas áreas apresentar falha, a equipe precisa identificar rapidamente o risco e tomar decisões.

## 0:50 a 1:30 - Solução

Para resolver esse problema, criamos um programa em Python chamado Mission Control AI.

O sistema usa uma matriz chamada dados_missao, onde cada linha representa um ciclo da missão e cada coluna representa uma informação monitorada.

Cada ciclo possui temperatura, comunicação, bateria, oxigênio e estabilidade.

O programa percorre os ciclos, analisa os dados, classifica cada área como normal, atenção ou crítico, e calcula a pontuação de risco.

## 1:30 a 2:10 - Funcionamento

A pontuação funciona assim:

Normal vale 0 ponto.
Atenção vale 1 ponto.
Crítico vale 2 pontos.

Como cada ciclo tem cinco informações, o risco máximo de um ciclo é 10 pontos.

Com isso, o sistema classifica o ciclo como missão estável, missão em atenção ou missão crítica.

Além disso, ele gera recomendações automáticas, como ativar modo de economia de energia, verificar controle térmico ou acionar protocolo de suporte à vida.

## 2:10 a 2:40 - Relatório final

No final da execução, o sistema mostra um relatório completo no terminal.

Esse relatório apresenta as médias dos indicadores, o ciclo mais crítico, o risco médio da missão, a tendência da missão e a área mais afetada.

Assim, a equipe consegue entender se a missão melhorou, piorou ou permaneceu estável.

## 2:40 a 3:00 - Encerramento

O Mission Control AI demonstra como conceitos fundamentais de Python, como matrizes, listas, funções, repetição e condicionais, podem ser usados para criar um sistema de análise e apoio à decisão.

Obrigado.
