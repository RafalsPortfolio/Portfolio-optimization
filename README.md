# English description
Here is a portoflio optimalization.

Two sub-projects:
- Markowitz theory
- Shapre theory

## Markowitz theory vs. Sharpe theory
Investment portfolio management is based on two key theories: the Markowitz theory and the Sharpe theory. Although the two concepts are related, they differ in their assumptions, objectives and methodology.

### Markowitz theory
Markowitz theory, developed by Harry Markowitz in 1952, focuses on optimising a portfolio by balancing risk and return. Its key elements are:

**Objective**: Minimising risk for a given return or maximising return for a given level of risk.
**Risk**: Defined as the standard deviation of portfolio returns.
**Diversification**: The use of correlations between assets to reduce risk.
**Effective frontier**: The set of portfolios with the best risk-return ratio.
Markowitz theory assumes that investors are rational and risk averse.

#### Patterns in Markowitz theory
1. the expected rate of return of a portfolio

$E(Rp) = Σ(wi * E(Ri))$

Where:
E(Rp): The expected rate of return of the portfolio,
wi: Weight of asset i in the portfolio,
E(Ri): Expected rate of return of asset i,
n: The number of assets in the portfolio.

2. the risk (variance) of the portfolio
σp² = ΣΣ(wi * wj * σij)

Where:
σp²: The variance of the portfolio,
wi, wj: Weights of assets i and j,
σij: Covariance between assets i and j.

3. Effective frontier
The efficient frontier is the set of portfolios that maximise return at a given level of risk or minimise risk at a given level of return. The formula for the optimal asset weights for a portfolio:

W = (Σ-¹ * (R - Rf * 1)) / (1' * Σ-¹ * (R - Rf * 1))

Where:
W: Vector of optimal asset weights,
Σ-¹: Inverse covariance matrix of assets,
R: Vector of expected returns,
Rf: Rate of return of the risk-free asset,
1: Unit vector,
1': Transpose of unit vector.

4. the standard deviation of the portfolio
σp = √(σp²)

Where:
σp: Standard deviation of the portfolio,
σp²: The variance of the portfolio.

### Sharpe theory
Sharpe theory, developed by William Sharpe in 1964, is based on the Capital Asset Pricing Model (CAPM). The main assumptions are:

**Objective**: Maximise portfolio efficiency, i.e. risk premium relative to volatility.
**Systematic risk**: Focus on market risk that cannot be eliminated by diversification.
**Risk-free assets**: The introduction of a market portfolio and risk-free investments as a benchmark.
**Sharpe ratio**: A measure of portfolio efficiency:


Description of formulas in Sharpe theory.
The **Sharpe ratio**:
Measure of portfolio efficiency:

S = (Rp - Rf) / σp

Where:
- S - Sharpe ratio,
- Rp - rate of return of the portfolio,
- Rf - rate of return of the risk-free asset,
- σp - standard deviation of portfolio return (total risk).

** CAPM (Capital Asset Pricing Model)**:
Determines the expected rate of return of an asset based on systematic risk:

E(Ri) = Rf + βi * (E(Rm) - Rf)

Where:
- E(Ri) - expected rate of return of the asset,
- Rf - the risk-free rate of return of the asset,
- βi - beta coefficient of the asset (a measure of systematic risk),
- E(Rm) - expected rate of return of the market,
- (E(Rm) - Rf) - market risk premium.

### Main differences between Markowitz theory and Sharpe theory.
**Objective**:
*Markowitz:* Minimisation of risk or maximisation of return.
*Sharpe:* Maximising the ratio of risk premium to volatility (Sharpe ratio).

**Risk**:
*Markowitz:* Captures the total risk of the portfolio, measured by standard deviation.
*Sharpe:* Focuses on systematic risk (risk associated with the market as a whole).

**Diversification**:
*Markowitz:* Key element of risk reduction through correlation analysis between assets.
*Sharpe:* Assumes that unsystematic risk has already been eliminated through diversification.

**Reference point**:
*Markowitz:* Effective portfolio frontier, i.e. the set of portfolios with the best risk-return ratio.
*Sharpe:* Market portfolio (optimal portfolio) and risk-free asset.

**Tools**:
*Markowitz:* Analysis of the covariance matrix of asset returns.
*Sharpe:* Capital Asset Pricing Model (CAPM) and Sharpe ratio.

**Narzędzia**:
*Markowitz:* Analiza macierzy kowariancji stóp zwrotu aktywów.
*Sharpe:* Model CAPM (Capital Asset Pricing Model) i wskaźnik Sharpe’a.
