import { helper } from './helpers.js';

helper();

async function getStockPrice(symbol) {
    /**
     * Get the current stock price for a given symbol using Yahoo Finance API.
     * 
     * @param {string} symbol - Stock symbol (e.g., 'AAPL' for Apple)
     * @returns {number|null} Current stock price
     */
    try {
        // Convert symbol to uppercase and create URL
        symbol = symbol.toUpperCase();
        const url = `https://query1.finance.yahoo.com/v8/finance/chart/${symbol}`;
        
        // Create headers to mimic browser request
        const headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        };
        
        // Fetch data from URL
        const response = await fetch(url, { headers });
        
        if (!response.ok) {
            if (response.status === 404) {
                console.log(`Error: Symbol '${symbol}' not found`);
            } else {
                console.log(`HTTP Error: ${response.status} - ${response.statusText}`);
            }
            return null;
        }
        
        const data = await response.json();
        
        // Extract current price from response
        const price = data.chart.result[0].meta.regularMarketPrice;
        return price;
        
    } catch (e) {
        console.log(`Error fetching stock price: ${e.message}`);
        return null;
    }
}

function main() {
    const args = process.argv.slice(2);
    
    if (args.length !== 1) {
        console.log("Usage: node stock_price.js <stock_symbol>");
        console.log("Example: node stock_price.js AAPL");
        process.exit(1);
    }
    
    const symbol = args[0];
    getStockPrice(symbol).then(price => {
        if (price !== null) {
            console.log(`Current price of ${symbol}: $${price.toLocaleString('en-US', {
                minimumFractionDigits: 2,
                maximumFractionDigits: 2
            })}`);
        }
    });
}

main();