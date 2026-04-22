# 1. Cenário de Pouso e Fila de Módulos

> Seção 1 — Atividade Integradora FIAP — Módulo de Gerenciamento de Pouso e Estabilização de Base (MGPEB)
> Missão Aurora Siger

---

## 1.1 Contexto da Missão Aurora Siger

A missão Aurora Siger representa a primeira tentativa de estabelecer uma colônia permanente em Marte. O **Módulo de Gerenciamento de Pouso e Estabilização de Base (MGPEB)** é o sistema central que coordena a chegada, autorização e posicionamento de todos os módulos que compõem a colônia. Sem um sistemaorganized de gerenciamento, seria impossível coordenar a chegada dezenas de landers de forma segura e eficiente.

### 1.1.1 Definição do Problema

Uma colônia marciana nascente requer a chegada coordenada de múltiplos módulos com diferentes finalidades:
- Habitação para colonos
- Geração e distribuição de energia
- Produção local de recursos (oxigênio, água, metano)
- Suporte médico
- Logística e armazenamento
- Laboratórios científicos

Cada módulo tem **prioridades diferentes**, **dependências específicas** (não pode pousar antes que outro esteja operacional) e **recursos limitados** (combustível para manutenção em órbita). O MGPEB precisa organizar tudo isso em uma **fila coerente**.

---

## 1.2 Arquitetura da Base Aurora Siger

A base é organizada em **4 zonas operacionais**, inspiradas no conceito NASA Common Habitat Base Camp (Howard Jr., 2021):

| Zona | Nome | Função Principal |
|------|------|------------------|
| Z1 | Habitação | Área de vida e operações para a tripulação |
| Z2 | Pouso | Áreas designadas para recebimento de landers |
| Z3 | Produção de Recursos (ISRU) | Geração de O₂, CH₄, água e materiais |
| Z4 | Energia | Geração e distribuição de energia nuclear |

### 1.2.1 Localização das Zonas

```
                    [Z1 - HABITAÇÃO]
                    (~500m do centro)

         [Z4 - ENERGIA]          [Z3 - ISRU]
         (≤2km)                  (≤8km)

    ======================================
              [Z2 - POUSO]
         (≥2km, morro abaixo)
```

---

## 1.3 Catálogo de Módulos

A seguir, a relação completa dos módulos da Base Aurora Siger com seus atributos básicos:

### 1.3.1 Atributos Definidos para Cada Módulo

| Atributo | Tipo | Descrição |
|---------|------|----------|
| `id` | string | Identificador único |
| `nome` | string | Nome descritivo |
| `tipo_carga` | string | Categoria do módulo |
| `prioridade_pouso` | int | 1 = crítica, 5 = baixa |
| `nivel_combustivel` | float | % combustível restante (0-100) |
| `massa_kg` | int | Massa em quilogramas |
| `criticidade` | string | MÁXIMA, ALTA, MÉDIA, BAIXA |
| `horario_chegada_orbita` | string | Timestamp ISO 8601 |
| `zona_destino` | string | Zona onde pousará |

### 1.3.2 Módulos por Fase de Entrega

| ID | Nome | Tipo | Fase | Prioridade | Combustível | Massa | Criticidade | Dependência |
|----|------|------|------|-----------|------------|-------|------------|-----------|
| POWER-NUC-01 | Reator Nuclear | energia | 1 | 1 | 100% | 6.000 kg | MÁXIMA | — |
| RAD-NUC-01 | Radiadores Nucleares | infraestrutura | 1 | 1 | 95% | 1.000 kg | MÁXIMA | POWER-NUC-01 |
| PWR-DIST-01 | Terminal de Distribuição | energia | 1 | 1 | 95% | 600 kg | MÁXIMA | POWER-NUC-01 |
| COM-RELAY-01 | Relay de Comunicações | comunicacao | 1 | 1 | 93% | 1.200 kg | MÁXIMA | POWER-NUC-01 |
| LSMS-01 | Guindaste de Superfície | construcao | 1 | 1 | 88% | 2.000 kg | ALTA | PWR-DIST-01 |
| PWR-TERM-01 | Terminal de Energia | energia | 1 | 1 | 95% | 800 kg | ALTA | POWER-NUC-01 |
| RASSOR-01 | Robô Escavador A | construcao | 1 | 2 | 87% | 45 kg | MÉDIA | PWR-DIST-01 |
| RASSOR-02 | Robô Escavador B | construcao | 1 | 2 | 85% | 45 kg | MÉDIA | PWR-DIST-01 |
| RASSOR-03 | Robô Escavador C | construcao | 1 | 2 | 84% | 45 kg | MÉDIA | PWR-DIST-01 |
| ATHLETE-01 | Robô Hexápode | construcao | 1 | 1 | 85% | 900 kg | ALTA | PWR-DIST-01 |
| LANCE-01 | Lâmina Bulldozer | construcao | 1 | 2 | 80% | 300 kg | MÉDIA | ATHLETE-01 |
| VIPER-BCK-01 | Baldes de Escavação | construcao | 1 | 2 | 86% | 150 kg | MÉDIA | ATHLETE-01 |
| BIND-MAT-01 | Material de Ligação 3D | logistica | 1 | 2 | 79% | 2.500 kg | BAIXA | — |
| PRINT3D-01 | Impressora 3D Regolito | construcao | 1 | 2 | 84% | 400 kg | MÉDIA | BIND-MAT-01 |
| SINTER-01 | Dispositivo Sinterização | construcao | 1 | 2 | 81% | 180 kg | MÉDIA | PWR-DIST-01 |
| CABLE-CART-01 | Carrinho de Cabos | infraestrutura | 1 | 1 | 90% | 200 kg | ALTA | PWR-TERM-01 |
| MTV-01 | Rover Terreno A | mobilidade | 1 | 1 | 91% | 900 kg | ALTA | PWR-TERM-01 |
| MTV-02 | Rover Terreno B | mobilidade | 1 | 1 | 89% | 900 kg | ALTA | PWR-TERM-01 |
| AIRLOCK-TCAN-01 | Airlock Duplo | habitacao | 2 | 2 | 90% | 3.000 kg | ALTA | POWER-NUC-01 |
| RAD-FIELD-01 | Campo de Radiadores | infraestrutura | 2 | 2 | 92% | 2.000 kg | ALTA | POWER-NUC-01 |
| ROVER-PR-01 | Rover Pressurizado A | mobilidade | 1 | 2 | 88% | 15.000 kg | ALTA | POWER-NUC-01 |
| ROVER-PR-02 | Rover Pressurizado B | mobilidade | 1 | 2 | 86% | 15.000 kg | ALTA | POWER-NUC-01 |
| PUP-01 | Pallet Utilidade A | logistica | 1 | 3 | 80% | 500 kg | BAIXA | ROVER-PR-01 |
| PUP-02 | Pallet Utilidade B | logistica | 1 | 3 | 79% | 500 kg | BAIXA | ROVER-PR-02 |
| ISRU-ALPHA-01 | Planta ISRU | isru | 2 | 1 | 89% | 5.000 kg | ALTA | POWER-NUC-01 |
| LOX-TANK-01 | Tanque LOX | isru | 2 | 2 | 82% | 1.200 kg | MÉDIA | ISRU-ALPHA-01 |
| CH4-TANK-01 | Tanque Metano | isru | 2 | 2 | 78% | 1.000 kg | MÉDIA | ISRU-ALPHA-01 |
| H2O-TANK-01 | Tanque Água | isru | 2 | 2 | 83% | 1.100 kg | MÉDIA | ISRU-ALPHA-01 |
| HAB-CORE-01 | Habitat Principal | habitacao | 3 | 2 | 95% | 45.000 kg | ALTA | AIRLOCK-TCAN-01 |
| LOG-01 | Módulo Logística A | logistica | 2 | 3 | 85% | 8.000 kg | MÉDIA | HAB-CORE-01 |
| LOG-02 | Módulo Logística B | logistica | 2 | 3 | 82% | 8.000 kg | MÉDIA | HAB-CORE-01 |
| MOPS-01 | Módulo Científico | ciencia | 2 | 4 | 90% | 2.500 kg | MÉDIA | HAB-CORE-01 |

---

## 1.4 Estruturas de Dados Lineares

### 1.4.1 Fila Principal de Pouso (Queue)

A **fila principal** contém os módulos aguardando autorização para pouso, ordenados por prioridade:

```python
fila_pouso_principal = [
    # Ordenado por prioridade e horario de chegada a orbita
    "POWER-NUC-01",   # Prioridade 1 - energia (primeiro!)
    "RAD-NUC-01",     # Prioridade 1
    "PWR-DIST-01",    # Prioridade 1
    "COM-RELAY-01",   # Prioridade 1
    "LSMS-01",       # Prioridade 1
    "ATHLETE-01",    # Prioridade 1
    "PWR-TERM-01",   # Prioridade 1
    "CABLE-CART-01", # Prioridade 1
    "MTV-01",       # Prioridade 1
    "MTV-02",       # Prioridade 1
    "RASSOR-01",    # Prioridade 2
    "RASSOR-02",    # Prioridade 2
    "RASSOR-03",    # Prioridade 2
    "LANCE-01",     # Prioridade 2
    "VIPER-BCK-01", # Prioridade 2
    "BIND-MAT-01",  # Prioridade 2
    "PRINT3D-01",   # Prioridade 2
    "SINTER-01",    # Prioridade 2
    "RAD-FIELD-01", # Prioridade 2
    "ROVER-PR-01",  # Prioridade 2
    "ROVER-PR-02",  # Prioridade 2
    "AIRLOCK-TCAN-01",  # Prioridade 2
    "PUP-01",      # Prioridade 3
    "PUP-02",      # Prioridade 3
    "ISRU-ALPHA-01",  # Prioridade 1
    "LOX-TANK-01",  # Prioridade 2
    "CH4-TANK-01",  # Prioridade 2
    "H2O-TANK-01",  # Prioridade 2
    "HAB-CORE-01",  # Prioridade 2
    "LOG-01",      # Prioridade 3
    "LOG-02",      # Prioridade 3
    "MOPS-01",     # Prioridade 4
]
```

### 1.4.2 Lista de Módulos Pousados (Lista Simples)

```python
modulos_pousados = []  # Começa vazia, módulos são adicionados após pouso
```

### 1.4.3 Lista de Módulos em Espera (Stack)

Quando um módulo não pode pousar (ex: tempestade, área indisponível), é movido para uma **pilha de espera**:

```python
pilha_espera = []  # Stack - LIFO (Last In, First Out)
```

### 1.4.4 Lista de Módulos em Alerta

Módulos que precisam de atenção especial (baixo combustível, sensores com problema):

```python
lista_alerta = []  # Módulos que requerem intervenção
```

### 1.4.5 Resumo das Estruturas

| Estrutura | Tipo | Uso | Operações |
|----------|------|-----|-----------|
| `fila_pouso_principal` | Queue | Módulos aguardando autorização | enqueue, dequeue, peek |
| `modulos_pousados` | Lista | Módulos que já pousaram | append, remove, search |
| `pilha_espera` | Stack | Módulos adiados temporariamente | push, pop, peek |
| `lista_alerta` | Lista | Módulos com problemas | append, search, update |

---

## 1.5 Regras de Organização da Fila

### 1.5.1 Prioridade de Pouso

A ordem de pouso segue estas regras:

1. **Prioridade 1** — Sistemas críticos (energia, comunicações, construção)
2. **Prioridade 2** — Sistemas essenciais (habitat, ISRU, mobilidade)
3. **Prioridade 3** — Sistemas operacionais (logística)
4. **Prioridade 4** — Sistemas complementares (ciência)

### 1.5.2 Dependências

Um módulo **só pode pousar** quando sua dependência já estiver pousada:

- `POWER-NUC-01` → sem dependência (primeiro)
- `PWR-DIST-01` → depende de `POWER-NUC-01`
- `HAB-CORE-01` → depende de `AIRLOCK-TCAN-01`
- `LOG-01` → depende de `HAB-CORE-01`

### 1.5.3 Combustível Mínimo

Módulos com menos de **20% de combustível** são movidos para a pilha de espera e recebem prioridade de pouso emergencial.

---

## 1.6 Representação Visual da Fila

```
╔══════════════════════════════════════════════════════════════════╗
║                    FILA DE POUSO - AURORA SIGER              ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  [PRIORIDADE 1 - Críticos]                                      ║
║  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐     ║
║  │NUC-01│ │RAD-01│ │PWR-01│ │COM-01│ │LSMS-01│ │ATH-01│     ║
║  └──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘     ║
║                                                                   ║
║  [PRIORIDADE 2 - Essenciais]                                     ║
║  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐     ║
║  │TERM-01│ │CABLE-│ │RASSOR│ │ROVER │ │ISRU- │ │AIRLK │     ║
║  └──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘     ║
║                                                                   ║
║  [PRIORIDADE 3 - Operacionais]                                   ║
║  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐                           ║
║  │PUP-01│ │PUP-02│ │LOG-01│ │LOG-02│                              ║
║  └──────┘ └──────┘ └──────┘ └──────┘                           ║
║                                                                   ║
║  [PRIORIDADE 4 - Ciência]                                       ║
║  ┌──────┐                                                    ║
║  │MOPS-01│                                                   ║
║  └──────┘                                                    ║
║                                                                   ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## 1.7 Conclusão

O cenário de pouso definido nesta seção estabelece a fundação para o MGPEB. A organização em **4 zonas**, com **33 módulos** distribuídos em **3 fases de entrega**, e estruturados em **filas, pilhas e listas**, permite que o sistema gerencie de forma eficiente a construção da Base Aurora Siger.

As seções seguintes complementam este cenário com:
- **Seção 2:** Regras de decisão usando portas lógicas
- **Seção 3:** Implementação em Python
- **Seção 4:** Modelagem de funções matemáticas
- **Seção 5:** Contextualização histórica da computação
- **Seção 6:** Princípios ESG e governança

---

## Referências

- Howard Jr., R. L. (2021). *Common Habitat Base Camp for Moon and Mars Surface Operations*. NASA Johnson Space Center.
- NASA Artemis Program (2026). *Base Camp Architecture*.
- SpaceX Starship Mars Mission (2026). *Mars Colony Architecture*.