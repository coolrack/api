"""
Part B: Cryptocurrency Information Program
Student: devin l.

API Documentation: https://www.coingecko.com/en/api/documentation
CoinGecko API - Free cryptocurrency data API without authentication required

This program provides a menu-driven interface to explore cryptocurrency
information using the CoinGecko public API.
"""

import requests
import json


def get_crypto_price(crypto_name, currency='usd'):
    """
    Function 1: Get the current price of a specific cryptocurrency.
    Uses query parameters to specify the cryptocurrency and currency.
    
    Parameters:
        crypto_name: The ID of the cryptocurrency (e.g., 'bitcoin', 'ethereum')
        currency: The currency to display price in (default: 'usd')
    """
    # API endpoint with query parameters for cryptocurrency price
    api_url = f"https://api.coingecko.com/api/v3/simple/price"
    
    # Query parameters to customize the API request
    params = {
        'ids': crypto_name,
        'vs_currencies': currency,
        'include_24hr_change': 'true',
        'include_market_cap': 'true'
    }
    
    try:
        # Make API request with query parameters
        response = requests.get(api_url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            
            # Check if the cryptocurrency was found
            if crypto_name in data:
                crypto_data = data[crypto_name]
                price = crypto_data.get(currency, 'N/A')
                change_24h = crypto_data.get(f'{currency}_24h_change', 'N/A')
                market_cap = crypto_data.get(f'{currency}_market_cap', 'N/A')
                
                # Format and display the results
                print("\n" + "="*60)
                print(f"💰 {crypto_name.upper()} Price Information")
                print("="*60)
                print(f"Current Price: ${price:,.2f} {currency.upper()}" if isinstance(price, (int, float)) else f"Current Price: {price}")
                
                if isinstance(change_24h, (int, float)):
                    emoji = "📈" if change_24h >= 0 else "📉"
                    print(f"{emoji} 24h Change: {change_24h:.2f}%")
                
                if isinstance(market_cap, (int, float)):
                    print(f"💼 Market Cap: ${market_cap:,.0f} {currency.upper()}")
                
                print("="*60 + "\n")
            else:
                print(f"\n❌ Error: Cryptocurrency '{crypto_name}' not found.")
                print("Try using IDs like: bitcoin, ethereum, cardano, dogecoin\n")
        else:
            print(f"\n❌ Error: Unable to fetch data (Status code: {response.status_code})\n")
    
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Connection Error: {e}\n")


def get_trending_cryptos():
    """
    Function 2: Get the trending cryptocurrencies.
    This shows what cryptocurrencies are currently trending on CoinGecko.
    """
    # API endpoint for trending cryptocurrencies
    api_url = "https://api.coingecko.com/api/v3/search/trending"
    
    try:
        # Make API request without parameters
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            trending_coins = data['coins']
            
            # Display trending cryptocurrencies
            print("\n" + "="*60)
            print("🔥 Top Trending Cryptocurrencies")
            print("="*60)
            
            # Show top 7 trending coins with their ranking
            for i, coin_data in enumerate(trending_coins[:7], 1):
                coin = coin_data['item']
                name = coin['name']
                symbol = coin['symbol']
                rank = coin['market_cap_rank']
                
                print(f"{i}. {name} ({symbol.upper()}) - Market Cap Rank: #{rank if rank else 'N/A'}")
            
            print("="*60 + "\n")
        else:
            print(f"\n❌ Error: Unable to fetch trending data (Status code: {response.status_code})\n")
    
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Connection Error: {e}\n")


def search_cryptocurrency():
    """
    Function 3: Search for cryptocurrencies by name or symbol.
    Uses query parameters to filter search results.
    """
    # Get search query from user
    search_term = input("\nEnter cryptocurrency name or symbol to search: ").strip()
    
    if not search_term:
        print("❌ Please enter a valid search term.\n")
        return
    
    # API endpoint for searching cryptocurrencies
    api_url = "https://api.coingecko.com/api/v3/search"
    
    # Query parameter for search
    params = {'query': search_term}
    
    try:
        # Make API request with search query parameter
        response = requests.get(api_url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            coins = data['coins']
            
            print("\n" + "="*60)
            print(f"🔍 Search Results for '{search_term}'")
            print("="*60)
            
            if coins:
                # Display up to 10 search results
                for i, coin in enumerate(coins[:10], 1):
                    name = coin['name']
                    symbol = coin['symbol']
                    market_cap_rank = coin.get('market_cap_rank', 'N/A')
                    
                    print(f"{i}. {name} ({symbol.upper()}) - Rank: #{market_cap_rank if market_cap_rank else 'Unranked'}")
                
                if len(coins) > 10:
                    print(f"\n... and {len(coins) - 10} more results")
            else:
                print(f"No cryptocurrencies found matching '{search_term}'")
            
            print("="*60 + "\n")
        else:
            print(f"\n❌ Error: Unable to search (Status code: {response.status_code})\n")
    
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Connection Error: {e}\n")


def display_menu():
    """
    Displays the main menu with all available options.
    """
    print("\n" + "="*60)
    print("       🪙  CRYPTOCURRENCY INFORMATION SYSTEM  🪙")
    print("="*60)
    print("\nPlease select an option:")
    print("  [1] Get Current Price of a Cryptocurrency")
    print("  [2] View Trending Cryptocurrencies")
    print("  [3] Search for a Cryptocurrency")
    print("  [4] Exit Program")
    print("="*60)


def main():
    """
    Main function that runs the cryptocurrency information program.
    Displays menu and handles user choices.
    """
    print("\n" + "="*60)
    print("   Welcome to the Cryptocurrency Information Program!")
    print("="*60)
    print("\nThis program uses the CoinGecko API to provide real-time")
    print("cryptocurrency data, market trends, and search functionality.")
    
    # Main program loop
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            # Option 1: Get specific cryptocurrency price
            print("\n📊 Popular cryptocurrencies: bitcoin, ethereum, cardano, solana, dogecoin")
            crypto_name = input("Enter cryptocurrency ID: ").strip().lower()
            
            if crypto_name:
                # Ask if user wants a different currency (using query parameters)
                currency = input("Enter currency (usd, eur, gbp) [default: usd]: ").strip().lower()
                currency = currency if currency else 'usd'
                get_crypto_price(crypto_name, currency)
            else:
                print("❌ Please enter a valid cryptocurrency name.\n")
        
        elif choice == '2':
            # Option 2: View trending cryptocurrencies
            print("\n🔥 Fetching trending cryptocurrencies...")
            get_trending_cryptos()
        
        elif choice == '3':
            # Option 3: Search for cryptocurrencies
            search_cryptocurrency()
        
        elif choice == '4':
            # Option 4: Exit the program
            print("\n" + "="*60)
            print("   Thank you for using the Crypto Information System!")
            print("="*60 + "\n")
            break
        
        else:
            # Handle invalid menu choices
            print("\n❌ Invalid choice. Please enter a number between 1 and 4.\n")


# Entry point of the program
if __name__ == "__main__":
    main()
