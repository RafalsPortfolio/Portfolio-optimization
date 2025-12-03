import requests

url = "https://query1.finance.yahoo.com/v8/finance/chart/AAPL?range=1d&interval=1d"
response = requests.get(url)

print("Status code:", response.status_code)
print("Response text:", response.text[:500])  # Wyświetl pierwsze 500 znaków odpowiedzi
