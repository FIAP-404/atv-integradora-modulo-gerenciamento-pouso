# 5. Contextualização do MGPEB à Luz da Evolução da Computação

> Seção 5 — Atividade Integradora FIAP — Módulo de Gerenciamento de Pouso e Estabilização de Base (MGPEB)
> Missão Aurora Siger

---

## 5.1 Introdução

Para compreender verdadeiramente o MGPEB (Módulo de Gerenciamento de Pouso e Estabilização de Base), é fundamental mergulhar na história da computação — especificamente, na trajetória dos **computadores de propósito geral** até os modernos **sistemas embarcados de alta confiabilidade** que hoje controlam missões espaciais.

O MGPEB não surge do nada. Ele é herdeiro de décadas de evolução tecnológica, aprendizados de falhas históricas, e inovações em engenharia de sistemas. Compreender essa trajetória não é apenas um exercício acadêmico — é essencial para entender **por que** o MGPEB foi projetado de determinada forma e **quais limitações** influenciam suas escolhas de algoritmos e estruturas de dados.

Esta seção examina:
1. A história dos primeiros computadores de propósito geral
2. O legado do Apollo Guidance Computer
3. A evolução dos computadores espaciais até os rovers marcianos
4. As limitações de hardware típicas de missões em Marte
5. Como essas limitações moldam o MGPEB

---

## 5.2 Os Primários Computadores de Propósito Geral

### 5.2.1 ENIAC (1945) — O beginning

O **ENIAC** (Electronic Numerical Integrator and Computer), completado em 1945 na Universidade da Pensilvânia, é considerado o primeiro computador eletrônico de propósito geral da história. Foi projetado para calcular tabelas de balística para o exército americano durante a Segunda Guerra Mundial.

**Características Técnicas:**

| Especificação | Valor |
|--------------|-------|
| Peso | 27 toneladas |
| Área occupation | 167 m² (~280 m² de área de superfície) |
| Consumo de energia | 150 kW |
| Velocidade de processamento | ~5.000 operações por segundo |
| Memória | 20 registradores de 10 dígitos |
| Componentes | ~18.000 válvulas de vácuo |

**Limitações:**
- Precisava de semanas para ser reprogramado (relogiação manual)
- Vulnerável a falhas de válvulas (manutenção constante)
- Gerava calor extremo (sala refrigerada constante)
- Não tinha armazenamento permanente de programas

**Relevância para o MGPEB:** O ENIAC demonstra que os primeiros computadores não eram adequados para operações em tempo real. Cada mudança de função exigia modificações físicas. Essa limitação moldou a necessidade de **software reutilizável** — uma lição que o MGPEB aplica diretamente em seu design modular.

### 5.2.2 A Revolução do Transistor (1947)

Em dezembro de 1947, John Bardeen, Walter Brattain e William Shockley (Bell Labs) inventaram o **transistor de junção**, substituindo as frágeis válvulas de vácuo por componentes sólidos minúsculos.

**Impacto:**
- Computers passaram de toneladas para quilogramas
- Confiabilidade aumentou drasticamente
- Consumo de energia caiu exponencialmente
- Custo de fabricação despencou

Para o MGPEB, o transistor é fundamental: nossos processors espaciais usam transistores rad-hard (tolerantes à radiação) como descendentes diretos dessa invenção.

### 5.2.3 Circuits Integrados (1958)

Jack Kilby (Texas Instruments) e Robert Noyce (Fairchild Semiconductor) criaram independentemente o **circuito integrado** — múltiplos transistores gravados em uma única pastilha de silício.

A miniaturização possibilitou:
-Computers para aplicações embarcadas
- Confiabilidade para uso aeroespacial
- Redução drástica de peso e energia

Este é o princípio que permite ao MGPEB operar em um módulo de pouso com recursos limitados.

---

## 5.3 O Apollo Guidance Computer (AGC) — 1969

O **Apollo Guidance Computer (AGC)** é o ancestral directo do MGPEB. Desenvolvido pelo MIT Instrumentation Laboratory para a missão Apollo, foi o primeiro computador embarcado de **missão crítica** da história — literalmente guiando astronautas da Apollo 11 à Lua e de volta.

### 5.3.1 Arquitetura do AGC

```
┌─────────────────────────────────────────┐
│         APOLLO GUIDANCE COMPUTER            │
│              (AGC)                     │
├─────────────────────────────────────────┤
│  ┌─────────────────────────────┐       │
│  │    PROCESSADOR            │       │
│  │    CPU: 16-bit            │       │
│  │    Clock: 2.048 MHz       │       │
│  │   .word: 15 bits + 1 par. │       │
│  └─────────────────────────────┘       │
│              │                          │
│  ┌─────────────────────────────┐       │
│  │    MEMÓRIA                │       │
│  │    ROM: 72 KB (core rope)   │       │
│  │    RAM: 4 KB (core memory) │       │
│  └─────────────────────────────┘       │
│              │                          │
│  ┌─────────────────────────────┐       │
│  │    INPUT/OUTPUT           │       │
│  │    Display: DSKY          │       │
│  │    Interfaces: 36 canais    │       │
│  └─────────────────────────────┘       │
└─────────────────────────────────────────┘
```

### 5.3.2 Comparação com Tecnologia Atual

| Especificação | AGC (1969) | iPhone 15 (2024) | Razão |
|---------------|-----------|------------------|-------|
| Clock | 2,048 MHz | 3.770 MHz | ~1.840x |
| RAM | 4 KB | 6 GB | ~1.500.000x |
| Armazenamento | 72 KB | 512 GB | ~7.000.000x |
| Transistores | ~5.600 | ~19 bilhões | ~3.400.000x |
| Peso | 32 kg | 0,17 kg | ~188x menor |
| Consumo | 55 W | ~5 W | ~11x menor |

É extraordinário pensar que o iPhone no bolso de qualquer pessoa hoje tem **milhões de vezes** mais capacidade que o computador que levou humanos à Lua.

### 5.3.3 O Princípio da Redundância Tripla

O AGC foi pioneiro no uso de **redundância tripla** para missões críticas:

```
┌─────────────────────────────────────────┐
│         SISTEMA REDUNDANTE              │
│         (Triple Modular Redundancy)      │
├─────────────────────────────────────────┤
│                                         │
│    ┌─────────┐                          │
│    │ CPU 1   │                          │
│    └────┬────┘                          │
│         │                               │
│    ┌────┴────┐    ┌─────────┐        │
│    │ VOTER   │───││ CPU 2   │        │
│    │Circuit  │   └─────────┘           │
│    └────┬────┘    ┌─────────┐        │
│         │─────────││ CPU 3   │        │
│         │         └───���─────┘        │
│         │                              │
│         ▼                              │
│    ┌─────────┐                        │
│    │ DECISÃO  │                        │
│    │ FINAL   │                        │
│    └─────────┘                        │
└─────────────────────────────────────────┘
```

**Como funciona:**
1. Três CPUs idênticas executam o mesmo programa simultaneamente
2. Cada CPU produz uma saída
3. O circuito de votação (voter) compara as três saídas
4. Se 2 de 3 saídas coincidem, essa é a decisão aceita
5. Se uma CPU diverge (por radiação ou falha), ela é ignorada

**Relevância para o MGPEB:** O princípio de tolerância a falhas do AGC deve ser adaptado ao MGPEB. Em Marte, não há possibilidade de reparo humano — um bug pode significar a perda de toda a missão. O MGPEB implementa redundância através de:
- **Checksums** para validar integridade de dados
- **Verificação de dependências** antes de cada pouso
- **Log de auditoria** de todas as decisões
- **Override humano** para emergências

---

## 5.4 Evolução dos Computadores nos Rovers Marcianos

A sequência de rovers marcianos ilustra perfeitamente como as **limitações de hardware** moldaram as escolhas de software e algoritmos ao longo de décadas.

### 5.4.1 Linha do Tempo dos Rovers

| Rover | Ano | Processor | Clock | RAM | Flash | Innovation |
|-------|-----|-----------|-------|-----|-------|------------|
| Sojourner | 1997 | Intel 80C85 | 2 MHz | 512 KB | — | Primeiro rover em Marte |
| Spirit | 2004 | RAD6000 | 20 MHz | 128 MB | 256 MB | rad-hard processor |
| Opportunity | 2004 | RAD6000 | 20 MHz | 128 MB | 256 MB | Longa duração (15 anos) |
| Curiosity | 2012 | RAD750 | 200 MHz | 256 MB | 2 GB | MSL, laboratório móvel |
| Perseverance | 2021 | RAD750 | 200 MHz | 256 MB | 2 GB | + Ingenuity (drone) |

### 5.4.2 Por Que Usar Processadores "Antigos"?

Uma observação surpreendente: o **Perseverance** (2021) usa exatamente o mesmo processador que o Curiosity (2012) — o **RAD750**, baseado na arquitetura do PowerPC 603, cujo chip debutou no **iMac G3 de 1997**.

Isso não é falta de ambição ou descuido — é **engenharia conservadora deliberada**:

**Por que não usar processadores modernos?**
1. **Validação:** Processadores precisam ser validados para uso espacial (~5-10 anos)
2. **Tolerância à radiação:** Chips modernos usa transistores menores que são vulneráveis a radiação
3. **Confiabilidade:** Tecnologias testadas em missões são preferidas a "novidades"
4. **Driver support:** Software robusto leva anos para ser desenvolvido

**Lição para o MGPEB:** Em computação espacial, **confiabilidade** sempre vence sobre **desempenho**. O MGPEB reflete isso usando algoritmos simples e bem testados, ao invés de abordagens mais eficientes porém mais complexas.

---

## 5.5 Limitações de Hardware em Marte

Uma missão em Marte enfrenta limitações drastically diferentes de ambientes computacionais tradicionais. O MGPEB deve operar dentro dessas restrições.

### 5.5.1 Radiação Cósmica

Em Marte, a ausência de campo magnético global e a atmosfera tênue expõem a eletrônica a níveis letais de radiação:

| Fonte | Intensidade (Terra = 1) |
|-------|----------------------|
| Radiação de fundo | ~170x |
| Eventos solares (CME) | ~10-50x |
| Raios cósmicosgalácticos | Constante |

**Problemas causados por radiação:**

1. **SEU (Single Event Upset):** Um único próton cósmico pode "flipar" um bit (0 → 1 ou 1 → 0), corrompendo dados ou instruções

2. **Latch-up:** Radiação pode criar curto-circuito interno, destruindo permanentemente o chip

3. **Degradação cumulativa:** Exposição prolongada degrada performance de transistores

**Soluções implementadas no MGPEB:**
- **Checksums** para validação de dados
- **ECC (Error Correcting Code)** em memória
- **Reinício periódicopara limpar erros acumulados**
- **Decisões via majority voting** quando possível

```
┌─────────────────────────────────────────┐
│     PROTEÇÃO CONTRA RADIAÇÃO NO MGPEB    │
├─────────────────────────────────────────┤
│                                          │
│  DADOS ──► CHECKSUM ──► VALIDAÇÃO        │
│              │                            │
│         ┌────┴────┐                    │
│         │ OK?     │                    │
│         └────┬────┘                    │
│            Sim    Não                    │
│         ┌───┘    └──┐                  │
│         ▼           ▼                    │
│    PROCESSA      REJEITA +               │
│                  REGISTRA               │
│                  ERRO                   │
└─────────────────────────────────────────┘
```

### 5.5.2 Temperatura Extrema

Marte oferece temperaturas que destruiriam electronics comuns:

| Condição | Temperatura |
|---------|-----------|
| Máximo diurno (equador) | ~20 °C |
| Mínimo noturno (polos) | ~-125 °C |
| Variação diária | ~60 °C |

Os processadores do MGPEB precisam operar em toda essa faixa, requerendo:
- **Heaters elétricos** para evitar congelamento
- **Isolamento térmico** passivo
- **Graceful degradation** em temperaturas extremas

### 5.5.3 Memória Limitada

Os rovers atuais usam:

| Recurso | Perseverance | MGPEB (estimado) |
|--------|-------------|-----------------|
| RAM | 256 MB | ~16-64 MB |
| Flash | 2 GB | ~64-256 MB |

O MGPEB não pode se dar ao luxo de ter memória "infinita". Cada estrutura de dados deve ter **tamanho máximo definido** e **políticas de descarte** quando a capacidade é atingida.

**Implicações diretas:**
- Listas com alocação dinâmica ilimitada são proibidas
- Precisamos predefinir maximum de módulos na fila
- Alertas em 80% de capacidade
- Política de descarte de módulos de baixa prioridade

### 5.5.4 Consumo de Energia

Cada Watt gasto em processamento é um Watt a menos para:
- Aquecimento (sobrevivência)
- Comunicação (com a Terra)
- Instrumentos científicos

**Comparativo de consumo:**

| Operação | Consumo (W) |
|---------|-----------|
| Processador em plena carga (RAD750) | ~2-5 W |
| Comunicação (antena de alto ganho) | ~100-150 W |
| Aquecedor de sobrevivência | ~50-200 W |
| Aquecedor de bateria | ~20-50 W |

O MGPEB prioriza **algoritmos eficientes** em energia:
- **Evitar loops desnecessários**
- **Operações batch** quando possível
- **Sleep mode** entre verificações
- **Processamento locais**, minimizando comunicação

### 5.5.5 Latência de Comunicação

Um sinal de Marte para a Terra leva:

| Posição de Marte | Tempo (min) |
|----------------|-------------|
| Mínima distância (~55 milhões km) | ~3 minutos |
| Máxima distância (~400 milhões km) | ~22 minutos |

**Implicação:**
- O MGPEB **não pode** esperar resposta da Terra para decisões críticas
- Deve ser **totalmente autônomo**
- Humans são apenas "consultores" para emergências
- Todo o lógico de decisão está incorporated no próprio módulo

---

## 5.6 Como as Limitações Influenciam o MGPEB

Todas as limitações acima têm **consequências diretas** no design do MGPEB:

### 5.6.1 Escolha de Algoritmos

| Algoritmo | Complexidade | Adequado para MGPEB? |
|----------|--------------|----------------------|
| Bubble Sort | O(n²) | ❌ Não — muito lento |
| Selection Sort | O(n²) | ❌ Não — muito lento |
| Insertion Sort | O(n²) | ⚠️ Apenas para n < 10 |
| **Merge Sort** | O(n log n) | ✅ Sim — eficiente |
| **Quick Sort** | O(n log n) | ✅ Sim — eficiente |
| **Binary Search** | O(log n) | ✅ Sim — obrigatório |

**Decisão:** O MGPEB usa **Quick Sort** para ordenação da fila, sendo O(n log n) — muito superior ao O(n²) do Bubble Sort.

### 5.6.2 Estruturas de Dados

Estruturas de dados devem ser **determinísticas** e com **tamanho limitado**:

| Estrutura | Uso no MGPEB | Limitação |
|----------|-------------|-----------|
| Queue (Fila) | Fila principal de pouso | Máximo: 50 módulos |
| List (Lista) | Módulos pousados, alerta | Máximo: 30 cada |
| Stack (Pilha) | Módulos adiados | Máximo: 20 módulos |

**Controle de capacidade:**
```python
# Exemplo de controle de capacidade no MGPEB
CAPACIDADE_MAXIMA = 50

def adicionar_modulo(fila, modulo):
    if len(fila) >= CAPACIDADE_MAXIMA * 0.8:
        registrar_alerta("Fila atingindo 80% da capacidade")
    
    if len(fila) >= CAPACIDADE_MAXIMA:
        # Política de descarte: remover menor prioridade
        modulo_descartado = remover_menor_prioridade(fila)
        mover_para_espera(modulo_descartado)
        return False
    
    fila.append(modulo)
    return True
```

### 5.6.3 Código Simples é Código Confiável

Princípios de programação do MGPEB:

| Prática | Razão |
|---------|-------|
| **Evitar recursão** | Risco de stack overflow com memória limitada |
| **Preferir loops iterativos** | Mais previsível, mais fácil de debugar |
| **Comentar extensivamente** | Manutenção remota por equipe terrestre |
| **Evitar bibliotecas externas** | Simplificar validação e depuração |
| **Funções pequenas** | Modular, testável, reutilizável |
| **Uma responsabilidade por função** | Manutenibilidade |

### 5.6.4 Tolerância a Falhas

O MGPEB implementa tolerância a falhas em múltiplas camadas:

**Camada 1 �� Validação de dados:**
- Checksum para cada registro
- Verificação de consistência antes de decisões

**Camada 2 — Decisões confirmadas:**
- Múltiplas verificações para decisões críticas
- Log de auditoria de todas as decisões

**Camada 3 — Override humano:**
- Operador humano pode sobrepor decisão automática
- Emergências têm prioridade inquestionável

---

## 5.7 A Jornada da Sala de Máquinas ao Espaço Profundo

Para contextualizar o MGPEB, apresentamos a linha do tempo da computação espacial:

```
1945 ─► ENIAC
        Primeiro computador eletrônico de propósito geral
        27 toneladas, 150 kW, 5.000 ops/s

   │
   ▼
1947 ─► TRANSISTOR
        Bell Labs - miniaturização começa
        -> Computers de quilogramas, não toneladas

   │
   ▼
1958 ─► CIRCUITO INTEGRADO
        Jack Kilby - múltiplos transistores em um chip
        -> Nacimento da computação embarcada

   │
   ▼
1969 ─► AGC (Apollo Guidance Computer)
        Primeiro computador de missão crítica
        32 kg, 55 W, 2 MHz
        -> Guiou humanos até a Lua
        -> Introduziu redundância tripla

   │
   ▼
1971 ─► INTEL 4004
        Primeiro microprocessador comercial
        -> Computadores pessoais

   │
   ▼
1977 ─► VOYAGER
        Computers de 8 bits exploram sistema solar externo
        -> Missões de longa duração

   │
   ▼
1997 ─► SOJOURNER
        Primeiro rover em Marte
        Intel 80C85, 2 MHz, 512 KB RAM
        -> Robots em altri planeta

   │
   ▼
2004 ─► SPIRIT / OPPORTUNITY
        RAD6000, 20 MHz, 128 MB RAM
        -> Processadores rad-hard especializados

   │
   ▼
2012 ─► CURIOSITY
        RAD750, 200 MHz, 256 MB RAM
        -> Laboratório científico móvel

   │
   ▼
2021 ─► PERSEVERANCE + INGENUITY
        RAD750 + Snapdragon (drone)
        -> Missão mais complexa já enviada a Marte

   │
   ▼
2026 ─► AURORA SIGER - MGPEB
        Gerenciamento de colônia completa
        -> Primeiro sistema a gerenciar colonists, não apenas robots
```

---

## 5.8 Conclusão

O MGPEB representa a convergência de **oitenta anos de evolução computacional** — do ENIAC ao processamento multi-core, dos 150 kW de consumo aos watts limitados de uma missão marciana.

### 5.8.1 Legado do AGC

O princípio mais importante herdado do Apollo Guidance Computer é a **tolerância a falhas através de redundância e verificação**. O MGPEB nunca toma uma decisão crítica sem validar os dados.

### 5.8.2 Lições dos Rovers Marcianos

Os rovers ensinaram que:
- **Confiabilidade** > Desempenho
- **Simplicidade** > Elegância
- **Validação** > Assunção
- **Autonomia** > Dependência

### 5.8.3 Limitações como Oportunidades

As limitações de hardware marciano — memória, energia, radiação, temperatura — não são apenas obstáculos. Elas impuseram **disciplina de engenharia** que resultou em sistemas mais robustos. O MGPEB herda essa disciplina:

- Algoritmos O(n log n) em vez de O(n²)
- Estruturas de dados com tamanho máximo definido
- Código simples, bem comentado, testável
- Múltiplas camadas de validação
- Override humano para emergências

### 5.8.4 Para Onde Vamos

O MGPEB não é o fim da jornada — é um passo. Assim como o AGC abriu caminho para os rovers marcianos, o MGPEB abre caminho para:
- Gestão autônoma de colônias maiores
- Coordenação multi-base em Marte
- Sistema de backup de outrasmissões
- Protocolos para futuras missões a Lua, Europa, Titã

A história da computação espacial continua — e o MGPEB é o próximo capítulo.

---

## Referências

1. Wikipedia. "Comparison of embedded computer systems on board the Mars rovers." https://en.wikipedia.org/wiki/Comparison_of_embedded_computer_systems_on_board_the_Mars_rovers

2. Big Think. "NASA's Perseverance rover has a 1997 computer chip brain." https://bigthink.com/hard-science/perseverance-rover-brain/

3. Communications of the ACM. "How NASA Built Artemis II's Fault-Tolerant Computer." https://cacm.acm.org/news/how-nasa-built-artemis-iis-fault-tolerant-computer/

4. BAE Systems. "Radiation Hardened Electronics." https://www.baesystems.com/en-us/product/radiation-hardened-electronics

5. Howard Jr., R. L. (2021). *Common Habitat Base Camp for Moon and Mars Surface Operations*. NASA Johnson Space Center.

6. MIT Museum. "Apollo Guidance Computer (AGC)." MIT Instrumentation Laboratory Archives.

7. Wikipedia. "Apollo 11" — Computer systems. https://en.wikipedia.org/wiki/Apollo_11