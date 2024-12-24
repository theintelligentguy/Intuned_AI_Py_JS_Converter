import urllib.request
import json
import sys
from helpers import helper

helper()

def get_stock_price(symbol: str) -> float:
    """
    Get the current stock price for a given symbol using Yahoo Finance API.
    
    Args:
        symbol (str): Stock symbol (e.g., 'AAPL' for Apple)
    
    Returns:
        float: Current stock price
    """
    try:
        # Convert symbol to uppercase and create URL
        symbol = symbol.upper()
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
        
        # Create headers to mimic browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        # Create request with headers
        req = urllib.request.Request(url, headers=headers)
        
        # Open URL and read response
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read())
            
        # Extract current price from response
        price = data['chart']['result'][0]['meta']['regularMarketPrice']
        return price
        
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error: Symbol '{symbol}' not found")
        else:
            print(f"HTTP Error: {e.code} - {e.reason}")
        return None
    except Exception as e:
        print(f"Error fetching stock price: {str(e)}")
        return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python stock_price.py <stock_symbol>")
        print("Example: python stock_price.py AAPL")
        sys.exit(1)
        
    symbol = sys.argv[1]
    price = get_stock_price(symbol)
    
    if price is not None:
        print(f"Current price of {symbol}: ${price:,.2f}")

main()