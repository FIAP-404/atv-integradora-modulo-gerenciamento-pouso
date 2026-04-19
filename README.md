# atv-integradora-modulo-gerenciamento-pouso

# 📋 Módulos da Base Aurora Siger — Inspirados no NASA Base Camp

O base camp é dividido em **4 zonas operacionais** e os módulos são entregues em **3 fases**.
Cada elemento que chega via lander compõe a fila de pouso gerenciada pelo **MGPEB**.

---

## 📐 Estrutura de Atributos

### Estáticos — definidos no cadastro, não mudam durante a missão

| Atributo                | Tipo      | Descrição                                                                                          |
| :---------------------- | :-------- | :------------------------------------------------------------------------------------------------- |
| `id`                    | `string`  | Identificador único do módulo                                                                      |
| `nome`                  | `string`  | Nome descritivo                                                                                    |
| `tipo_carga`            | `string`  | `energia` · `habitat` · `isru` · `logistica` · `mobilidade` · `construcao` · `comunicacao` · `infraestrutura` · `ciencia` |
| `zona`                  | `string`  | `habitacao` · `pouso` · `energia` · `isru` · `construcao` · `ciencia`                             |
| `fase_entrega`          | `int`     | `1`, `2` ou `3`                                                                                    |
| `prioridade_pouso`      | `int`     | `1` = crítico → `5` = baixa prioridade                                                            |
| `massa_kg`              | `int`     | Massa total em quilogramas                                                                         |
| `critico`               | `bool`    | `True` se a base não opera sem este módulo                                                         |
| `capacidade_tripulantes`| `int`     | Pessoas suportadas (`0` se não habitável)                                                          |
| `autonomia_dias`        | `int`     | Dias de operação sem reabastecimento                                                               |
| `consumo_energia_kw`    | `float`   | Consumo médio em kilowatts                                                                         |
| `geracao_energia_kw`    | `float`   | Energia gerada em kilowatts (`0.0` se não gerador)                                                |
| `dependencia_id`        | `string`  | ID do módulo que deve pousar antes (`null` se nenhum)                                              |

### Dinâmicos — atualizados em tempo real pelo MGPEB

| Atributo                  | Tipo     | Descrição                                                          |
| :------------------------ | :------- | :----------------------------------------------------------------- |
| `nivel_combustivel`       | `float`  | Percentual de combustível restante (0–100)                         |
| `sensores_integros`       | `bool`   | `True` se todos os sensores de bordo estão operacionais            |
| `dependencia_satisfeita`  | `bool`   | `True` se o módulo dependente já pousou com sucesso                |
| `condicao_atmosferica_ok` | `bool`   | `True` se ventos e visibilidade permitem pouso seguro              |
| `area_pouso_disponivel`   | `bool`   | `True` se há área livre e nivelada na Landing Zone                 |
| `energia_base_disponivel` | `bool`   | `True` se o Power Terminal está ativo na superfície                |
| `horario_orbita_estimado` | `string` | Timestamp ISO 8601 de chegada à órbita de espera                   |
| `status`                  | `string` | `em_orbita` · `autorizado` · `pousado` · `alerta` · `bloqueado`   |

---

## 🗂️ Catálogo Completo de Módulos

> **Legenda:** `F` = fase · `P` = prioridade · `M (kg)` = massa · `C` = crítico · `Tri.` = tripulantes · `Aut.` = autonomia (dias) · `Con.` = consumo (kW) · `Ger.` = geração (kW) · `Dep.` = dependencia_id · `Cmb.` = combustível (%)

### 🏠 Zona de Habitação

| ID                   | Nome                   | Tipo           |  F  |  P  |   M (kg) |  C  | Tri. | Aut. | Con.  | Ger. | Dep.                 | Cmb. | Horário Órbita      |
| :------------------- | :--------------------- | :------------- | :-: | :-: | -------: | :-: | ---: | ---: | ----: | ---: | :------------------- | ---: | :------------------ |
| `HAB-CORE-01`        | Habitat Principal      | habitat        |  3  |  2  |   45.000 | ✅  |    8 |  624 | 100,0 |  0,0 | `AIRLOCK-TCAN-01`    | 95,0 | 2031-08-10T06:00    |
| `AIRLOCK-TCAN-01`    | Nó de Airlock Duplo    | habitat        |  2  |  2  |    3.000 | ✅  |    4 |  624 |   5,0 |  0,0 | `POWER-NUC-01`       | 90,0 | 2031-05-22T14:00    |
| `LOG-01`             | Módulo de Logística A  | logistica      |  2  |  3  |    8.000 | ❌  |    0 |    0 |   2,0 |  0,0 | `HAB-CORE-01`        | 85,0 | 2031-08-20T09:00    |
| `LOG-02`             | Módulo de Logística B  | logistica      |  2  |  3  |    8.000 | ❌  |    0 |    0 |   2,0 |  0,0 | `HAB-CORE-01`        | 82,0 | 2031-08-22T09:00    |
| `ROVER-PR-01`        | Rover Pressurizado A   | mobilidade     |  1  |  2  |   15.000 | ✅  |    4 |   30 |  15,0 |  0,0 | `POWER-NUC-01`       | 88,0 | 2031-03-01T10:00    |
| `ROVER-PR-02`        | Rover Pressurizado B   | mobilidade     |  1  |  2  |   15.000 | ✅  |    4 |   30 |  15,0 |  0,0 | `POWER-NUC-01`       | 86,0 | 2031-03-03T10:00    |
| `PUP-01`             | Pallet de Utilidade A  | logistica      |  1  |  3  |      500 | ❌  |    0 |    0 |   1,0 |  0,0 | `ROVER-PR-01`        | 80,0 | 2031-03-01T10:30    |
| `PUP-02`             | Pallet de Utilidade B  | logistica      |  1  |  3  |      500 | ❌  |    0 |    0 |   1,0 |  0,0 | `ROVER-PR-02`        | 79,0 | 2031-03-03T10:30    |
| `RAD-FIELD-01`       | Campo de Radiadores    | infraestrutura |  2  |  2  |    2.000 | ✅  |    0 |    0 |   0,0 |  0,0 | `POWER-NUC-01`       | 92,0 | 2031-05-10T08:00    |

### 🛬 Zona de Pouso

| ID                   | Nome                   | Tipo           |  F  |  P  |   M (kg) |  C  | Tri. | Aut. | Con. | Ger. | Dep.                 | Cmb. | Horário Órbita      |
| :------------------- | :--------------------- | :------------- | :-: | :-: | -------: | :-: | ---: | ---: | ---: | ---: | :------------------- | ---: | :------------------ |
| `PWR-TERM-01`        | Terminal de Energia    | energia        |  1  |  1  |      800 | ✅  |    0 | 3650 |  0,0 | 50,0 | `POWER-NUC-01`       | 95,0 | 2031-01-20T07:00    |
| `CABLE-CART-01`      | Carrinho de Cabos      | infraestrutura |  1  |  1  |      200 | ✅  |    0 |    0 |  0,5 |  0,0 | `PWR-TERM-01`        | 90,0 | 2031-01-20T07:30    |
| `MTV-01`             | Rover de Terreno A     | mobilidade     |  1  |  1  |      900 | ✅  |    2 |   10 |  5,0 |  0,0 | `PWR-TERM-01`        | 91,0 | 2031-01-25T11:00    |
| `MTV-02`             | Rover de Terreno B     | mobilidade     |  1  |  1  |      900 | ✅  |    2 |   10 |  5,0 |  0,0 | `PWR-TERM-01`        | 89,0 | 2031-01-27T11:00    |

### ⚡ Zona de Energia

| ID                   | Nome                        | Tipo           |  F  |  P  |  M (kg) |  C  | Tri. | Aut. | Con. |  Ger. | Dep.             | Cmb. | Horário Órbita   |
| :------------------- | :-------------------------- | :------------- | :-: | :-: | -------: | :-: | ---: | ---: | ---: | ----: | :--------------- | ---: | :--------------- |
| `POWER-NUC-01`       | Reator Nuclear de Fissão    | energia        |  1  |  1  |    6.000 | ✅  |    0 | 3650 |  0,0 | 100,0 | `null`           |100,0 | 2031-01-10T05:00 |
| `RAD-NUC-01`         | Radiadores do Reator        | infraestrutura |  1  |  1  |    1.000 | ✅  |    0 |    0 |  0,0 |   0,0 | `POWER-NUC-01`   | 95,0 | 2031-01-10T05:30 |
| `COM-RELAY-01`       | Array de Comunicações       | comunicacao    |  1  |  1  |    1.200 | ✅  |    0 |    0 | 10,0 |   0,0 | `POWER-NUC-01`   | 93,0 | 2031-01-12T06:00 |
| `PWR-DIST-01`        | Terminal de Distribuição    | energia        |  1  |  1  |      600 | ✅  |    0 |    0 |  0,0 |   0,0 | `POWER-NUC-01`   | 95,0 | 2031-01-15T07:00 |

### 🔬 Zona de Produção de Recursos (ISRU)

| ID                   | Nome                        | Tipo       |  F  |  P  |   M (kg) |  C  | Tri. | Aut. |  Con. | Ger. | Dep.             | Cmb. | Horário Órbita   |
| :------------------- | :-------------------------- | :--------- | :-: | :-: | -------: | :-: | ---: | ---: | ----: | ---: | :--------------- | ---: | :--------------- |
| `ISRU-ALPHA-01`      | Planta ISRU                 | isru       |  2  |  1  |    5.000 | ✅  |    0 |    0 | 850,0 |  0,0 | `POWER-NUC-01`   | 89,0 | 2031-04-05T09:00 |
| `RASSOR-01`          | Robô Escavador A            | construcao |  1  |  2  |       45 | ❌  |    0 |    0 |   0,5 |  0,0 | `PWR-DIST-01`    | 87,0 | 2031-02-01T08:00 |
| `RASSOR-02`          | Robô Escavador B            | construcao |  1  |  2  |       45 | ❌  |    0 |    0 |   0,5 |  0,0 | `PWR-DIST-01`    | 85,0 | 2031-02-01T08:30 |
| `RASSOR-03`          | Robô Escavador C            | construcao |  1  |  2  |       45 | ❌  |    0 |    0 |   0,5 |  0,0 | `PWR-DIST-01`    | 84,0 | 2031-02-01T09:00 |
| `ATHLETE-01`         | Robô Hexápode A             | construcao |  1  |  1  |      900 | ✅  |    0 |    0 |   2,0 |  0,0 | `PWR-DIST-01`    | 85,0 | 2031-02-05T10:00 |
| `LANCE-01`           | Lâmina Bulldozer A          | construcao |  1  |  2  |      300 | ❌  |    0 |    0 |   0,0 |  0,0 | `ATHLETE-01`     | 80,0 | 2031-02-05T10:30 |
| `LOX-TANK-01`        | Tanque de LOX               | isru       |  2  |  2  |    1.200 | ❌  |    0 |    0 |   1,0 |  0,0 | `ISRU-ALPHA-01`  | 82,0 | 2031-06-01T12:00 |
| `CH4-TANK-01`        | Tanque de Metano            | isru       |  2  |  2  |    1.000 | ❌  |    0 |    0 |   1,0 |  0,0 | `ISRU-ALPHA-01`  | 78,0 | 2031-06-05T12:00 |
| `H2O-TANK-01`        | Tanque de Água              | isru       |  2  |  2  |    1.100 | ❌  |    0 |    0 |   1,0 |  0,0 | `ISRU-ALPHA-01`  | 83,0 | 2031-06-10T12:00 |

### 🏗️ Equipamentos de Construção

| ID                   | Nome                        | Tipo       |  F  |  P  |   M (kg) |  C  | Tri. | Aut. | Con. | Ger. | Dep.             | Cmb. | Horário Órbita   |
| :------------------- | :-------------------------- | :--------- | :-: | :-: | -------: | :-: | ---: | ---: | ---: | ---: | :--------------- | ---: | :--------------- |
| `LSMS-01`            | Guindaste de Superfície     | construcao |  1  |  1  |    2.000 | ✅  |    0 |    0 |  3,0 |  0,0 | `PWR-DIST-01`    | 88,0 | 2031-01-18T06:00 |
| `VIPER-BCK-01`       | Baldes de Escavação         | construcao |  1  |  2  |      150 | ❌  |    0 |    0 |  0,3 |  0,0 | `ATHLETE-01`     | 86,0 | 2031-02-05T11:00 |
| `PRINT3D-01`         | Impressora 3D de Regolito   | construcao |  1  |  2  |      400 | ❌  |    0 |    0 |  4,0 |  0,0 | `BIND-MAT-01`    | 84,0 | 2031-02-10T09:00 |
| `SINTER-01`          | Dispositivo de Sinterização | construcao |  1  |  2  |      180 | ❌  |    0 |    0 |  2,5 |  0,0 | `PWR-DIST-01`    | 81,0 | 2031-02-12T09:00 |
| `BIND-MAT-01`        | Material de Ligação 3D      | logistica  |  1  |  2  |    2.500 | ❌  |    0 |    0 |  0,0 |  0,0 | `null`           | 79,0 | 2031-02-08T08:00 |

### 🔭 Ciência

| ID                   | Nome                                      | Tipo    |  F  |  P  |  M (kg) |  C  | Tri. | Aut. | Con. | Ger. | Dep.           | Cmb. | Horário Órbita   |
| :------------------- | :---------------------------------------- | :------ | :-: | :-: | -------: | :-: | ---: | ---: | ---: | ---: | :------------- | ---: | :--------------- |
| `MOPS-01`            | Módulo de Observação e Pesquisa Científica| ciencia |  2  |  4  |    2.500 | ❌  |    0 |    0 |  8,0 |  0,0 | `HAB-CORE-01`  | 90,0 | 2031-09-01T10:00 |

---

## 🔗 Grafo de Dependências

```
POWER-NUC-01           # pousa primeiro — sem dependência
├── RAD-NUC-01
├── PWR-DIST-01
│   ├── COM-RELAY-01
│   ├── LSMS-01
│   ├── SINTER-01
│   ├── RASSOR-01..03
│   └── ATHLETE-01
│       ├── LANCE-01
│       └── VIPER-BCK-01
├── PWR-TERM-01
│   ├── CABLE-CART-01
│   └── MTV-01..02
├── ROVER-PR-01..02
│   └── PUP-01..02
└── AIRLOCK-TCAN-01
    └── HAB-CORE-01
        ├── LOG-01..02
        └── MOPS-01

BIND-MAT-01            # sem dependência — insumo puro
└── PRINT3D-01

ISRU-ALPHA-01          # depende de POWER-NUC-01
├── LOX-TANK-01
├── CH4-TANK-01
└── H2O-TANK-01
```

---

> **Referência:** Arquitetura baseada no documento oficial da NASA
> *"Common Habitat Base Camp for Moon and Mars Surface Operations"* — Robert L. Howard Jr., NASA Johnson Space Center.
> Complementado por análise dos planos Artemis (2026) e missão SpaceX Starship para Marte.
