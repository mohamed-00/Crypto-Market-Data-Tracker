import pandas as pd
import requests
from datetime import datetime
import os
from time import sleep

class CryptoData:
    def __init__(self, currency='usd', per_page=250):
        """Initialize the CryptoData class with API parameters."""
        self.api_url = 'https://api.coingecko.com/api/v3/coins/markets'
        self.currency = currency
        self.per_page = per_page
        self.data = None

    def fetch_data(self):
        """Fetch cryptocurrency data from CoinGecko API."""
        params = {
            'vs_currency': self.currency,
            'order': 'market_cap_desc',
            'per_page': self.per_page,
            'page': 1
        }
        response = requests.get(self.api_url, params=params)
        if response.status_code == 200:
            print('Connection successful')
            self.data = pd.DataFrame(response.json())
        else:
            print('Failed to fetch data')
            self.data = None

    def process_data(self):
        """Process and clean the fetched data."""
        if self.data is not None:
            self.data = self.data[['name', 'current_price', 'price_change_percentage_24h', 'market_cap_change_24h', 'ath', 'roi']]
            self.data[['Date','Time']] = [datetime.now().strftime('%Y-%m-%d'),datetime.now().strftime('%H:%M')]

    def get_top_movers(self):
        """Get the top 10 gainers and losers based on 24-hour price change."""
        if self.data is not None:
            high_top_10 = self.data.sort_values(by='price_change_percentage_24h', ascending=False).head(10)
            low_top_10 = self.data.sort_values(by='price_change_percentage_24h', ascending=True).head(10)
            return high_top_10, low_top_10
        return None, None

    def save_to_excel(self, file_path='Crypto.xlsx'):
        """Save the processed data to an Excel file, appending if the file already exists."""
        if self.data is not None:
            high_top_10, low_top_10 = self.get_top_movers()
            
            # Check if the file exists and read existing data
            if os.path.exists(file_path):
                existing_sheets = pd.ExcelFile(file_path)
                whole_data = pd.read_excel(file_path, sheet_name='Whole Data') if 'Whole Data' in existing_sheets.sheet_names else pd.DataFrame()
                high_top_data = pd.read_excel(file_path, sheet_name='High top ten') if 'High top ten' in existing_sheets.sheet_names else pd.DataFrame()
                low_top_data = pd.read_excel(file_path, sheet_name='Low top ten') if 'Low top ten' in existing_sheets.sheet_names else pd.DataFrame()
                
                # Append new data to the existing data
                print("Appending to existing file...")
                whole_data = pd.concat([whole_data, self.data], ignore_index=True)
                high_top_data = pd.concat([high_top_data, high_top_10], ignore_index=True)
                low_top_data = pd.concat([low_top_data, low_top_10], ignore_index=True)
            else:
                # If file does not exist, create new dataframes
                whole_data, high_top_data, low_top_data = self.data, high_top_10, low_top_10
            
            # Save data to Excel file
            with pd.ExcelWriter(file_path, mode='w', engine='openpyxl') as writer:
                whole_data.to_excel(writer, sheet_name='Whole Data', index=False)
                high_top_data.to_excel(writer, sheet_name='High top ten', index=False)
                low_top_data.to_excel(writer, sheet_name='Low top ten', index=False)
            print('Data saved successfully!')

# Example usage
# crypto = CryptoData()
# crypto.fetch_data()
# crypto.process_data()
# crypto.save_to_excel()