# Trabalho sobre Sistemas de Amortização de Empréstimos

**Aluno**: Mauricio Benjamin da Rocha

## 1. Introdução

Os sistemas de amortização são métodos utilizados para pagar um empréstimo ao longo do tempo. Os mais comuns são:

- **SAC (Sistema de Amortização Constante)**
- **Sistema Price (Parcelas Iguais com Juros)**

Cada um desses sistemas apresenta diferentes características em relação à forma como os juros e a amortização são calculados.

## 2. Funcionamento dos Diferentes Sistemas

### 2.1 SAC (Sistema de Amortização Constante)

No SAC, a amortização do capital é constante ao longo do tempo, enquanto os juros diminuem conforme a dívida é paga. Como resultado, as parcelas iniciais são mais altas e vão reduzindo ao longo do tempo.

**Fórmulas:**

- **Amortização**:

$$
A = \frac{P}{N}
$$

- **Juros**:

$$
J = S \times i
$$

- **Parcela**:

$$
P_n = A + J_n
$$

Onde:

- \( P \) = valor total do empréstimo
- \( N \) = número de parcelas
- \( S \) = saldo devedor
- \( i \) = taxa de juros por período

### 2.2 Sistema Price (Parcelas Iguais com Juros)

No Sistema Price, o valor das parcelas é fixo ao longo do tempo. Inicialmente, a maior parte da parcela corresponde aos juros, enquanto a amortização aumenta com o tempo.

**Fórmula da parcela fixa:**

$$P = \frac{P \times i}{1 - (1 + i)^{-N}}$$

Onde:

- \( P \) = valor total do empréstimo
- \( i \) = taxa de juros por período
- \( N \) = número de parcelas

## 3. Exemplos de Cálculo

### Exemplo 1: SAC

Considere um empréstimo de R$ 10.000,00 a uma taxa de juros de 1% ao mês, pago em 5 meses.

| Mês | Amortização (A) | Juros (J) | Parcela (P) | Saldo Devedor |
|------|----------------|------------|-------------|---------------|
| 1    | 2.000,00       | 100,00     | 2.100,00    | 8.000,00      |
| 2    | 2.000,00       | 80,00      | 2.080,00    | 6.000,00      |
| 3    | 2.000,00       | 60,00      | 2.060,00    | 4.000,00      |
| 4    | 2.000,00       | 40,00      | 2.040,00    | 2.000,00      |
| 5    | 2.000,00       | 20,00      | 2.020,00    | 0,00          |

Gráfico: Evolução das Parcelas no SAC

(Gráfico de barras comparando amortização, juros e parcela total)

---

### Exemplo 2: Sistema Price

Para o mesmo empréstimo de R$ 10.000,00 a 1% ao mês em 5 meses:

Cálculo da parcela fixa:

$$
P = \frac{10000 \times 0.01}{1 - (1 + 0.01)^{-5}} \approx 2.121,33
$$

| Mês | Juros (J) | Amortização (A) | Parcela (P) | Saldo Devedor |
|------|------------|----------------|-------------|---------------|
| 1    | 100,00     | 2.021,33       | 2.121,33    | 7.978,67      |
| 2    | 79,79      | 2.041,54       | 2.121,33    | 5.937,13      |
| 3    | 59,37      | 2.061,96       | 2.121,33    | 3.875,17      |
| 4    | 38,75      | 2.082,58       | 2.121,33    | 1.792,59      |
| 5    | 17,93      | 2.103,40       | 2.121,33    | 0,00          |

Gráfico: Evolução das Parcelas no Sistema Price

(Gráfico de linhas mostrando a redução dos juros e aumento da amortização ao longo do tempo)

## 4. Conclusão

- O **SAC** é vantajoso para quem deseja pagar menos juros no total, pois as parcelas diminuem ao longo do tempo.
- O **Sistema Price** é melhor para quem precisa de parcelas fixas e previsíveis.
- A escolha do sistema de amortização depende do perfil financeiro do tomador do empréstimo.

Ambos os sistemas têm aplicações práticas em financiamentos, hipotecas e créditos pessoais, sendo essenciais para o planejamento financeiro adequado.
