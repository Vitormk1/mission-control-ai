# Mission Control AI
# GS2026.1 - Pensamento Computacional e Automação com Python
# Sistema Inteligente de Monitoramento de Missão Espacial

NOME_MISSAO = "Ares Sentinel One"
NOME_EQUIPE = "Equipe Mission Control"

# Matriz principal do projeto.
# Ordem obrigatória de cada ciclo:
# [temperatura, comunicacao, bateria, oxigenio, estabilidade]
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

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]


def pontuacao_por_classificacao(classificacao):
    """Converte a classificação textual em pontuação de risco."""
    if classificacao == "NORMAL":
        return 0
    if classificacao == "ATENÇÃO":
        return 1
    return 2


def analisar_temperatura(temperatura):
    """Analisa a temperatura interna do módulo espacial."""
    if temperatura < 18:
        return "ATENÇÃO", "Temperatura abaixo do ideal"
    if temperatura <= 30:
        return "NORMAL", "Temperatura estável"
    if temperatura <= 35:
        return "ATENÇÃO", "Temperatura elevada"
    return "CRÍTICO", "Risco de superaquecimento"


def analisar_comunicacao(comunicacao):
    """Analisa a qualidade da comunicação com a base."""
    if comunicacao < 30:
        return "CRÍTICO", "Comunicação com a base em nível crítico"
    if comunicacao <= 59:
        return "ATENÇÃO", "Comunicação instável"
    return "NORMAL", "Comunicação estável"


def analisar_bateria(bateria):
    """Analisa o nível de bateria da missão."""
    if bateria < 20:
        return "CRÍTICO", "Bateria em nível crítico"
    if bateria <= 49:
        return "ATENÇÃO", "Bateria abaixo do recomendado"
    return "NORMAL", "Energia estável"


def analisar_oxigenio(oxigenio):
    """Analisa o suporte de oxigênio disponível."""
    if oxigenio < 80:
        return "CRÍTICO", "Oxigênio em nível crítico"
    if oxigenio <= 89:
        return "ATENÇÃO", "Oxigênio abaixo do ideal"
    return "NORMAL", "Oxigênio adequado"


def analisar_estabilidade(estabilidade):
    """Analisa a estabilidade operacional dos sistemas."""
    if estabilidade < 40:
        return "CRÍTICO", "Estabilidade operacional crítica"
    if estabilidade <= 69:
        return "ATENÇÃO", "Estabilidade operacional reduzida"
    return "NORMAL", "Estabilidade operacional adequada"


def classificar_ciclo(pontuacao_total):
    """Classifica a situação geral do ciclo conforme a pontuação de risco."""
    if pontuacao_total <= 2:
        return "MISSÃO ESTÁVEL"
    if pontuacao_total <= 5:
        return "MISSÃO EM ATENÇÃO"
    return "MISSÃO CRÍTICA"


def gerar_recomendacao(analises, pontuacao_total):
    """Gera recomendação automática com base nos alertas encontrados no ciclo."""
    classificacoes = [item["classificacao"] for item in analises]
    areas_criticas = [
        item["area"] for item in analises if item["classificacao"] == "CRÍTICO"
    ]
    areas_atencao = [
        item["area"] for item in analises if item["classificacao"] == "ATENÇÃO"
    ]

    if pontuacao_total == 0:
        return "Manter operação normal e continuar monitoramento."

    if len(areas_criticas) >= 3:
        return (
            "Ativar modo de segurança, reduzir operações não essenciais e priorizar "
            "energia, comunicação e suporte à vida."
        )

    if "Temperatura interna" in areas_criticas:
        return "Verificar imediatamente o controle térmico da missão."

    if "Comunicação com a base" in areas_criticas:
        return "Tentar restabelecer contato com a base e usar canal reserva."

    if "Sistema de energia" in areas_criticas:
        return "Ativar modo de economia de energia e desligar sistemas secundários."

    if "Suporte de oxigênio" in areas_criticas:
        return "Acionar protocolo de suporte à vida e verificar reservas de oxigênio."

    if "Estabilidade operacional" in areas_criticas:
        return "Reduzir operações não essenciais e estabilizar os sistemas principais."

    if "CRÍTICO" in classificacoes:
        return "Executar protocolo de contingência para os sistemas críticos."

    if areas_atencao:
        return "Monitorar sistemas em atenção e preparar plano de contingência."

    return "Continuar acompanhamento da missão."


def analisar_ciclo(ciclo):
    """Analisa um ciclo completo da missão."""
    temperatura, comunicacao, bateria, oxigenio, estabilidade = ciclo

    resultados = [
        ("Temperatura interna", "Temperatura", temperatura, "°C", analisar_temperatura(temperatura)),
        ("Comunicação com a base", "Comunicação", comunicacao, "%", analisar_comunicacao(comunicacao)),
        ("Sistema de energia", "Bateria", bateria, "%", analisar_bateria(bateria)),
        ("Suporte de oxigênio", "Oxigênio", oxigenio, "%", analisar_oxigenio(oxigenio)),
        ("Estabilidade operacional", "Estabilidade", estabilidade, "%", analisar_estabilidade(estabilidade)),
    ]

    analises = []

    for area, nome, valor, unidade, resultado in resultados:
        classificacao, mensagem = resultado
        risco = pontuacao_por_classificacao(classificacao)

        analises.append({
            "area": area,
            "nome": nome,
            "valor": valor,
            "unidade": unidade,
            "classificacao": classificacao,
            "mensagem": mensagem,
            "risco": risco
        })

    pontuacao_total = sum(item["risco"] for item in analises)
    classificacao_ciclo = classificar_ciclo(pontuacao_total)
    recomendacao = gerar_recomendacao(analises, pontuacao_total)

    return {
        "analises": analises,
        "pontuacao_total": pontuacao_total,
        "classificacao_ciclo": classificacao_ciclo,
        "recomendacao": recomendacao
    }


def analisar_tendencia(riscos_por_ciclo):
    """Compara o primeiro e o último ciclo para identificar a tendência."""
    primeiro_risco = riscos_por_ciclo[0]
    ultimo_risco = riscos_por_ciclo[-1]

    if ultimo_risco > primeiro_risco:
        return "A missão apresentou tendência de piora."
    if ultimo_risco < primeiro_risco:
        return "A missão apresentou tendência de melhora."
    return "A missão permaneceu estável em relação ao início."


def identificar_area_mais_afetada(pontuacao_por_area):
    """Identifica a área com maior pontuação acumulada de risco."""
    maior_risco = max(pontuacao_por_area)
    indice_maior_risco = pontuacao_por_area.index(maior_risco)
    return areas_monitoradas[indice_maior_risco], maior_risco


def calcular_medias():
    """Calcula as médias gerais de cada informação monitorada."""
    quantidade_ciclos = len(dados_missao)

    media_temperatura = sum(ciclo[0] for ciclo in dados_missao) / quantidade_ciclos
    media_comunicacao = sum(ciclo[1] for ciclo in dados_missao) / quantidade_ciclos
    media_bateria = sum(ciclo[2] for ciclo in dados_missao) / quantidade_ciclos
    media_oxigenio = sum(ciclo[3] for ciclo in dados_missao) / quantidade_ciclos
    media_estabilidade = sum(ciclo[4] for ciclo in dados_missao) / quantidade_ciclos

    return {
        "temperatura": media_temperatura,
        "comunicacao": media_comunicacao,
        "bateria": media_bateria,
        "oxigenio": media_oxigenio,
        "estabilidade": media_estabilidade
    }


def classificar_missao_final(risco_medio):
    """Classifica a missão com base no risco médio."""
    if risco_medio <= 2:
        return "MISSÃO ESTÁVEL"
    if risco_medio <= 5:
        return "MISSÃO EM ATENÇÃO"
    return "MISSÃO CRÍTICA"


def gerar_conclusao(classificacao_final, tendencia, ciclos_criticos):
    """Gera a conclusão final da missão."""
    if classificacao_final == "MISSÃO ESTÁVEL":
        return (
            "A missão manteve boa condição operacional. Os sistemas devem continuar "
            "sendo monitorados para evitar falhas futuras."
        )

    if classificacao_final == "MISSÃO CRÍTICA":
        return (
            "A missão apresentou risco elevado. A equipe deve manter o modo de "
            "segurança ativo, priorizar sistemas vitais e executar ações corretivas."
        )

    if "melhora" in tendencia and ciclos_criticos > 0:
        return (
            "A missão passou por instabilidade relevante, mas apresentou recuperação "
            "parcial. A equipe deve manter o plano de contingência ativo."
        )

    return (
        "A missão apresentou pontos de atenção durante a operação. É necessário "
        "acompanhar os sistemas instáveis e manter protocolos preventivos."
    )


def exibir_cabecalho():
    """Exibe o cabeçalho inicial do sistema."""
    print("=" * 70)
    print("MISSION CONTROL AI")
    print("=" * 70)
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print("=" * 70)


def gerar_relatorio_final(resultados_ciclos, riscos_por_ciclo, pontuacao_por_area):
    """Exibe o relatório final consolidado da missão."""
    medias = calcular_medias()

    maior_risco = max(riscos_por_ciclo)
    ciclo_mais_critico = riscos_por_ciclo.index(maior_risco) + 1
    risco_medio = sum(riscos_por_ciclo) / len(riscos_por_ciclo)
    ciclos_criticos = sum(1 for risco in riscos_por_ciclo if classificar_ciclo(risco) == "MISSÃO CRÍTICA")

    tendencia = analisar_tendencia(riscos_por_ciclo)
    area_mais_afetada, maior_risco_area = identificar_area_mais_afetada(pontuacao_por_area)
    classificacao_final = classificar_missao_final(risco_medio)
    conclusao = gerar_conclusao(classificacao_final, tendencia, ciclos_criticos)

    print("=" * 70)
    print("RELATÓRIO FINAL DA MISSÃO")
    print("=" * 70)
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print(f"Média de temperatura: {medias['temperatura']:.2f} °C")
    print(f"Média de comunicação: {medias['comunicacao']:.2f}%")
    print(f"Média de bateria: {medias['bateria']:.2f}%")
    print(f"Média de oxigênio: {medias['oxigenio']:.2f}%")
    print(f"Média de estabilidade: {medias['estabilidade']:.2f}%")
    print(f"Ciclo mais crítico: Ciclo {ciclo_mais_critico}")
    print(f"Maior pontuação de risco: {maior_risco}")
    print(f"Risco médio da missão: {risco_medio:.2f}")
    print(f"Quantidade de ciclos críticos: {ciclos_criticos}")

    print("\nTendência da missão:")
    print(tendencia)

    print("\nPontuação acumulada por área:")
    for indice, area in enumerate(areas_monitoradas):
        print(f"{area}: {pontuacao_por_area[indice]} pontos")

    print("\nÁrea mais afetada:")
    print(f"{area_mais_afetada} ({maior_risco_area} pontos)")

    print("\nClassificação final da missão:")
    print(classificacao_final)

    print("\nConclusão:")
    print(conclusao)


def executar_monitoramento():
    """Executa a análise completa da missão."""
    exibir_cabecalho()

    riscos_por_ciclo = []
    pontuacao_por_area = [0, 0, 0, 0, 0]
    resultados_ciclos = []

    for indice, ciclo in enumerate(dados_missao):
        resultado = analisar_ciclo(ciclo)
        resultados_ciclos.append(resultado)
        riscos_por_ciclo.append(resultado["pontuacao_total"])

        print(f"\nCICLO {indice + 1}")
        print("-" * 70)

        for posicao_area, analise in enumerate(resultado["analises"]):
            pontuacao_por_area[posicao_area] += analise["risco"]

            print(
                f"{analise['nome']}: {analise['valor']}{analise['unidade']} | "
                f"{analise['classificacao']} | {analise['mensagem']}"
            )

        print(f"Pontuação de risco do ciclo: {resultado['pontuacao_total']}")
        print(f"Classificação do ciclo: {resultado['classificacao_ciclo']}")
        print(f"Recomendação: {resultado['recomendacao']}")

    print()
    gerar_relatorio_final(resultados_ciclos, riscos_por_ciclo, pontuacao_por_area)


if __name__ == "__main__":
    executar_monitoramento()
