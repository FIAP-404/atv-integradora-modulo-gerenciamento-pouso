# Função 3 — Geração de Energia Solar ao Longo do Sol Marciano
**Missão Aurora Siger · MGPEB — Módulo de Gerenciamento de Pouso e Estabilização de Base**

> **Tipo de função:** Quadrática (2º grau), côncava para baixo  
> **Inspiração real:** NASA InSight Lander (Elysium Planitia, 2018) · NASA Mars Exploration Rovers Spirit e Opportunity

---

## 1. Contexto Real — NASA InSight e Rovers Marcianos

A energia solar é o sistema de potência primário de praticamente todas as missões não nucleares em Marte. A NASA acumulou décadas de dados reais sobre geração fotovoltaica no planeta vermelho, tornando essa uma das variáveis mais bem documentadas do ambiente marciano.

### Histórico de Geração Solar em Marte (NASA)

| Missão | Painéis | Geração no 1º Sol | Pico de Potência |
|---|---|---|---|
| **Phoenix Lander (2008)** | Fixos | ~1.800 Wh/sol | ~300 W |
| **InSight Lander (2018)** | UltraFlex 2×2,2m | **4.588 Wh/sol** *(recorde)* | **600–700 W** |
| **Aurora Siger — Colônia** | Array expandido | ~43.200 Wh/sol | **5.400 W** |

> 📡 **Dado real NASA:** O InSight gerou **4.588 Wh** em seu primeiro sol marciano — o maior recorde de geração solar já registrado na superfície de Marte. Seus painéis UltraFlex produziam entre **600 e 700 W de pico** em dia claro. Por outro lado, após anos de acúmulo de poeira, a geração caiu para apenas **500 Wh/sol** — uma redução de 90% que levou ao fim da missão em dezembro de 2022.

> ☀️ **Condição solar em Marte:** A irradiância solar máxima na superfície marciana é de aproximadamente **590 W/m²** — cerca de 43% da irradiância terrestre (1.367 W/m²). Isso ocorre porque Marte está 1,52 vez mais distante do Sol do que a Terra. Além disso, a atmosfera fina e carregada de poeira atenua ainda mais a luz disponível.

> 🕐 **Duração do sol marciano:** Um sol (dia marciano) tem duração de **24 horas, 39 minutos e 35 segundos** — apenas 2,7% mais longo que um dia terrestre. Nas regiões equatoriais de Marte, há aproximadamente **12 horas de luz solar** por sol.

---

## 2. Fenômeno Físico Modelado

Durante um sol marciano, a potência gerada pelos painéis solares da base não é constante: ela começa em **zero no nascer do sol**, sobe progressivamente até o **pico ao meio-dia**, e depois decresce simetricamente até **zero no pôr do sol**.

Esse comportamento é causado pelo **ângulo de incidência da luz solar** sobre os painéis:
- Ao nascer e pôr do sol, os raios chegam **oblíquos** → energia por m² é baixa
- Ao meio-dia, os raios chegam **perpendiculares** aos painéis → energia por m² é máxima

Embora o modelo físico exato seja uma função trigonométrica (cosseno do ângulo zenital), para o currículo desta disciplina adotamos a **aproximação por parábola côncava para baixo**, que representa com boa fidelidade o comportamento real observado nas missões da NASA.

---

## 3. Fórmula Matemática

Definindo t como as **horas após o nascer do sol marciano**, com t ∈ [0, 12]:

$$\boxed{P(t) = -150t^2 + 1800t}$$

Onde P(t) é a potência gerada em **Watts (W)**.

### Verificação dos Pontos Notáveis

**Nascer do sol (t = 0):**
$$P(0) = -150 \cdot 0^2 + 1800 \cdot 0 = \mathbf{0 \text{ W}} \checkmark$$

**Meio-dia marciano (t = 6 h):**
$$P(6) = -150 \cdot 36 + 1800 \cdot 6 = -5400 + 10800 = \mathbf{5400 \text{ W}} \checkmark$$

**Pôr do sol (t = 12 h):**
$$P(12) = -150 \cdot 144 + 1800 \cdot 12 = -21600 + 21600 = \mathbf{0 \text{ W}} \checkmark$$

### Forma de Vértice (equivalente)

A mesma função pode ser escrita na **forma de vértice** da parábola:

$$P(t) = -150 \cdot (t - 6)^2 + 5400$$

Onde:
- **t = 6** é o instante do pico (meio-dia)
- **5.400 W** é a potência máxima

---

## 4. Significado dos Parâmetros

| Símbolo | Valor | Papel na função | Significado físico |
|---|---|---|---|
| **P(t)** | — | Variável dependente | Potência gerada pelos painéis solares no instante t (W) |
| **t** | — | Variável independente | Horas após o nascer do sol marciano |
| **−150** | Coeficiente de t² | Abre a parábola para baixo | Define a taxa de variação da geração ao longo do dia |
| **+1800** | Coeficiente de t | Inclina a curva para cima no início | Relacionado à velocidade com que a irradiação cresce na manhã |
| **5.400 W** | Valor no vértice | Ponto máximo da parábola | Potência de pico ao meio-dia marciano — base da Aurora Siger |
| **t = 6 h** | Eixo de simetria | t = −b / (2a) = 1800 / 300 | Meio-dia: momento em que o sol está perpendicular aos painéis |
| **t ∈ [0, 12]** | Domínio | Raízes da equação | Período de luz solar na região equatorial marciana |

> **Eixo de simetria:** a parábola é perfeitamente simétrica em torno de t = 6h. Isso reflete o comportamento físico real: a potência gerada às 9h da manhã é igual à potência gerada às 15h da tarde, pois o ângulo solar é o mesmo nos dois instantes.

---

## 5. Tabela de Valores

Calculando **P(t) = −150t² + 1800t** para cada hora do sol marciano:

| Horas após nascer do sol (t) | Horário local aprox. | Cálculo | P(t) (W) | Situação operacional |
|:---:|:---:|---|:---:|:---:|
| 0  | 06h00 | −150×0 + 0           | **0**     | 🌅 Nascer do sol |
| 1  | 07h00 | −150×1 + 1800        | **1.650** | ⚠️ Limiar mínimo |
| 2  | 08h00 | −150×4 + 3600        | **3.000** | ✅ Operações ativas |
| 3  | 09h00 | −150×9 + 5400        | **4.050** | ✅ Operações ativas |
| 4  | 10h00 | −150×16 + 7200       | **4.800** | ✅ Operações ativas |
| 5  | 11h00 | −150×25 + 9000       | **5.250** | ✅ Operações ativas |
| 6  | 12h00 | −150×36 + 10800      | **5.400** | 🌞 PICO — Meio-dia |
| 7  | 13h00 | −150×49 + 12600      | **5.250** | ✅ Operações ativas |
| 8  | 14h00 | −150×64 + 14400      | **4.800** | ✅ Operações ativas |
| 9  | 15h00 | −150×81 + 16200      | **4.050** | ✅ Operações ativas |
| 10 | 16h00 | −150×100 + 18000     | **3.000** | ✅ Operações ativas |
| 11 | 17h00 | −150×121 + 19800     | **1.650** | ⚠️ Limiar mínimo |
| 12 | 18h00 | −150×144 + 21600     | **0**     | 🌇 Pôr do sol |

> **Simetria confirmada:** P(1) = P(11) = 1.650 W · P(2) = P(10) = 3.000 W · P(3) = P(9) = 4.050 W · P(4) = P(8) = 4.800 W · P(5) = P(7) = 5.250 W. A tabela é perfeitamente espelhada em torno do meio-dia (t = 6h).

---

## 6. Análise Qualitativa do Gráfico

```
P(t) (W)
5400 |              ●
     |           /     \
5250 |         ●         ●
     |        /           \
4800 |      ●               ●
     |     /                 \
4050 |   ●                     ●
     |  /                       \
3000 | ●                           ●
     |/                             \
1650 ●_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _● ⚠️ LIMIAR MÍNIMO (1.650 W)
     |                               \
   0 ●---+---+---+---+---+---+---+---+●→ t (h após nascer do sol)
     0   1   2   3   4   5   6   7   8   9  10  11  12
     |←────────── JANELA OPERACIONAL (10 horas) ──────────→|
```

### O que o gráfico revela:

**📈 Forma da parábola — côncava para baixo**  
O coeficiente de t² é **negativo (−150)**, portanto a parábola abre para baixo. A curva sobe da esquerda até o vértice e depois desce — representando o ciclo natural de geração solar: aumento na manhã, pico ao meio-dia, queda na tarde.

**🔝 Vértice = ponto de máxima geração**  
O vértice de uma parábola `P(t) = at² + bt` ocorre em:

$$t_{vertice} = \frac{-b}{2a} = \frac{-1800}{2 \times (-150)} = \frac{-1800}{-300} = 6 \text{ h}$$

O vértice está em t = 6h com P = **5.400 W** — o meio-dia marciano, quando o sol está no ponto mais alto do céu e os raios incidem mais perpendicularmente nos painéis.

**🔄 Simetria perfeita em torno de t = 6h**  
Por ser uma parábola, a curva é exatamente simétrica. Isso reflete a realidade física: a posição angular do sol no céu é idêntica 2 horas antes e 2 horas depois do meio-dia, gerando a mesma irradiância.

**📊 O que acontece quando as variáveis aumentam ou diminuem:**

| Variação | Efeito em P(t) |
|---|---|
| *t* se afasta do meio-dia | P(t) **diminui** — sol mais oblíquo, menos energia |
| Tempestade de poeira (τ aumenta) | Vértice mais baixo — P_max pode cair para apenas 100–200 W (como aconteceu com o InSight) |
| Painéis mais sujos (acúmulo de poeira) | Parábola "achatada" para baixo — toda a curva é multiplicada por fator < 1 |
| Painéis inclinados para seguir o sol | Parábola mais "alta" — P_max aumenta em até 30–40% |
| Latitude mais alta (longe do equador) | Vértice menor e janela solar mais curta — parábola mais estreita e baixa |
| Coeficiente |a| maior em módulo | Parábola mais "fechada" — o pico é mais estreito e rápido |

---

## 7. Cálculo da Energia Total Diária

A energia total gerada em um sol é calculada somando (integrando) a potência ao longo de todas as horas:

**Estimativa pela tabela (método dos trapézios simplificado):**

$$E_{dia} \approx \sum_{t=0}^{11} P(t) \times 1h = (0 + 1650 + 3000 + 4050 + 4800 + 5250 + 5400 + 5250 + 4800 + 4050 + 3000 + 1650) \times 1$$

$$E_{dia} \approx 42.900 \text{ Wh} \approx \mathbf{43{,}2 \text{ kWh/sol}}$$

**Resultado exato pela fórmula:**

$$E_{dia} = \int_0^{12} (-150t^2 + 1800t) \, dt = \left[-50t^3 + 900t^2\right]_0^{12}$$

$$E_{dia} = -50 \times 1728 + 900 \times 144 = -86400 + 129600 = \mathbf{43.200 \text{ Wh} = 43{,}2 \text{ kWh/sol}}$$

> 📊 **Contexto:** 43,2 kWh por sol equivale à energia elétrica consumida por aproximadamente 10 casas brasileiras em um dia — suficiente para manter operações básicas de uma colônia nascente como a Aurora Siger.

---

## 8. Cálculo da Janela Operacional de Pouso

O MGPEB define que operações de pouso **só podem ser autorizadas** quando a potência gerada for suficiente para alimentar todos os sistemas simultaneamente. O limiar mínimo operacional é:

$$P_{min} = 1.650 \text{ W}$$

Para encontrar os instantes exatos de início e fim da janela, resolve-se:

$$P(t) = 1.650$$
$$-150t^2 + 1800t = 1650$$
$$-150t^2 + 1800t - 1650 = 0$$

Dividindo toda a equação por −150:

$$t^2 - 12t + 11 = 0$$

Fatorando:

$$(t - 1)(t - 11) = 0$$

$$\boxed{t = 1 \text{ h} \quad \text{ou} \quad t = 11 \text{ h}}$$

**Conclusão:** A janela operacional de pouso da colônia Aurora Siger é:

$$t \in [1h, 11h] \quad \text{após o nascer do sol} \quad \Rightarrow \quad \mathbf{10 \text{ horas por sol}}$$

---

## 9. Conexão com as Decisões de Engenharia do MGPEB

A função P(t) = −150t² + 1800t orienta diretamente três decisões críticas do sistema:

### ① Janela de Autorização de Pouso — Regra Booleana

O MGPEB só autoriza um pouso se a potência atual for maior que o limiar mínimo. Essa condição é expressa como uma função booleana composta:

```python
def potencia_solar(hora_atual):
    return -150 * (hora_atual ** 2) + 1800 * hora_atual

autorizar_pouso = (
    potencia_solar(hora_atual) >= 1650
    and combustivel > 800
    and area_livre
    and sensores_ok
)
```

A função P(t) fornece o valor de potência gerada no instante consultado — sem ela, o sistema não teria como avaliar quantitativamente se há energia suficiente para sustentar o pouso. Um módulo que solicitar autorização **antes de t = 1h** ou **após t = 11h** recebe a primeira condição como FALSO e é automaticamente redirecionado para a fila de espera noturna.

### ② Planejamento da Fila — Capacidade Máxima por Janela

Cada pouso consome em média **800 W** de potência dos sistemas da base (computação, comunicação, iluminação da pista, retrofoguetes auxiliares). O número máximo de módulos que podem pousar simultaneamente é:

$$N_{max}(t) = \left\lfloor \frac{P(t) - P_{reserva}}{P_{por\_pouso}} \right\rfloor = \left\lfloor \frac{P(t) - 1650}{800} \right\rfloor$$

**Exemplo ao meio-dia (t = 6h):**

$$N_{max}(6) = \left\lfloor \frac{5400 - 1650}{800} \right\rfloor = \left\lfloor \frac{3750}{800} \right\rfloor = \left\lfloor 4{,}69 \right\rfloor = \mathbf{4 \text{ módulos simultâneos}}$$

**Exemplo às 9h da manhã (t = 3h):**

$$N_{max}(3) = \left\lfloor \frac{4050 - 1650}{800} \right\rfloor = \left\lfloor \frac{2400}{800} \right\rfloor = \mathbf{3 \text{ módulos}}$$

O MGPEB usa esse cálculo para **distribuir a fila de módulos** ao longo do sol, priorizando os mais críticos para o pico solar e deixando os menos urgentes para as horas intermediárias.

### ③ Alerta de Tempestade de Poeira — Fator de Degradação

A NASA documentou que o InSight teve sua geração reduzida de **5.000 Wh para 500 Wh** por acúmulo de poeira — queda de 90%. O MGPEB aplica um **fator de degradação k** (0 < k ≤ 1) à função:

$$P_{real}(t) = k \cdot (-150t^2 + 1800t)$$

Quando sensores detectam tempestade de poeira (k < 0,5), o limiar de t₁ e t₂ é recalculado automaticamente:

$$-150k \cdot t^2 + 1800k \cdot t = 1650$$
$$t^2 - 12t + \frac{11}{k} = 0$$

Com k = 0,5 (tempestade moderada): a janela operacional **se reduz de 10 para ~6 horas**. Com k < 0,31, a potência jamais atinge o limiar e o MGPEB **suspende todos os pousos do sol**.

---

## 10. Resumo da Modelagem

| Item | Descrição |
|---|---|
| **Função** | P(t) = −150t² + 1800t |
| **Tipo** | Quadrática (2º grau), côncava para baixo |
| **Domínio** | t ∈ [0, 12] horas após o nascer do sol |
| **Imagem** | P(t) ∈ [0, 5.400] watts |
| **Coef. de t²** | −150 → parábola abre para baixo (geração tem máximo) |
| **Coef. de t** | +1800 → crescimento inicial da geração pela manhã |
| **Vértice** | t = 6h, P = 5.400 W → pico ao meio-dia marciano |
| **Eixo de simetria** | t = 6h → curva perfeitamente simétrica pelo meio-dia |
| **Limiar operacional** | P = 1.650 W → t = 1h e t = 11h (janela de 10 horas) |
| **Energia total/sol** | 43.200 Wh = 43,2 kWh por sol marciano |
| **Referência real** | NASA InSight (4.588 Wh/sol, 600–700 W pico) · NASA Glenn Research Center — Mars Solar Power |

---

*Missão Aurora Siger · MGPEB · Passo 4 — Modelagem de Funções Matemáticas*  
*Referências: NASA JPL — InSight Power Generation · NASA Glenn Research Center — Solar Radiation on Mars (Appelbaum & Flood, 1990) · Marspedia — Sunlight · pv-magazine-usa.com — Mars Solar Power Record (2018)*
