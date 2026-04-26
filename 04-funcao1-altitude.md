# Função 1 — Altitude em Função do Tempo durante a Descida Propulsionada
**Missão Aurora Siger · MGPEB — Módulo de Gerenciamento de Pouso e Estabilização de Base**

> **Tipo de função:** Quadrática (2º grau)  
> **Inspiração real:** NASA Perseverance EDL (Jezero Crater, 2021) · SpaceX Starship Mars Landing concept

---

## 1. Contexto Real — NASA e SpaceX

A fase mais crítica de qualquer missão marciana é chamada de **EDL — Entry, Descent and Landing** ("Sete Minutos de Terror", como a NASA a denomina). O processo começa com a nave viajando a cerca de **20.000 km/h** e termina com o módulo parado na superfície sete minutos depois.

A descida é dividida em três fases distintas:

| Fase | Altitude | Velocidade | Método de Frenagem |
|---|---|---|---|
| Entrada atmosférica | 125 km → 11 km | 20.000 → 1.512 km/h | Escudo térmico + arrasto |
| Descida com paraquedas | 11 km → 2 km | 1.512 → 360 km/h | Paraquedas supersônico |
| **Descida propulsionada** | **2 km → 0 m** | **360 → 0 km/h** | **Retrofoguetes** |

A modelagem matemática desta atividade foca na **fase de descida propulsionada** — o momento em que os retrofoguetes assumem o controle e desaceleram o módulo até o pouso suave.

> 📡 **Dado real NASA:** O Perseverance iniciou sua descida propulsionada a aproximadamente **2 km de altitude** com velocidade de ~**100 m/s** para baixo, após a separação do backshell e do paraquedas. O Sky Crane (guindaste espacial) então ativou seus retrofoguetes para o pouso final.

> 🚀 **Dado real SpaceX:** O Starship entrará na atmosfera marciana a **7,5 km/s** e utilizará **retropropulsão supersônica** — a mesma tecnologia validada nos pousos do Falcon 9 na Terra — para a descida propulsionada final em Marte.

---

## 2. Dedução da Fórmula Matemática

### Princípio físico: Equação do Movimento Uniformemente Variado

Com os retrofoguetes ativos, o módulo sofre **dois efeitos simultâneos**:

- ⬇️ A **gravidade marciana** puxa o módulo para baixo → aceleração de **3,72 m/s²**
- ⬆️ Os **retrofoguetes** empurram o módulo para cima → aceleração de frenagem

A aceleração **resultante líquida** (para cima) é:

$$a_{liquida} = a_{retro} - g_{Marte}$$

Adotando os parâmetros dos módulos da Aurora Siger:
- **a_retro = 6,22 m/s²** (empuxo dos retrofoguetes para cima)
- **g_Marte = 3,72 m/s²** (gravidade marciana para baixo)
- **a_líquida = +2,5 m/s²** (resultado: aceleração líquida de frenagem, para cima)

A equação clássica da cinemática para a posição é:

$$h(t) = h_0 + v_0 \cdot t + \frac{1}{2} \cdot a \cdot t^2$$

Substituindo os valores iniciais:

$$h(t) = 2000 + (-100) \cdot t + \frac{1}{2} \cdot (2{,}5) \cdot t^2$$

### Resultado — Fórmula do MGPEB:

$$\boxed{h(t) = 1{,}25t^2 - 100t + 2000}$$

### Verificação do Pouso Suave

Para que o pouso seja considerado **suave e seguro**, duas condições devem ser satisfeitas simultaneamente no instante do toque (t = T):

**Condição 1 — Altitude zero:**
$$h(T) = 1{,}25T^2 - 100T + 2000 = 0$$
$$T = \frac{100 \pm \sqrt{100^2 - 4 \cdot 1{,}25 \cdot 2000}}{2 \cdot 1{,}25} = \frac{100 \pm \sqrt{10000 - 10000}}{2{,}5} = \frac{100}{2{,}5} = \mathbf{40 \text{ s}}$$

**Condição 2 — Velocidade zero (pouso suave):**
$$v(t) = h'(t) = 2{,}5t - 100$$
$$v(40) = 2{,}5 \cdot 40 - 100 = 100 - 100 = \mathbf{0 \text{ m/s}} \checkmark$$

O módulo toca o solo em **t = 40 s** com velocidade **zero** — pouso suave confirmado.

---

## 3. Significado dos Parâmetros

| Símbolo | Valor | Papel na função | Significado físico |
|---|---|---|---|
| **h(t)** | — | Variável dependente | Altitude do módulo em relação ao solo (m) |
| **t** | — | Variável independente | Tempo desde o início da descida propulsionada (s) |
| **1,25** | Coeficiente de t² | Abre a parábola para cima | Metade da aceleração líquida de frenagem: ½ × 2,5 |
| **−100** | Coeficiente de t | Inclina a curva para baixo inicialmente | Velocidade inicial downward de −100 m/s |
| **2.000** | Termo independente | Intercepta o eixo vertical | Altitude inicial h₀ = 2.000 m ao ligar os retrofoguetes |
| **t = 40 s** | Raiz da equação | Vértice da parábola (mínimo) | Instante do toque no solo |

> ⚠️ **Domínio da função:** t ∈ [0, 40] segundos. Fora desse intervalo, a função não tem significado físico (o módulo já pousou).  
> **Imagem da função:** h(t) ∈ [0, 2.000] metros.

---

## 4. Tabela de Valores

Calculando **h(t) = 1,25t² − 100t + 2.000** para instantes selecionados:

| Tempo t (s) | Cálculo | h(t) (m) | v(t) = 2,5t − 100 (m/s) | Status |
|:---:|---|:---:|:---:|:---:|
| 0  | 1,25×0 − 0 + 2000      | **2.000** | −100,0 m/s | 🔵 Início da queima |
| 5  | 1,25×25 − 500 + 2000   | **1.531** | −87,5 m/s  | ✅ Descida normal |
| 10 | 1,25×100 − 1000 + 2000 | **1.125** | −75,0 m/s  | ✅ Descida normal |
| 15 | 1,25×225 − 1500 + 2000 | **781**   | −62,5 m/s  | ✅ Descida normal |
| 20 | 1,25×400 − 2000 + 2000 | **500**   | −50,0 m/s  | ⚠️ Ponto de não retorno |
| 25 | 1,25×625 − 2500 + 2000 | **281**   | −37,5 m/s  | ⚠️ Atenção à velocidade |
| 27 | 1,25×729 − 2700 + 2000 | **211**   | −32,5 m/s  | 🔴 Alerta: h < 200 m |
| 30 | 1,25×900 − 3000 + 2000 | **125**   | −25,0 m/s  | 🔴 Final de aproximação |
| 35 | 1,25×1225 − 3500 + 2000| **31**    | −12,5 m/s  | 🔴 Pouso iminente |
| 40 | 1,25×1600 − 4000 + 2000| **0**     | 0,0 m/s    | 🟢 Pouso suave confirmado |

**Observação importante:** A velocidade v(t) é **sempre negativa** durante a descida (módulo caindo), mas vai se aproximando de zero — isso representa o módulo desacelerando progressivamente até o pouso suave.

---

## 5. Análise Qualitativa do Gráfico

```
h(t) (m)
2000 |●
     |  \
1531 |    \
     |      \
1125 |        \
     |          \
 781 |            \
     |              \
 500 |_ _ _ _ _ _ _ _●_ _ _ _ ⚠️ PONTO DE NÃO RETORNO
     |                 \
 281 |                   \
     |                     \
 200 |_ _ _ _ _ _ _ _ _ _ _ _\_ _ 🔴 ALERTA (h < 200 m)
     |                        \
 125 |                          \
     |                            \
  31 |                               \
     |                                  \
   0 +--+--+--+--+--+--+--+--+--+--+---●→ t (s)
     0  5 10 15 20 25 27 30       35  40
```

### O que o gráfico revela:

**📉 Forma da parábola — côncava para cima**  
O coeficiente de t² é **positivo (+1,25)**, portanto a parábola abre para cima. Visualmente, a curva desce cada vez mais devagar — o módulo vai **desacelerando** progressivamente até tocar o solo. É exatamente o comportamento esperado de uma frenagem controlada por retrofoguetes.

**📐 Vértice da parábola = ponto de pouso**  
O vértice de uma parábola `h(t) = at² + bt + c` ocorre em:

$$t_{vertice} = \frac{-b}{2a} = \frac{-(-100)}{2 \times 1{,}25} = \frac{100}{2{,}5} = 40 \text{ s}$$

O vértice é justamente o ponto de menor altitude — o **toque no solo** (h = 0). Não existe um "rebote": após t = 40 s, a função matematicamente voltaria a crescer, mas fisicamente o módulo já está pousado e os motores foram desligados.

**🎯 Ponto inicial (t = 0)**  
Em t = 0, h(0) = **2.000 m**. É o ponto onde a parábola intercepta o eixo vertical, representando a altitude em que os retrofoguetes foram acionados. Abaixo desse ponto, não há mais paraquedas — apenas o empuxo dos motores.

**📊 O que acontece quando as variáveis aumentam ou diminuem:**

| Variação | Efeito em h(t) |
|---|---|
| *t* aumenta (tempo passa) | h(t) **diminui** — módulo se aproxima do solo |
| *a_retro* maior (frenagem mais forte) | Coef. t² sobe, parábola mais "fechada" — pouso em menos tempo |
| *a_retro* menor (frenagem insuficiente) | Parábola mais "aberta" — módulo pode não parar a tempo e bater no solo |
| *v₀* maior em módulo (mais rápido no início) | Coef. t mais negativo — descida mais abrupta no início |
| *h₀* maior (começa mais alto) | Parábola deslocada para cima — mais tempo disponível para frear |
| *g_Marte* maior (gravidade maior) | *a_líquida* diminui — mais difícil frear, parábola mais larga |

**⚠️ Caso crítico — frenagem insuficiente:**  
Se a aceleração dos retrofoguetes for menor que 3,72 m/s² (igual à gravidade marciana), a aceleração líquida se torna zero ou negativa, e o módulo **nunca para de acelerar para baixo** — colidindo com a superfície. Esse é o cenário que o MGPEB deve detectar e bloquear antes de autorizar o pouso.

---

## 6. Cálculo dos Instantes Críticos para o MGPEB

### Ponto de Não Retorno — h = 500 m

Abaixo de 500 m, um abort (cancelamento do pouso) já não é mais possível. O MGPEB deve ter confirmado todas as condições antes desse ponto. Calculando o instante exato:

$$1{,}25t^2 - 100t + 2000 = 500$$
$$1{,}25t^2 - 100t + 1500 = 0$$
$$t = \frac{100 \pm \sqrt{10000 - 7500}}{2{,}5} = \frac{100 \pm \sqrt{2500}}{2{,}5} = \frac{100 \pm 50}{2{,}5}$$

$$t = \frac{50}{2{,}5} = \mathbf{20 \text{ s}}$$

Em **t = 20 s**, o módulo está a exatamente **500 m** de altitude. A partir daí, o pouso é irreversível.

### Alerta de Aproximação Final — h = 200 m

Abaixo de 200 m, o MGPEB ativa o protocolo de aproximação final com potência máxima dos retrofoguetes:

$$1{,}25t^2 - 100t + 2000 = 200$$
$$1{,}25t^2 - 100t + 1800 = 0$$
$$t = \frac{100 \pm \sqrt{10000 - 9000}}{2{,}5} = \frac{100 \pm \sqrt{1000}}{2{,}5} \approx \frac{100 \pm 31{,}6}{2{,}5}$$

$$t \approx \frac{68{,}4}{2{,}5} \approx \mathbf{27{,}4 \text{ s}}$$

Em **t ≈ 27 s**, o módulo entra na zona de alerta final a ~200 m de altitude, com velocidade de queda de ~32 m/s.

---

## 7. Conexão com as Decisões de Engenharia do MGPEB

A função h(t) = 1,25t² − 100t + 2.000 orienta três decisões críticas do sistema:

### ① Janela de Ativação dos Retrofoguetes

O MGPEB calcula o instante exato para acionar os motores **antes** do módulo entrar em órbita de pouso, garantindo que a altitude h₀ = 2.000 m seja respeitada. Se os retrofoguetes forem acionados tarde demais (h₀ menor), o vértice da parábola não chegará a zero: o módulo baterá no solo em alta velocidade.

Usando a fórmula de forma inversa — dado h_ativacao e v₀, calcular *a_retro* mínima necessária:

$$a_{retro_{min}} = g_{Marte} + \frac{v_0^2}{2 \cdot h_0} = 3{,}72 + \frac{100^2}{2 \times 2000} = 3{,}72 + 2{,}5 = \mathbf{6{,}22 \text{ m/s}^2}$$

### ② Autorização de Pouso — Regra Booleana Integrada

A autorização é bloqueada se qualquer condição falhar antes de t = 20 s (h > 500 m). Em Python, essa condição pode ser implementada da seguinte forma:

```python
def velocidade_esperada(t):
    return 2.5 * t - 100  # v(t) = 2,5t - 100

autorizar_pouso = (
    combustivel > 800
    and velocidade_atual <= velocidade_esperada(t)
    and area_pouso_livre
    and sensores_ok
)
```

A velocidade esperada no instante *t* vem diretamente da derivada da função. Se a velocidade real for **mais negativa** que a esperada, os retrofoguetes estão com falha — pouso bloqueado.

### ③ Priorização de Módulos na Fila — Cálculo de Janela de Pouso

O MGPEB usa a função h(t) para calcular a **janela de tempo disponível** antes que um módulo em órbita de pouso consuma todo seu combustível acima da altitude segura:

$$t_{janela} = t_{nao\_retorno} - t_{atual} = 20 - t_{atual}$$

Módulos com menor janela disponível são priorizados na fila de pouso, integrando diretamente o algoritmo de ordenação com a modelagem matemática da descida.

---

## 8. Resumo da Modelagem

| Item | Descrição |
|---|---|
| **Função** | h(t) = 1,25t² − 100t + 2.000 |
| **Tipo** | Quadrática (2º grau), côncava para cima |
| **Domínio** | t ∈ [0, 40] segundos |
| **Imagem** | h(t) ∈ [0, 2.000] metros |
| **Coef. de t²** | +1,25 → parábola abre para cima (frenagem) |
| **Coef. de t** | −100 → velocidade inicial de 100 m/s para baixo |
| **Termo independente** | 2.000 → altitude inicial (h₀) |
| **Vértice** | t = 40 s, h = 0 m → ponto de pouso |
| **Ponto de não retorno** | t = 20 s, h = 500 m |
| **Alerta de aproximação** | t ≈ 27 s, h ≈ 200 m |
| **Gravidade em Marte** | 3,72 m/s² (38% da terrestre) |
| **Referência real** | NASA Perseverance EDL · SpaceX Starship Mars concept |

---

*Missão Aurora Siger · MGPEB · Passo 4 — Modelagem de Funções Matemáticas*  
*Referências: NASA JPL — Mars 2020 EDL Press Kit · NASASpaceFlight.com — Perseverance EDL Timeline · Marspedia — Landing on Mars · SpaceX Starship Technical Overview*
