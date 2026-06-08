# 🚀 Monitoramento Inteligente de Missão Espacial
## Soluções em Energias Renováveis e Sustentáveis

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-green?style=for-the-badge)

## 📋 Descrição do Projeto
Este projeto consiste em uma solução computacional desenvolvida em **Python** para o monitoramento inteligente de sistemas energéticos e operacionais de uma missão espacial experimental. O sistema simula a telemetria de uma espaçonave, interpretando dados críticos e aplicando conceitos de sustentabilidade e eficiência energética para garantir a autonomia da operação.

A aplicação analisa em tempo real variáveis essenciais como temperatura, status de comunicação, integridade dos módulos operacionais e nível das baterias, executando tomadas de decisão automatizadas e gerenciamento de recursos diante de cenários críticos.

---

## 🛠️ Funcionalidades Implementadas

* **Monitoramento de Dados Simulados:** Captura e tratamento de dados cíclicos de telemetria (temperatura externa, estabilidade de sinal, nível de bateria e falhas em módulos).
* **Geração Automática de Alertas:** Identificação visual imediata de anomalias operacionais, como riscos de congelamento, superaquecimento ou falhas críticas de hardware.
* **Tomada de Decisão Básica:** Estruturas lógicas automatizadas que reagem às crises, acionando sistemas de suporte à vida ou ajustando a posição da nave para restabelecer comunicação.
* **Gerenciamento Sustentável de Energia:** Ativação automática de modos de contenção de gastos baseados na reserva energética disponível.

---

## 💡 Sustentabilidade e Energias Renováveis
O diferencial ecológico do software reside na sua **árvore de decisão de consumo**, que protege a matriz energética renovável da nave (baterias alimentadas via captação solar):

### 1. Gestão Eficiente da Potência
O sistema monitora continuamente o percentual de carga ativa (`dado_energia`). Sempre que o nível atinge um patamar crítico ($\le 25\%$), o **Modo Economia de Energia** é ativado, protegendo a vida útil das baterias contra descargas profundas.

### 2. Priorização e Racionamento
Em casos de temperaturas extremas ($\ge 150^\circ\text{C}$ ou $\le -150^\circ\text{C}$), o sistema valida se há saldo sustentável na bateria ($> 15\%$) antes de acionar os climatizadores.

### 3. Resiliência (Modo de Espera Passivo)
Caso a energia esteja severamente baixa ($\le 15\%$), o script suspende o controle ativo e entra em modo de espera para priorizar o **recarregamento fotovoltaico**, simulando o comportamento real de sondas espaciais.

---

## 🚀 Como Executar
1. Certifique-se de ter o Python instalado.
2. Clone o repositório:
   ```bash
   git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
