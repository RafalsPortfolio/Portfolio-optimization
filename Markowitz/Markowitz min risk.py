import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from datetime import datetime


# Funkcja do pobierania danych historycznych o cenach
def get_price_data(tickers, start_date, end_date):
    price_data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    return price_data


# Funkcja do obliczania średnich zwrotów i macierzy kowariancji
def calculate_returns(price_data):
    returns = price_data.pct_change().dropna()
    mean_returns = returns.mean() * 365
    cov_matrix = returns.cov() * 365
    return mean_returns, cov_matrix


# Funkcja celu do minimalizacji (ryzyko)
def portfolio_volatility(weights, mean_returns, cov_matrix):
    return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))


def neg_sharpe_ratio(weights, mean_returns, cov_matrix, risk_free_rate=0.04):
    portfolio_return = np.dot(weights, mean_returns)
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    return - (portfolio_return - risk_free_rate) / portfolio_volatility  # Maksymalizacja Sharpe -> minimalizujemy -Sharpe


# Funkcja do optymalizacji portfela
def optimize_portfolio(tickers, mean_returns, cov_matrix):
    num_assets = len(tickers)
    args = (mean_returns, cov_matrix)

    # Ograniczenia: suma wag = 1
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    # Ograniczenia: wagi >= 0
    bounds = tuple((0, 1) for asset in range(num_assets))

    # Inicjalizacja wag równych dla wszystkich aktywów
    initial_weights = num_assets * [1. / num_assets, ]

    # Optymalizacja
    # optimal = minimize(portfolio_volatility, initial_weights, args=args,
    #                    method='SLSQP', bounds=bounds, constraints=constraints)
    optimal = minimize(neg_sharpe_ratio, initial_weights, args=(mean_returns, cov_matrix, 0.04), method='SLSQP', bounds=bounds, constraints=constraints)

    return optimal

def plot_efficient_frontier(mean_returns, cov_matrix, optimal_weights):
    """
Rysuje efektywną granicę portfela Markowitza oraz oznacza optymalny portfel.

:param mean_returns: Średnie zwroty aktywów
:param cov_matrix: Macierz kowariancji zwrotów
:param optimal_weights: Wagi optymalnego portfela
    """
    num_portfolios = 10_000  # Liczba losowych portfeli do wygenerowania
    results = np.zeros((3, num_portfolios))  # Macierz przechowująca wyniki: [zwrot, ryzyko, Sharpe]

    num_assets = len(mean_returns)

    for i in range(num_portfolios):
        weights = np.random.dirichlet(np.ones(num_assets))  # Losowe wagi sumujące się do 1
        portfolio_return = np.dot(weights, mean_returns)  # Oczekiwany zwrot portfela
        portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))  # Ryzyko (odchylenie standardowe)
        sharpe_ratio = portfolio_return / portfolio_volatility  # Współczynnik Sharpe’a

        results[0, i] = portfolio_return
        results[1, i] = portfolio_volatility
        results[2, i] = sharpe_ratio

    # Optymalny portfel - na podstawie podanych wag
    optimal_return = np.dot(optimal_weights, mean_returns)
    optimal_volatility = np.sqrt(np.dot(optimal_weights.T, np.dot(cov_matrix, optimal_weights)))

    # Wykres
    plt.figure(figsize=(10, 6))
    plt.scatter(results[1, :], results[0, :], c=results[2, :], cmap='viridis', marker='o', alpha=0.3, label="Losowe portfele")
    plt.colorbar(label="Sharpe Ratio")
    plt.scatter(optimal_volatility, optimal_return, color='red', marker='*', s=300, label='Optymalny portfel')

    plt.xlabel("Ryzyko (Zmienność)")
    plt.ylabel("Oczekiwany zwrot")
    plt.title("Efektywna granica portfela Markowitza")
    plt.legend()
    plt.grid()
    plt.show()


# Główna funkcja
def main():
    # tickers = ['SOL-USD', 'SUI20947-USD', 'TAO22974-USD', 'RUNE-USD', 'AAVE-USD', 'PEPE24478-USD', 'FET-USD', 'WIF-USD', 'BONK-USD', 'PENDLE-USD', 'KAS-USD']  # Wprowadź swoje tickery
    # tickers = ['OM-USD',
    #            'CPOOL-USD',
    #            'RIO-USD',
    #            'ONDO-USD']
    # tickers = ['BTC-USD',
    #            'ORDI-USD',
    #            '1000SATS-USD',
    #            'SOV-USD',
    #            'SAVM-USD',
    #            'TRAC25208-USD',
    #            'DOG30933-USD',
    #            'ORNJ-USD',
    #            'RATS28452-USD',
    #            'ORDS-USD']
    tickers = ['ACX22620-USD',
               'BANANA28066-USD',
               'GIGA30063-USD',
               # 'PAAL-USD',
               'SPX28081-USD',
               'COOKIE31838-USD',
               'HYPE32196-USD',
               'VIRTUAL-USD',
               'AIXBT-USD',
               'DOG30933-USD',
               'ENA-USD', # Stable coin and luqidity for Exchanges
               'KAS-USD',  # l1
               'AEVO-USD',
               'USUAL-USD',
               'SUI20947-USD',  # L1
               'TAO22974-USD',  # AI Agents infra
               'AAVE-USD',  # DeFi blue chip
               'PEPE24478-USD',  # Meme
               # 'FET-USD',  # AI Agents infra
               # 'WIF-USD',  # Meme
               'BONK-USD',  # Meme
               'PENDLE-USD',  # Defi 3.0
               # 'BTC-USD',
               'SOL-USD',
               'ONDO-USD',
               # 'ETH-USD',
               'OM-USD',
               'CPOOL-USD',
               # 'RIO-USD',
               'TON11419-USD',
               # 'PAXG-USD'
               'TRX-USD',
               'XRP-USD'
               ]
    tickers.sort()

    start_date = '2024-11-12'
    end_date = datetime.now().strftime('%Y-%m-%d')

    # Pobieranie danych
    price_data = get_price_data(tickers, start_date, end_date)

    # Obliczanie średnich zwrotów i macierzy kowariancji
    mean_returns, cov_matrix = calculate_returns(price_data)

    # Optymalizacja portfela
    optimal = optimize_portfolio(tickers, mean_returns, cov_matrix)

    # Wyświetlenie wyników
    print("Optymalne wagi portfela:")
    for i, ticker in enumerate(tickers):
        print(f"{ticker}: {optimal.x[i]:.4f}")

    # Obliczanie ryzyka i zwrotu
    optimal_return = np.dot(optimal.x, mean_returns)
    optimal_volatility = portfolio_volatility(optimal.x, mean_returns, cov_matrix)

    print(f"\nOczekiwany zwrot: {optimal_return:.4f}")
    print(f"Ryzyko (zmienność): {optimal_volatility:.4f}")

    # Wykres ryzyko-zwrot
    plt.scatter(optimal_volatility, optimal_return, color='red', marker='o', s=200)
    plt.title('Optymalizacja portfela')
    plt.xlabel('Ryzyko (zmienność)')
    plt.ylabel('Oczekiwany zwrot')
    plt.grid()
    plt.show()
    optimal_weights = optimal.x
    plot_efficient_frontier(mean_returns, cov_matrix, optimal_weights)


if __name__ == "__main__":
    main()
