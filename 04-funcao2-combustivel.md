# Função 2 — Consumo de Combustível em Função do Tempo
**Missão Aurora Siger · MGPEB — Módulo de Gerenciamento de Pouso e Estabilização de Base**

> **Tipo de função:** Linear decrescente  
> **Inspiração real:** SpaceX Falcon 9 (motores Merlin 1D) · NASA Mars EDL

---

## 1. Contexto Real — SpaceX e NASA

Durante a queima de pouso do **Falcon 9**, os motores Merlin 1D queimam propelente a uma taxa aproximadamente constante. Em missões de alta energia, a SpaceX aciona até três motores simultaneamente para triplicar a desaceleração nos momentos finais do voo — o chamado *landing burn*.

Os motores Merlin 1D, com nove unidades ativas, queimam cerca de **1.658 kg/s** de propelente. Em queima de pouso com motor único, a taxa fica em torno de **184 kg/s**. Para os módulos da colônia Aurora Siger, adotamos uma taxa simplificada de **80 kg/s**, compatível com módulos de menor porte destinados ao pouso em Marte.

> 🔴 **Contexto marciano:** A gravidade em Marte é **3,72 m/s²** (38% da Terra). Isso reduz a força necessária dos retrofoguetes e, consequentemente, o consumo de combustível por segundo — tornando o pouso mais eficiente em termos de propelente. Ainda assim, o combustível é um recurso crítico e **não renovável** na colônia.

---

## 2. Fórmula Matemática

Como a taxa de queima é constante ao longo do tempo, o consumo segue uma **função linear decrescente**:

$$m(t) = m_0 - r \cdot t$$

Aplicando os parâmetros da missão:

$$\boxed{m(t) = 2400 - 80t}$$

### Significado dos Parâmetros

| Símbolo | Valor | Significado |
|---|---|---|
| **m(t)** | — | Massa de combustível restante no instante *t* (kg) — variável dependente |
| **t** | — | Tempo decorrido desde o início da queima de pouso (s) — variável independente |
| **m₀ = 2.400 kg** | Coeficiente linear | Combustível disponível em t = 0. É o ponto onde a reta intercepta o eixo vertical |
| **r = 80 kg/s** | Coeficiente angular | Taxa de queima. Representa a inclinação negativa da reta: −80 |
| **t_max = 30 s** | Domínio | Duração total da queima de pouso. Para t > 30 s, o motor já foi desligado |

> O domínio da função é **t ∈ [0, 30]** e a imagem é **m(t) ∈ [0, 2400]**, ambos em valores não negativos, pois não existe combustível negativo.

---

## 3. Tabela de Valores

Calculando **m(t) = 2.400 − 80t** para instantes selecionados:

| Tempo t (s) | Cálculo | m(t) (kg) | Combustível restante | Status do módulo |
|:---:|---|:---:|:---:|:---:|
| 0  | 2400 − 80×0  | **2.400** | 100% | ✅ Autorizado |
| 5  | 2400 − 80×5  | **2.000** | 83%  | ✅ Autorizado |
| 10 | 2400 − 80×10 | **1.600** | 67%  | ✅ Autorizado |
| 15 | 2400 − 80×15 | **1.200** | 50%  | ✅ Autorizado |
| 20 | 2400 − 80×20 | **800**   | 33%  | ⚠️ Alerta     |
| 25 | 2400 − 80×25 | **400**   | 17%  | 🚫 Bloqueado  |
| 28 | 2400 − 80×28 | **160**   | 7%   | 🚫 Bloqueado  |
| 30 | 2400 − 80×30 | **0**     | 0%   | 🚫 Bloqueado  |

**Limiares de segurança adotados pelo MGPEB:**
- ✅ **Autorizado:** m(t) > 800 kg
- ⚠️ **Alerta:** 400 kg < m(t) ≤ 800 kg
- 🚫 **Bloqueado:** m(t) ≤ 400 kg

---

## 4. Análise Qualitativa do Gráfico

```
m(t) (kg)
2400 |●
     |  \
2000 |    \
     |      \
1600 |        \
     |          \
1200 |            \
     |              \
 800 |_ _ _ _ _ _ _ _●_ _ _ ⚠️ NÍVEL DE ALERTA
     |                  \
 400 |_ _ _ _ _ _ _ _ _ _ ●_ _ 🚫 NÍVEL CRÍTICO
     |                      \
   0 +---+---+---+---+---+---●--→ t (s)
     0   5  10  15  20  25  30
```

### O que o gráfico revela:

**📉 Comportamento geral — reta decrescente**  
A função é estritamente decrescente: à medida que t aumenta, m(t) diminui de forma linear e constante. Não há aceleração nem desaceleração no consumo — cada segundo consome exatamente 80 kg.

**📐 Inclinação (coeficiente angular = −80)**  
A inclinação negativa confirma o decréscimo. Quanto maior a taxa de queima *r*, mais inclinada a reta — e mais rápido o módulo ficará sem combustível. Se *r* dobrasse para 160 kg/s, o combustível se esgotaria em apenas 15 segundos.

**🎯 Ponto inicial (t = 0)**  
Em t = 0, m(0) = **2.400 kg**. É o ponto onde a reta intercepta o eixo vertical. Representa o combustível máximo disponível antes de iniciar a queima de pouso.

**⛔ Cruzamento do nível crítico (t = 25 s)**  
Isolando *t* na fórmula para encontrar quando m(t) = 400 kg:

$$t_{critico} = \frac{m_0 - m_{critico}}{r} = \frac{2400 - 400}{80} = \frac{2000}{80} = 25 \text{ s}$$

A partir desse instante, o MGPEB bloqueia automaticamente qualquer novo pouso. A reta não pode cruzar esse limiar com segurança operacional.

**📊 Se as variáveis aumentam ou diminuem:**

| Variação | Efeito em m(t) |
|---|---|
| *t* aumenta | m(t) **diminui** — combustível sendo consumido |
| *r* aumenta (motor mais potente) | Reta mais inclinada — combustível acaba mais rápido |
| *m₀* aumenta (mais combustível inicial) | Reta deslocada para cima — maior margem de segurança |
| *r* = 0 (motor desligado) | Reta horizontal — combustível se mantém constante |

---

## 5. Conexão com as Decisões de Engenharia do MGPEB

A função m(t) = 2.400 − 80t alimenta diretamente três decisões críticas do sistema:

### ① Autorização de Pouso — Regra Booleana

O MGPEB só autoriza o pouso se o combustível inicial for superior ao nível de alerta. Em Python, essa condição pode ser implementada da seguinte forma:

```python
def combustivel_restante(t):
    return 2400 - 80 * t

autorizar = (
    combustivel_inicial > 800
    and area_livre
    and sensores_ok
)
```

A função m(t) fornece o valor exato de **combustivel_inicial** — a variável consultada no momento em que o módulo solicita entrada na fila de pouso. Sem ela, a regra booleana não teria como quantificar a condição de combustível.

### ② Duração Máxima de Queima e Suporte à Decisão de Ignição

É importante ser preciso sobre o que m(t) modela: ela descreve o combustível restante **a partir do momento em que a queima já foi iniciada**. Por isso, sozinha ela não determina o instante ideal de ignição — para isso, seria necessário combiná-la com a função de altitude h(t), que informa a que distância do solo o módulo se encontra em cada instante.

O que m(t) oferece diretamente é o **tempo máximo de queima disponível**, ou seja, por quanto tempo os motores podem operar antes de cruzar o limiar crítico:

$$t_{queima\_max} = \frac{m_0 - m_{critico}}{r} = \frac{2400 - 400}{80} = 25 \text{ s}$$

Esse valor é entregue à lógica de pouso do MGPEB como uma restrição operacional: qualquer sequência de ignição que demande mais de **25 segundos de queima contínua** é rejeitada antes mesmo de começar, independentemente da altitude. Combinada com h(t), a restrição de 25 s permite calcular a altitude mínima em que a ignição deve ocorrer para que o módulo consiga desacelerar completamente sem esgotar o combustível — integrando as duas funções numa decisão única e coerente.

### ③ Ordenação da Fila por Combustível Crítico

O algoritmo de ordenação da fila de pouso usa m(t) para calcular o **tempo máximo de espera tolerável** de cada módulo antes de entrar em colapso de combustível:

$$t_{espera\_max} = \frac{m_0 - m_{critico}}{r} = \frac{m_0 - 400}{80}$$

**Exemplo:** Um módulo com apenas 1.200 kg de combustível inicial suporta no máximo:

$$t_{espera\_max} = \frac{1200 - 400}{80} = 10 \text{ s}$$

Módulos com menor margem de espera sobem automaticamente na fila de prioridade — integrando diretamente a modelagem matemática ao algoritmo de ordenação do MGPEB.

---

## 6. Resumo da Modelagem

| Item | Descrição |
|---|---|
| **Função** | m(t) = 2.400 − 80t |
| **Tipo** | Linear decrescente |
| **Domínio** | t ∈ [0, 30] segundos |
| **Imagem** | m(t) ∈ [0, 2.400] kg |
| **Coeficiente angular** | −80 (taxa de consumo negativa) |
| **Coeficiente linear** | 2.400 (combustível inicial) |
| **Nível de alerta** | m(t) = 800 kg → t = 20 s |
| **Nível crítico** | m(t) = 400 kg → t = 25 s |
| **Referência real** | SpaceX Merlin 1D · NASA Mars EDL |

---

*Missão Aurora Siger · MGPEB · Passo 4 — Modelagem de Funções Matemáticas*  
*Referências: SpaceX Falcon 9 Technical Overview · NASA Mars 2020 EDL Press Kit · Marspedia — Solar Panel*
