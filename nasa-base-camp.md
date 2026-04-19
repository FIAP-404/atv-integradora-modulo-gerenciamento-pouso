# Resumo Técnico — NASA Common Habitat Base Camp

> Baseado em: Howard Jr., R. L. (2021). *Common Habitat Base Camp for Moon and Mars Surface Operations*.  
> NASA Johnson Space Center, Houston, TX. AIAA Senior Member.

---

## 1. Visão geral do documento

O paper descreve o conceito de **Common Habitat** — um habitat de longa duração que pode operar tanto na Lua quanto em Marte sem modificações estruturais. Ele usa o tanque de oxigênio líquido do foguete SLS como estrutura pressurizada e comporta uma **tripulação de 8 pessoas**.

Este documento é diretamente aplicável à Base Aurora Siger pois:
- Descreve exatamente os tipos de módulos que uma colônia marciana precisaria
- Define uma estrutura de zonas que pode mapear diretamente para as estruturas de dados do MGPEB
- Detalha a sequência de pousos e prioridades de entrega — o núcleo da atividade

---

## 2. Especificações do Common Habitat

| Atributo | Valor |
|----------|-------|
| Diâmetro | 8,41 metros |
| Comprimento | 15 metros |
| Capacidade | 8 pessoas |
| Portas de acoplamento | 4 (2 longitudinais + 2 radiais) |
| Sistema de acoplamento | MGAAMA 6x6 (Multi-Gravity Active-Active Mating Adapter) |

### Decks internos

**Upper Deck (Deck Superior)** — Área social e de operações em grupo:
- Galeria com câmaras de cultivo de plantas
- Centro de comando e controle
- Instalação de cuidados médicos
- Tela de projeção panorâmica
- Compartimento de higiene

**Mid Deck (Deck Médio)** — Área de trabalho principal:
- Laboratório de ciências da vida (biologia espacial + pesquisa humana)
- Laboratório de ciências físicas (geologia, sensoriamento remoto, física)
- Instalação de fabricação, manutenção e reparo
- Equipamentos de exercício (ARED, CEVIS, T2)

**Lower Deck (Deck Inferior)** — Área privada:
- 8 quartos privados idênticos (beliches + mesa de trabalho)
- 4 instalações combinadas de higiene e gestão de resíduos

---

## 3. As quatro zonas da base — mapeamento para o MGPEB

O paper define 4 zonas operacionais distintas, cada uma com características e requisitos de pouso específicos. Essa estrutura é ideal para organizar as **listas auxiliares** do MGPEB.

### Zona 1 — Habitation Zone (Zona de Habitação)
- **Distância das outras zonas:** centro de referência da base
- **Área preparada:** 60 metros de diâmetro, nivelada, inclinação ≤ 5°
- **Profundidade do regolito:** ≥ 1,6 metros (para estabilidade do habitat)
- **Módulos típicos:** Common Habitat, rovers, TCAN (airlock), Logistics Modules

**Condição de pouso — expressão booleana:**
```
ZONA_HABITACAO_PRONTA = (terreno_nivelado == True) AND 
                         (inclinacao_graus <= 5) AND 
                         (profundidade_regolito_m >= 1.6) AND
                         (vala_escavada == True)
```

### Zona 2 — Landing Zone (Zona de Pouso)
- **Localização:** ≥ 2 km abaixo (morro abaixo) da Zona de Habitação
- **Áreas de pouso:** círculos de 100 metros de diâmetro (~1,94 acres), inclinação ≤ 5°
- **Cluster padrão:** 5 áreas de pouso por cluster
- **Múltiplos clusters:** permitidos se necessário

**Atributos de área de pouso para o MGPEB:**
```python
area_pouso = {
    "id": "LP-01",
    "diametro_m": 100,
    "inclinacao_graus": 3.2,
    "disponivel": True,
    "ultima_utilizacao": "Sol 142"
}
```

### Zona 3 — Resource Production Zone (Zona de Produção de Recursos)
- **Localização:** ≤ 8 km da Zona de Habitação
- **Acesso:** caminho de travessia conhecido, inclinação média ≤ descida segura
- **Característica especial:** pode ser **relocada** se recursos esgotarem
- **Equipamentos:** ATHLETEs, RASSORs, VIPER, plantas ISRU fixas

Módulos desta zona têm **alta prioridade de pouso** — sem produção de recursos, a colônia não é autossuficiente.

### Zona 4 — Power Zone (Zona de Energia)
- **Localização:** ≤ 2 km da Zona de Habitação
- **Característica:** reator nuclear de fissão enterrado em cratera (≥ 30m de profundidade)
- **Blindagem:** camadas de regolito sobre o reator
- **Operação segura:** pessoal pode operar até 500 metros do centro da Zona de Energia

O reator de energia nuclear é o **primeiro item a ser pousado** em toda a sequência — sem energia, nada mais funciona.

---

## 4. Sequência de pousos — a fila do MGPEB em ação

O paper define 3 fases de montagem da base. Cada fase é uma **sub-fila com prioridade** no MGPEB:

### Fase 1 — Site Preparation (Preparação do Local)

Módulos pousados nesta fase (por landers não-tripulados):

| Módulo | Sigla | Prioridade | Função |
|--------|-------|-----------|--------|
| Reator nuclear + radiadores | NPE | MÁXIMA | Energia para tudo |
| Sistema de comunicações externas | ECA | ALTA | Contato com Terra |
| Manipulador de superfície (guindaste) | LSMS | ALTA | Montagem dos outros módulos |
| Adaptadores de acoplamento | MGAAMA | ALTA | Conexão entre módulos |
| Rovers pressurizados | PR | MÉDIA | Transporte |
| Robôs hexápodes | ATHLETE | MÉDIA | Movimentação de cargas |
| Lâminas de bulldozer | LANCE | MÉDIA | Preparação do terreno |
| Impressoras 3D de regolito | — | MÉDIA | Construção |
| Dispositivos de sinterização | — | MÉDIA | Solidificação do regolito |
| Veículos de terreno lunar/marciano | LTV | BAIXA | Exploração |

### Fase 2 — Element Staging (Preparação dos Elementos)

Módulos secundários como Logistics Modules, airlock (TCAN), tankers de LOX/metano/água.

### Fase 3 — Habitat Delivery (Entrega do Habitat)

O **Common Habitat** em si — o módulo principal de habitação. Só pousa depois que a infraestrutura está pronta para recebê-lo.

---

## 5. Módulos sugeridos para a Base Aurora Siger

Com base no paper da NASA, sugerimos os seguintes módulos para a atividade:

| ID | Nome | Tipo | Prioridade | Criticidade |
|----|------|------|-----------|------------|
| MOD-01 | Reator Hélio-3 | Energia | 1 | MÁXIMA |
| MOD-02 | Hub de Comunicações | Infraestrutura | 2 | ALTA |
| MOD-03 | Habitat Principal Aurora | Habitação | 3 | ALTA |
| MOD-04 | Módulo Médico Siger | Saúde | 3 | ALTA |
| MOD-05 | Planta ISRU Oxigênio | Recursos | 4 | ALTA |
| MOD-06 | Laboratório Científico | Pesquisa | 5 | MÉDIA |
| MOD-07 | Depósito de Logística A | Logística | 6 | MÉDIA |
| MOD-08 | Depósito de Logística B | Logística | 7 | MÉDIA |
| MOD-09 | Airlock de Superfície | Infraestrutura | 8 | MÉDIA |
| MOD-10 | Rover Pressurizado Artemis | Mobilidade | 9 | BAIXA |

---

## 6. Regras de decisão para autorização de pouso

Combinando os critérios do paper com as variáveis da atividade:

```
AUTORIZAR_POUSO(módulo) =
    (combustivel_percentual > 20) AND
    (area_pouso_disponivel == True) AND
    (inclinacao_area <= 5) AND
    (vento_ms <= 25) AND
    (tempestade_ativa == False) AND
    NOT (modulo_critico_pendente AND modulo.prioridade < CRITICO)
```

---

## Fonte

Howard Jr., R. L. (2021). *Common Habitat Base Camp for Moon and Mars Surface Operations*. NASA Johnson Space Center, Houston, TX, United States of America. AIAA Senior Member (Habitability Domain Lead, Human Systems Engineering and Integration Division).
