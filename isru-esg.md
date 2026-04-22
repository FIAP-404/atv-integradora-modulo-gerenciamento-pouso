# ISRU e ESG — Produção Local de Recursos e Governança na Base Aurora Siger

> Material de apoio para a atividade integradora FIAP — Missão Aurora Siger

---

## 1. O que é ISRU?

**ISRU (In-Situ Resource Utilization)** significa o aproveitamento de recursos encontrados no local da missão — no caso de Marte, extrair e processar materiais da atmosfera e do solo marciano para produzir o que a colônia precisa.

Isso elimina (ou reduz drasticamente) a necessidade de trazer tudo da Terra, o que é fundamental para a viabilidade econômica e operacional de uma colônia permanente.

---

## 2. Recursos produzíveis em Marte

### 2.1 Oxigênio (O₂)

O experimento **MOXIE** (Mars Oxygen In-Situ Resource Utilization Experiment), embarcado no rover Perseverance, demonstrou pela primeira vez em **20 de abril de 2021** a produção de oxigênio a partir do CO₂ da atmosfera marciana.

**Processo:** Eletrólise de óxido sólido (SOEC)
```
2 CO₂ → 2 CO + O₂
```

- Produção demonstrada: ~6 gramas de O₂ por hora
- Escala necessária para missão humana: ~2 kg/hora (para propelente de retorno)
- Aplicações: respiração, oxidante para propelente

### 2.2 Metano (CH₄) — Propelente

Usando a **Reação de Sabatier**:
```
CO₂ + 4H₂ → CH₄ + 2H₂O
```

O metano produzido serve como propelente para foguetes. Combinado com o O₂ produzido pelo MOXIE, é possível fabricar o combustível de retorno diretamente em Marte, tornando a missão de ida e volta viável.

### 2.3 Água (H₂O)

- Encontrada como gelo no subsolo marciano e nas calotas polares
- Pode ser extraída por aquecimento do regolito (solo marciano)
- Usos: consumo humano, eletrólise (H₂ para Sabatier + O₂ para respiração), cultivo de alimentos

### 2.4 Regolito (solo marciano)

- Pode ser sinterizado (fundido por calor) para criar estruturas sólidas
- Impressão 3D com regolito para construção civil na base
- Fornece blindagem contra radiação quando usado como cobertura sobre habitats

---

## 3. ISRU na Base Aurora Siger — Aplicação prática

Inspirado no documento da NASA (Howard Jr., 2021), a Base Aurora Siger deve ter uma **Zona de Produção de Recursos** separada da zona de habitação, com:

| Equipamento | Função |
|-------------|--------|
| Plantas ISRU fixas | Produção contínua de O₂ e CH₄ |
| ATHLETEs com VIPER | Escavação e transporte de gelo |
| RASSORs | Robôs de escavação autônoma de regolito |
| Impressoras 3D de regolito | Construção de estruturas |
| Tanques de armazenamento | LOX (O₂ líquido), Metano, Água |

**Critério de prioridade de pouso:** Módulos de produção de recursos (ISRU) devem ter **alta prioridade** na fila do MGPEB, pois habilitam a sustentabilidade de toda a missão.

---

## 4. ESG aplicado à Base Aurora Siger

ESG (Environmental, Social and Governance) são critérios de governança que garantem responsabilidade ambiental, social e institucional. Em uma colônia em Marte, esses princípios são ainda mais críticos — não há como chamar ajuda externa.

### 4.1 Ambiental (Environmental)

**Proteção Planetária — COSPAR Policy**

O Comitê de Pesquisa Espacial (COSPAR) estabelece a política internacional de proteção planetária, baseada no Artigo IX do Tratado do Espaço Exterior da ONU (1967), que proíbe a contaminação prejudicial de outros corpos celestes.

Princípios para a Base Aurora Siger:

- **Escolha da área de pouso:** evitar regiões com potencial de vida microbiana (zonas úmidas, subsolo com gelo próximo à superfície)
- **Gestão de resíduos:** todo resíduo biológico ou químico deve ser processado e não liberado no ambiente marciano
- **Zero contaminação cruzada:** módulos não podem liberar microrganismos terrestres no ambiente aberto de Marte

**Gestão de energia sustentável:**

- Energia nuclear de fissão como fonte primária (baixo impacto ambiental local)
- Geração solar como suplemento
- Eficiência energética máxima em todos os sistemas (recursos escassos)

**Modelagem de geração de energia solar (Função Senoidal):**
```
E(t) = E_max × max(0, sin(π × t / L))
```
Onde:
- `E(t)` = energia gerada em kW no instante t
- `E_max` = capacidade máxima do painel solar
- `L` = duração do dia marciano (≈ 88.620 segundos)
- `t` = tempo desde o amanhecer

### 4.2 Social

- **Equidade no acesso a recursos:** o MGPEB deve garantir que módulos de suporte médico e habitação tenham prioridade sobre módulos de carga comercial
- **Saúde e bem-estar:** módulos médicos têm criticidade máxima e não podem ser bloqueados na fila por critérios econômicos
- **Comunicação transparente:** todas as decisões de pouso do MGPEB devem ser registradas em log auditável

### 4.3 Governança (Governance)

- **Decisões algorítmicas auditáveis:** o MGPEB deve registrar cada decisão de autorizar/bloquear um pouso, com o estado de cada variável no momento da decisão
- **Mecanismos de override humano:** em situações de emergência, um operador humano pode sobrepor a decisão automática
- **Separação de poderes:** nenhum módulo de carga privada pode bloquear módulos de suporte à vida

**Estrutura de governança sugerida para a fila do MGPEB:**

| Nível | Tipo de módulo | Prioridade |
|-------|---------------|------------|
| 1 — Crítico | Médico, suporte à vida | Máxima — não pode ser bloqueado |
| 2 — Essencial | Energia, ISRU, habitat | Alta |
| 3 — Operacional | Logística, laboratório | Média |
| 4 — Secundário | Carga comercial, equipamentos extras | Baixa |

---

## 5. Reflexão ESG — Perguntas para o relatório

1. Como o MGPEB garante que módulos de carga comercial nunca atrasem módulos médicos em situações de emergência?
2. De que forma a produção local de oxigênio e metano (ISRU) reduz a pegada ambiental da missão comparado ao transporte desde a Terra?
3. Que mecanismos de log e auditoria o sistema deve ter para garantir transparência nas decisões de pouso?
4. Como a gestão de resíduos da base pode ser estruturada para não contaminar o ambiente marciano?

---

## Fontes

- [NASA — Overview: In-Situ Resource Utilization](https://www.nasa.gov/overview-in-situ-resource-utilization/)
- [Mars Oxygen ISRU Experiment (MOXIE) — Wikipedia](https://en.wikipedia.org/wiki/Mars_Oxygen_ISRU_Experiment)
- [COSPAR Planetary Protection Policy](https://cosparhq.cnes.fr/assets/uploads/2020/07/PPPolicyJune-2020_Final_Web.pdf)
- [Planetary Protection in the New Space Era — Frontiers](https://www.frontiersin.org/journals/astronomy-and-space-sciences/articles/10.3389/fspas.2020.589817/full)
- [Towards earth-space governance in a multi-planetary era — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2589811623000101)
- Howard Jr., R. L. (2021). *Common Habitat Base Camp for Moon and Mars Surface Operations*. NASA Johnson Space Center.
