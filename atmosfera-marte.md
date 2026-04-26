# Atmosfera de Marte — Dados Técnicos para o MGPEB

> Material de apoio para a atividade integradora FIAP — Missão Aurora Siger

---

## 1. Composição atmosférica

| Componente        | Concentração |
|-------------------|-------------|
| Dióxido de carbono (CO₂) | ~95%   |
| Nitrogênio (N₂)   | ~2,85%      |
| Argônio (Ar)      | ~2%         |
| Oxigênio (O₂)     | ~0,13%      |
| Vapor d'água      | traços      |

A atmosfera marciana é extremamente tênue — cerca de **0,6% da pressão atmosférica da Terra**. Isso tem impacto direto nas condições de pouso dos módulos da colônia.

---

## 2. Pressão atmosférica

- **Pressão média na superfície:** ~610 Pa (6,1 mbar)
- **Variação sazonal:** entre 6,8 mbar (inverno sul) e 9,0 mbar (verão sul), conforme medições dos Vikings
- **Variação por altitude:** a pressão pode variar por um fator de 15 devido à topografia marciana (diferença de altitude de até 30 km entre pontos da superfície)

### Implicação para o MGPEB
A baixa pressão atmosférica significa que paraquedas têm eficiência muito reduzida. Sistemas de pouso devem usar **retrofoguetes** e/ou airbags, aumentando o consumo de combustível. A pressão deve ser monitorada em tempo real para ajustar as decisões de pouso.

**Condição booleana sugerida:**
```
POUSO_AUTORIZADO = (pressao_atual >= PRESSAO_MINIMA) AND (vento_kmh <= VENTO_MAXIMO)
```

---

## 3. Temperatura

| Parâmetro             | Valor              |
|-----------------------|--------------------|
| Temperatura média     | −60 °C             |
| Temperatura diurna    | até −20 °C (equador) |
| Temperatura noturna   | até −125 °C (polos) |
| Variação diária (ΔT)  | ~60 °C             |

A grande variação diária de temperatura tem impacto em:
- Materiais estruturais dos módulos (fadiga térmica)
- Sensores e eletrônica embarcada
- Eficiência dos painéis solares
- Cálculo do momento ideal para pousos noturnos vs. diurnos

### Modelagem matemática sugerida (Função Linear)

Variação de temperatura ao longo do dia marciano (sol = dia marciano de ~24h 37min):

```
T(t) = T_min + (T_max - T_min) × sin(π × t / P)
```

Onde:
- `T(t)` = temperatura em °C no instante t
- `T_min` = temperatura mínima do dia (ex: −80 °C)
- `T_max` = temperatura máxima do dia (ex: −20 °C)
- `P` = período do sol marciano (~88.620 segundos)
- `t` = tempo em segundos desde o amanhecer

---

## 4. Velocidade de entrada e pouso

- **Velocidade de entrada na atmosfera:** ~7,6 km/s a 125 km de altitude
- **Altitude de abertura de paraquedas:** entre 8 e 12 km
- **Altitude de ativação de retrofoguetes:** entre 2 e 0,1 km

### Modelagem de descida (Função Quadrática)

A altura em função do tempo durante a fase de retrofoguetes pode ser aproximada por:

```
h(t) = h0 + v0 × t - (1/2) × a × t²
```

Onde:
- `h0` = altura inicial de ativação dos retrofoguetes (ex: 2.000 m)
- `v0` = velocidade vertical inicial (ex: −80 m/s, negativa pois é descida)
- `a` = desaceleração dos retrofoguetes (ex: 15 m/s²)
- `t` = tempo em segundos

O momento do toque é quando `h(t) = 0`. Isso define o **tempo de queima dos retrofoguetes** e o **consumo de combustível total**.

---

## 5. Tempestades de poeira

Marte é famoso pelas suas tempestades de poeira, que podem durar **semanas ou meses** e cobrir o planeta inteiro.

| Tipo de tempestade | Duração estimada | Impacto nos pousos |
|--------------------|-----------------|-------------------|
| Local              | horas a dias     | Reduz visibilidade, aumenta risco |
| Regional           | dias a semanas   | Pode suspender todos os pousos |
| Global             | semanas a meses  | Suspensão total, redução de ~99% da energia solar |

### Implicação para o MGPEB
Módulos aguardando na órbita devem ser movidos para **pilha de espera** durante tempestades globais.

**Condição booleana sugerida:**
```
ALERTA_TEMPESTADE = (opacidade_atmosferica > LIMIAR_OPTICO) OR (velocidade_vento > 25 m/s)
POUSO_BLOQUEADO = ALERTA_TEMPESTADE AND NOT (modulo.criticidade == "EMERGENCIA")
```

---

## 6. Radiação

A ausência de campo magnético global em Marte e a tênue atmosfera resultam em níveis de radiação muito superiores aos da Terra:

- Radiação na superfície de Marte: **~0,7 mSv/dia** (vs. ~0,003 mSv/dia na Terra)
- Isso é ~170 vezes mais que na superfície terrestre
- Eventos de ejeção de massa coronal (CMEs) podem aumentar esse valor por um fator de 10-50×

### Implicação para hardware
Processadores e memórias usados no MGPEB devem ser **tolerantes à radiação** (rad-hard), o que limita drasticamente a capacidade de processamento disponível (ver `computadores-espaciais.md`).

---

## Fontes

- [Atmosphere of Mars — Wikipedia](https://en.wikipedia.org/wiki/Atmosphere_of_Mars)
- [Mars Atmosphere, Climate, Weather — Space.com](https://www.space.com/16903-mars-atmosphere-climate-weather.html)
- [Martian Atmosphere and Its Effects on Propagation — NASA/JPL](https://descanso.jpl.nasa.gov/propagation/mars/MarsPub_sec3.pdf)
- [Mars — Atmosphere, Surface, Pressure — Britannica](https://www.britannica.com/place/Mars-planet/Composition-and-surface-pressure)
- Howard Jr., R. L. (2021). *Common Habitat Base Camp for Moon and Mars Surface Operations*. NASA Johnson Space Center.
