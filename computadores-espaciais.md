# História dos Computadores Espaciais — Contextualização do MGPEB

> Material de apoio para a atividade integradora FIAP — Missão Aurora Siger

---

## 1. Do ENIAC ao Apolo: os primeiros computadores de propósito geral

A história da computação começa com máquinas enormes, lentas e extremamente frágeis. O ENIAC (1945), considerado o primeiro computador eletrônico de propósito geral, pesava 27 toneladas, ocupava 167 m² e executava cerca de 5.000 operações por segundo — uma fração ínfima do que qualquer smartphone atual faz.

**A grande transição:** O surgimento dos transistores (1947, Bell Labs) e depois dos circuitos integrados (1958, Jack Kilby) permitiu miniaturizar drasticamente os computadores. Essa miniaturização foi absolutamente fundamental para o surgimento dos **sistemas embarcados** nas décadas seguintes.

---

## 2. O Computador de Guia do Apollo (AGC) — 1969

O **Apollo Guidance Computer (AGC)** é considerado o primeiro computador embarcado de missão crítica da história. Ele guiou os astronautas da Apollo 11 até a Lua e de volta em 1969.

| Especificação | AGC (1969) | iPhone 15 (2024) |
|---------------|-----------|-----------------|
| Clock | 2,048 MHz | 3.770 MHz |
| RAM | 4 KB | 6 GB |
| Armazenamento | 72 KB (ROM) | 512 GB |
| Transistores | ~5.600 | ~19 bilhões |
| Peso | 32 kg | 0,17 kg |

O AGC foi projetado com **redundância tripla** — três computadores trabalhando em paralelo, com votação por maioria para decisões críticas. Esse princípio ainda é usado hoje em sistemas de missão crítica.

**Relevância para o MGPEB:** O princípio de tolerância a falhas do AGC (redundância + votação) deve guiar o projeto do MGPEB. Um sistema de controle de pouso em Marte não pode ter ponto único de falha.

---

## 3. A evolução dos computadores nos rovers marcianos

A sequência de rovers marcianos ilustra perfeitamente como as limitações de hardware moldaram as escolhas de software e algoritmos:

| Rover | Ano | Processador | Clock | RAM | Flash |
|-------|-----|------------|-------|-----|-------|
| Sojourner | 1997 | Intel 80C85 | 2 MHz | 512 KB | — |
| Spirit / Opportunity | 2004 | RAD6000 | 20 MHz | 128 MB | 256 MB |
| Curiosity | 2012 | RAD750 | 200 MHz | 256 MB | 2 GB |
| Perseverance | 2021 | RAD750 | 200 MHz | 256 MB | 2 GB |

**Observação importante:** O Perseverance usa exatamente o mesmo processador que o Curiosity (RAD750, lançado em 2001), baseado na arquitetura do PowerPC 603 — o mesmo chip do iMac G3 de 1997. Isso não é falta de ambição, é engenharia conservadora deliberada para um ambiente extremo.

---

## 4. Por que computadores espaciais são tão "lentos"?

### 4.1 Radiação — o inimigo invisível

Em Marte, a ausência de campo magnético global e a atmosfera tênue expõem os eletrônicos a:
- **Raios cósmicos** — partículas de alta energia que atravessam circuitos
- **Eventos de partícula única (SEU)** — um próton cósmico pode "virar" um bit de 0 para 1 ou vice-versa
- **Latch-up** — um raio cósmico pode criar um curto-circuito que queima o chip permanentemente

**Solução:** Processadores **rad-hard (radiation-hardened)** usam transistores maiores e mais espaçados, técnicas de fabricação especiais e blindagem. O custo: são ordens de magnitude mais caros e muito mais lentos que chips comerciais equivalentes.

### 4.2 Temperatura extrema

Variações de −125 °C a 20 °C destroem componentes eletrônicos comuns. Soluções:
- Aquecedores elétricos para manter os chips dentro da faixa operacional
- Materiais especiais para PCBs (placas de circuito)

### 4.3 Consumo de energia

Cada Watt gasto em processamento é um Watt a menos para aquecimento, comunicação ou instrumentos científicos. Isso limita drasticamente o clock dos processadores.

---

## 5. Implicações para o MGPEB

As limitações de hardware de uma missão real em Marte devem guiar as escolhas de design do MGPEB:

### 5.1 Algoritmos devem ser simples e previsíveis

Algoritmos com **complexidade O(n²)** ou maior devem ser evitados para filas grandes. Para uma base com dezenas de módulos, algoritmos O(n log n) como **Merge Sort** ou **Quick Sort** são superiores ao Bubble Sort O(n²), especialmente em hardware limitado.

**Exemplo prático:**
- Ordenar 100 módulos com Bubble Sort: ~10.000 operações
- Ordenar 100 módulos com Merge Sort: ~700 operações
- Em um processador de 20 MHz com outras tarefas paralelas, essa diferença é significativa

### 5.2 Estruturas de dados devem ter tamanho fixo previsível

Em hardware com memória limitada (256 MB de RAM para TODO o sistema operacional + aplicações), listas com alocação dinâmica ilimitada são perigosas. O MGPEB deve ter:
- Tamanho máximo da fila definido em compilação
- Alertas quando a fila atinge 80% da capacidade
- Política de descarte para quando a capacidade máxima é atingida

### 5.3 Tolerância a falhas via redundância de dados

Memória pode ser corrompida por radiação. Estratégias:
- **ECC (Error Correcting Code):** detecta e corrige erros de 1 bit automaticamente
- **Checksum:** valida integridade dos dados antes de processar
- **Tripla redundância:** dados críticos armazenados em 3 locais, com leitura por votação

### 5.4 Código simples é código confiável

Em missões espaciais, código menos complexo é preferível mesmo que menos eficiente. Um bug em Marte não pode ser corrigido com uma visita do técnico. O MGPEB deve:
- Evitar recursão (risco de stack overflow em memória limitada)
- Preferir laços iterativos simples
- Comentar extensivamente (para manutenção remota por atualizações de software)

---

## 6. Linha do tempo: da sala de máquinas ao espaço profundo

```
1945 → ENIAC (27 toneladas, propósito geral)
1947 → Transistor (Bell Labs)
1958 → Circuito integrado (Jack Kilby, Texas Instruments)
1969 → AGC — primeiro computador embarcado de missão crítica (Apollo 11)
1971 → Intel 4004 — primeiro microprocessador comercial
1977 → Voyager — computadores de 8 bits guiam sonda ao sistema solar externo
1997 → Sojourner — primeiro rover em Marte (Intel 80C85, 2 MHz)
2004 → Spirit/Opportunity — RAD6000 a 20 MHz
2012 → Curiosity — RAD750 a 200 MHz
2021 → Perseverance — RAD750 + Ingenuity helicopter com Qualcomm Snapdragon
2026 → Aurora Siger — MGPEB (missão fictícia FIAP)
```

---

## 7. O MGPEB na perspectiva histórica

O MGPEB representa a convergência de décadas de evolução computacional:
- Herdeiro dos princípios de tolerância a falhas do AGC (1969)
- Usando algoritmos de busca e ordenação desenvolvidos nos anos 1960-70
- Rodando em hardware rad-hard semelhante ao dos rovers atuais
- Mas agora gerenciando não uma sonda robótica, mas uma **colônia humana** — o passo mais ousado da história da exploração espacial

---

## Fontes

- [Comparison of embedded computer systems on Mars rovers — Wikipedia](https://en.wikipedia.org/wiki/Comparison_of_embedded_computer_systems_on_board_the_Mars_rovers)
- [NASA's Perseverance rover has a 1997 computer chip brain — Big Think](https://bigthink.com/hard-science/perseverance-rover-brain/)
- [How NASA Built Artemis II's Fault-Tolerant Computer — Communications of the ACM](https://cacm.acm.org/news/how-nasa-built-artemis-iis-fault-tolerant-computer/)
- [Radiation Hardened Electronics — BAE Systems](https://www.baesystems.com/en-us/product/radiation-hardened-electronics)
- Howard Jr., R. L. (2021). *Common Habitat Base Camp for Moon and Mars Surface Operations*. NASA Johnson Space Center.
