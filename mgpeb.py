# ============================================================
# MGPEB - Modulo de Gerenciamento de Pouso e Estabilizacao de Base
# Atividade Integradora FIAP
# ============================================================


# ------------------------------------------------------------
# Cadastro dos modulos
# ------------------------------------------------------------

modulos = [
    {
        "id": "POWER-NUC-01",
        "nome": "Reator Nuclear",
        "tipo": "energia",
        "prioridade": 1,
        "combustivel": 100,
        "massa": 6000,
        "criticidade": "MAXIMA",
        "horario_chegada_orbita": "2031-01-10T05:00",
        "dependencia": None,
    },
    {
        "id": "RAD-NUC-01",
        "nome": "Radiadores do Reator",
        "tipo": "infraestrutura",
        "prioridade": 1,
        "combustivel": 95,
        "massa": 1000,
        "criticidade": "MAXIMA",
        "horario_chegada_orbita": "2031-01-10T05:30",
        "dependencia": "POWER-NUC-01",
    },
    {
        "id": "PWR-DIST-01",
        "nome": "Terminal de Distribuicao",
        "tipo": "energia",
        "prioridade": 1,
        "combustivel": 95,
        "massa": 600,
        "criticidade": "MAXIMA",
        "horario_chegada_orbita": "2031-01-15T07:00",
        "dependencia": "POWER-NUC-01",
    },
    {
        "id": "COM-RELAY-01",
        "nome": "Relay de Comunicacoes",
        "tipo": "comunicacao",
        "prioridade": 1,
        "combustivel": 93,
        "massa": 1200,
        "criticidade": "MAXIMA",
        "horario_chegada_orbita": "2031-01-12T06:00",
        "dependencia": "POWER-NUC-01",
    },
    {
        "id": "LSMS-01",
        "nome": "Guindaste de Superficie",
        "tipo": "construcao",
        "prioridade": 1,
        "combustivel": 88,
        "massa": 2000,
        "criticidade": "ALTA",
        "horario_chegada_orbita": "2031-01-18T06:00",
        "dependencia": "PWR-DIST-01",
    },
    {
        "id": "ATHLETE-01",
        "nome": "Robo Hexapode",
        "tipo": "construcao",
        "prioridade": 1,
        "combustivel": 85,
        "massa": 900,
        "criticidade": "ALTA",
        "horario_chegada_orbita": "2031-02-05T10:00",
        "dependencia": "PWR-DIST-01",
    },
    {
        "id": "MTV-01",
        "nome": "Rover de Terreno A",
        "tipo": "mobilidade",
        "prioridade": 1,
        "combustivel": 91,
        "massa": 900,
        "criticidade": "ALTA",
        "horario_chegada_orbita": "2031-01-25T11:00",
        "dependencia": "PWR-DIST-01",
    },
    {
        "id": "RASSOR-01",
        "nome": "Robo Escavador A",
        "tipo": "construcao",
        "prioridade": 2,
        "combustivel": 87,
        "massa": 45,
        "criticidade": "MEDIA",
        "horario_chegada_orbita": "2031-02-01T08:00",
        "dependencia": "PWR-DIST-01",
    },
    {
        "id": "ISRU-ALPHA-01",
        "nome": "Planta ISRU",
        "tipo": "isru",
        "prioridade": 1,
        "combustivel": 89,
        "massa": 5000,
        "criticidade": "ALTA",
        "horario_chegada_orbita": "2031-04-05T09:00",
        "dependencia": "POWER-NUC-01",
    },
    {
        "id": "AIRLOCK-TCAN-01",
        "nome": "Airlock Duplo",
        "tipo": "habitacao",
        "prioridade": 2,
        "combustivel": 90,
        "massa": 3000,
        "criticidade": "ALTA",
        "horario_chegada_orbita": "2031-05-22T14:00",
        "dependencia": "POWER-NUC-01",
    },
    {
        "id": "LOX-TANK-01",
        "nome": "Tanque de LOX",
        "tipo": "isru",
        "prioridade": 2,
        "combustivel": 82,
        "massa": 1200,
        "criticidade": "MEDIA",
        "horario_chegada_orbita": "2031-06-01T12:00",
        "dependencia": "ISRU-ALPHA-01",
    },
    {
        "id": "HAB-CORE-01",
        "nome": "Habitat Principal",
        "tipo": "habitacao",
        "prioridade": 2,
        "combustivel": 18,
        "massa": 45000,
        "criticidade": "ALTA",
        "horario_chegada_orbita": "2031-08-10T06:00",
        "dependencia": "AIRLOCK-TCAN-01",
    },
    {
        "id": "LOG-01",
        "nome": "Modulo de Logistica A",
        "tipo": "logistica",
        "prioridade": 3,
        "combustivel": 85,
        "massa": 8000,
        "criticidade": "MEDIA",
        "horario_chegada_orbita": "2031-08-20T09:00",
        "dependencia": "HAB-CORE-01",
    },
    {
        "id": "MOPS-01",
        "nome": "Modulo Cientifico",
        "tipo": "ciencia",
        "prioridade": 4,
        "combustivel": 90,
        "massa": 2500,
        "criticidade": "MEDIA",
        "horario_chegada_orbita": "2031-09-01T10:00",
        "dependencia": "HAB-CORE-01",
    },
]


# ------------------------------------------------------------
# Estruturas lineares
#   fila_pouso   = modulos aguardando autorizacao
#   pilha_espera = modulos adiados por condicao temporaria
#   pousados     = modulos que ja desceram com sucesso
#   lista_alerta = modulos com combustivel critico
# ------------------------------------------------------------

fila_pouso = []
pilha_espera = []
pousados = []
lista_alerta = []


def potencia_solar(hora):
    """P(t) = -150t^2 + 1800t  - Watts gerados em t horas apos o nascer do sol"""
    return -150 * (hora**2) + 1800 * hora


def dentro_janela_solar(hora):
    """Janela operacional: t in [1h, 11h] (P >= 1650 W)"""
    return potencia_solar(hora) >= 1650


def max_pousos_simultaneos(hora):
    """Quantos modulos podem pousar ao mesmo tempo na hora informada"""
    disponivel = potencia_solar(hora) - 1650
    if disponivel <= 0:
        return 0
    return int(disponivel // 800)


# ------------------------------------------------------------
# Triagem inicial
# ------------------------------------------------------------


def triar_modulos(lista_todos):
    """
    Distribui os modulos:
      - combustivel < 20% -> lista_alerta (avaliados sob regra U)
      - demais            -> fila_pouso (avaliados sob regra P)
    """
    for m in lista_todos:
        if m["combustivel"] < 20:
            lista_alerta.append(m)
            print(
                f"  [ALERTA] {m['id']} - combustivel {m['combustivel']}% - movido para lista_alerta!"
            )
        else:
            fila_pouso.append(m)


# ------------------------------------------------------------
# Ordenacao da fila por prioridade com bubble sort
# ------------------------------------------------------------


def ordenar_por_prioridade(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - i - 1):
            prioridade_j = lista[j]["prioridade"]
            prioridade_j1 = lista[j + 1]["prioridade"]
            comb_j = lista[j]["combustivel"]
            comb_j1 = lista[j + 1]["combustivel"]

            deve_trocar = prioridade_j > prioridade_j1 or (
                prioridade_j == prioridade_j1 and comb_j > comb_j1
            )

            if deve_trocar:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


# ------------------------------------------------------------
# Algoritmos de busca
# ------------------------------------------------------------


def menor_combustivel(lista):
    if not lista:
        return None
    menor = lista[0]
    for m in lista:
        if m["combustivel"] < menor["combustivel"]:
            menor = m
    return menor


def buscar_por_tipo(lista, tipo):
    return [m for m in lista if m["tipo"] == tipo]


def buscar_por_id(lista, id_modulo):
    for m in lista:
        if m["id"] == id_modulo:
            return m
    return None


def buscar_por_criticidade(lista, criticidade):
    return [m for m in lista if m["criticidade"] == criticidade]


# ------------------------------------------------------------
# Verificação de dependencia
# ------------------------------------------------------------


def dependencia_satisfeita(modulo, lista_pousados):
    """E = 1 se o modulo nao tem dependencia ou se ela ja pousou"""
    dep = modulo["dependencia"]
    if dep is None:
        return True
    for p in lista_pousados:
        if p["id"] == dep:
            return True
    return False


# ------------------------------------------------------------
# Autorização de pouso
# ------------------------------------------------------------


def autorizar_pouso(modulo, area_livre, sensores_ok, atmosfera_ok, lista_pousados):
    # Avaliacao das 5 variaveis binarias de decisao
    A = modulo["combustivel"] >= 20
    B = atmosfera_ok
    C = area_livre
    D = sensores_ok
    E = dependencia_satisfeita(modulo, lista_pousados)  # Dependencia OK

    P = A and B and C and D and E
    if P:
        return "AUTORIZADO (P=A.B.C.D.E=1)"

    # módulo com combustivel critico mas sensores OK recebe pouso prioritario
    # observação de seguranca: mesmo em urgencia, tempestade total
    # bloqueia, pois é impossivel pousar com seguranca fisica
    U = (not A) and D
    if U and B:
        return "AUTORIZADO POR URGENCIA (U=NOT_A.D=1)"

    if not B:
        return "BLOQUEADO - tempestade de poeira (B=0)"
    if not A and not D:
        return "BLOQUEADO - combustivel critico E sensores em falha"
    if not E:
        return f"ADIADO - dependencia '{modulo['dependencia']}' nao pousou (E=0)"
    if not D:
        return "ADIADO - sensores com falha (D=0)"
    return "ADIADO - area de pouso ocupada (C=0)"


# ------------------------------------------------------------
# Funçãop auxiliar de impressão
# ------------------------------------------------------------


def separador(titulo=""):
    print("\n" + "=" * 60)
    if titulo:
        print(f"  {titulo}")
        print("=" * 60)


# ============================================================
# SIMULAÇÃO PRINCIPAL
# ============================================================

separador("MGPEB - MISSÃO AURORA SIGER")

# ------------------------------------------
# ETAPA 1: Triagem inicial
# ------------------------------------------
separador("ETAPA 1 - TRIAGEM INICIAL")
print("Separando modulos com combustivel critico (<20%):\n")
triar_modulos(modulos)

print(f"\n  Modulos na fila normal : {len(fila_pouso)}")
print(f"  Modulos em lista_alerta: {len(lista_alerta)}")

# ------------------------------------------
# ETAPA 2: Ordenação da fila
# ------------------------------------------
separador("ETAPA 2 - ORDENAÇÃO DA FILA")
ordenar_por_prioridade(fila_pouso)

print("Fila apos ordenação por prioridade (desempate: menor combustivel):\n")
for m in fila_pouso:
    print(
        f"  [{m['prioridade']}] {m['id']:20s} | comb: {m['combustivel']:5.1f}% | {m['criticidade']}"
    )

# ------------------------------------------
# ETAPA 3: Buscas
# ------------------------------------------
separador("ETAPA 3 - BUSCAS")

critico = menor_combustivel(fila_pouso)
print(f"Módulo com menor combustivel: {critico['id']} ({critico['combustivel']}%)")

print("\nMódulos do tipo 'construcao' na fila:")
for m in buscar_por_tipo(fila_pouso, "construcao"):
    print(f"  - {m['id']}")

print("\nModulos com criticidade MÁXIMA:")
for m in buscar_por_criticidade(fila_pouso, "MAXIMA"):
    print(f"  - {m['id']}")

# ------------------------------------------
# ETAPA 4: Pousos em condicoes normais
# ------------------------------------------
separador("ETAPA 4 - POUSOS COM CONDICOES NORMAIS")

hora_atual = 6  # meio-dia marciano
capacidade = max_pousos_simultaneos(hora_atual)
potencia = potencia_solar(hora_atual)
print(f"Hora: t={hora_atual}h | Potencia solar: {potencia:.0f} W")
print(f"Capacidade simultanea (planejamento): {capacidade} modulos por janela\n")
print("Avaliando regra P = A.B.C.D.E para cada modulo:\n")

fila_temp = list(fila_pouso)
fila_pouso.clear()

for m in fila_temp:
    resultado = autorizar_pouso(
        m,
        area_livre=True,
        sensores_ok=True,
        atmosfera_ok=True,
        lista_pousados=pousados,
    )
    print(f"  {m['id']:20s} -> {resultado}")

    if resultado.startswith("AUTORIZADO"):
        pousados.append(m)
    else:
        pilha_espera.append(m)

# ------------------------------------------
# ETAPA 5: Cenario com tempestade
# ------------------------------------------
separador("ETAPA 5 - TEMPESTADE DE POEIRA (B=0)")
print("Mesmo modulo com A=C=D=E=1 e bloqueado pois B=0 zera o AND:\n")

modulo_teste = buscar_por_id(modulos, "MOPS-01")

resultado_tempestade = autorizar_pouso(
    modulo_teste,
    area_livre=True,
    sensores_ok=True,
    atmosfera_ok=False,  # B=0
    lista_pousados=pousados,
)
print(f"  {modulo_teste['id']} -> {resultado_tempestade}")

# ------------------------------------------
# ETAPA 6: Separacao entre logica e planejamento
# ------------------------------------------
separador("ETAPA 6 - LOGICA vs PLANEJAMENTO")

hora_noite = 0
print(f"Em t={hora_noite}h:")
print(f"  Potencia solar.............. {potencia_solar(hora_noite):.0f} W")
print(f"  Janela solar aberta?......... {dentro_janela_solar(hora_noite)}")
print(f"  Capacidade simultanea........ {max_pousos_simultaneos(hora_noite)} modulos\n")

modulo_noite = {
    "id": "LOG-TESTE",
    "nome": "Logistica Teste",
    "tipo": "logistica",
    "prioridade": 3,
    "combustivel": 85,
    "massa": 8000,
    "criticidade": "MEDIA",
    "horario_chegada_orbita": "2031-08-20T09:00",
    "dependencia": None,
}

resultado_noite = autorizar_pouso(
    modulo_noite,
    area_livre=True,
    sensores_ok=True,
    atmosfera_ok=True,
    lista_pousados=pousados,
)
print(f"Avaliacao logica (regra P): {modulo_noite['id']} -> {resultado_noite}")
print("Decisão operacional: P=1, mas capacidade=0 -> ENFILEIRADO para o dia.")

# ------------------------------------------
# ETAPA 7: Reprocessamento da pilha de espera
# ------------------------------------------
separador("ETAPA 7 - REPROCESSAMENTO DA PILHA DE ESPERA")
print(f"Modulos na pilha: {len(pilha_espera)}")
print("Reavaliando com pop LIFO apos novos pousos:\n")

reprocessados = []
while len(pilha_espera) > 0:
    m = pilha_espera.pop()

    resultado = autorizar_pouso(
        m,
        area_livre=True,
        sensores_ok=True,
        atmosfera_ok=True,
        lista_pousados=pousados,
    )
    print(f"  {m['id']:20s} -> {resultado}")

    if resultado.startswith("AUTORIZADO"):
        pousados.append(m)
        reprocessados.append(m)
    else:
        fila_pouso.append(m)

print(f"\n  Modulos aprovados no reprocessamento: {len(reprocessados)}")

# ------------------------------------------
# ETAPA 8: Lista de alerta
# ------------------------------------------
separador("ETAPA 8 - REGIME DE URGENCIA (U = NOT_A . D)")
print("Modulos com combustivel critico + sensores OK = pouso prioritario:\n")

ainda_em_alerta = []
for m in lista_alerta:
    resultado = autorizar_pouso(
        m,
        area_livre=True,
        sensores_ok=True,
        atmosfera_ok=True,
        lista_pousados=pousados,
    )
    print(f"  {m['id']:20s} | comb: {m['combustivel']}% -> {resultado}")
    if resultado.startswith("AUTORIZADO"):
        pousados.append(m)
    else:
        ainda_em_alerta.append(m)
lista_alerta = ainda_em_alerta

# ------------------------------------------
# ETAPA 9: Relatorio final
# ------------------------------------------
separador("RELATORIO FINAL")

print(f"Modulos pousados com sucesso : {len(pousados)}")
for m in pousados:
    print(
        f"  [OK] {m['id']:20s} | prioridade {m['prioridade']} | comb: {m['combustivel']}%"
    )

print(f"\nModulos de volta na fila     : {len(fila_pouso)}")
for m in fila_pouso:
    motivo = autorizar_pouso(m, True, True, True, pousados)
    print(f"  [--] {m['id']:20s} | {motivo}")

print(f"\nModulos ainda em alerta      : {len(lista_alerta)}")
for m in lista_alerta:
    print(f"  [!!] {m['id']:20s} | combustivel {m['combustivel']}%")

print(f"\nPilha de espera              : {len(pilha_espera)} modulos")

# ------------------------------------------
# ETAPA 10: Tabela de potencia solar
# ------------------------------------------
separador("TABELA - POTENCIA SOLAR P(t) = -150t^2 + 1800t")
print(f"{'Hora':>5} | {'P(t) W':>8} | {'Janela':>8} | {'Max pousos':>10}")
print("-" * 42)
for t in range(0, 13):
    p = potencia_solar(t)
    janela = "ABERTA " if dentro_janela_solar(t) else "FECHADA"
    n_max = max_pousos_simultaneos(t)
    print(f"  t={t:2d}h | {p:8.0f} | {janela:>8} | {n_max:>10}")
