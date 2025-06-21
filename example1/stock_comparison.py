import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.dates as mdates
import numpy as np

# Set font for matplotlib
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def get_stock_data(symbol, years=5):
    """
    Fetch stock data for the specified symbol and time period.
    
    Args:
        symbol (str): Stock symbol (e.g., 'GOOGL', 'AMZN', 'ARM')
        years (int): Number of years of data to fetch (default: 5)
    
    Returns:
        pandas.DataFrame: Historical stock data
    """
    end_date = datetime.now()
    start_date = end_date - timedelta(days=years*365)
    
    stock = yf.Ticker(symbol)
    data = stock.history(start=start_date, end=end_date)
    return data

def normalize_to_start(data):
    """
    Normalize stock data to start at 100% for comparison.
    
    Args:
        data (pandas.DataFrame): Stock price data
    
    Returns:
        pandas.DataFrame: Normalized data with starting point at 100%
    """
    if len(data) == 0:
        return data
    first_price = data['Close'].iloc[0]
    normalized_data = data.copy()
    normalized_data['Close'] = (data['Close'] / first_price) * 100
    return normalized_data

def create_comparison_chart():
    """
    Create stock price comparison charts for Google, Amazon, and ARM.
    Generates three subplots: normalized comparison, actual prices, and ARM individual chart.
    """
    # Fetch stock data
    print("Fetching Google stock data...")
    googl_data = get_stock_data('GOOGL')
    print("Fetching Amazon stock data...")
    amzn_data = get_stock_data('AMZN')
    print("Fetching ARM stock data...")
    arm_data = get_stock_data('ARM')
    
    # Normalize data for comparison
    googl_normalized = normalize_to_start(googl_data)
    amzn_normalized = normalize_to_start(amzn_data)
    arm_normalized = normalize_to_start(arm_data)
    
    # Create figure with three subplots
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 15))
    
    # First subplot: Normalized comparison
    ax1.plot(googl_normalized.index, googl_normalized['Close'], 
             label='Google (GOOGL)', linewidth=2, color='#4285F4')
    ax1.plot(amzn_normalized.index, amzn_normalized['Close'], 
             label='Amazon (AMZN)', linewidth=2, color='#FF9900')
    ax1.plot(arm_normalized.index, arm_normalized['Close'], 
             label='ARM (ARM)', linewidth=2, color='#00B4D8')
    
    ax1.set_title('Google vs Amazon vs ARM: 5-Year Stock Price Comparison (Normalized)', fontsize=16, fontweight='bold')
    ax1.set_ylabel('Relative Price (%)', fontsize=12)
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=12)
    
    # Calculate Y-axis range
    max_values = [
        googl_normalized['Close'].max(),
        amzn_normalized['Close'].max(),
        arm_normalized['Close'].max()
    ]
    ax1.set_ylim(80, max(max_values) * 1.1)
    
    # Format x-axis dates
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax1.xaxis.set_major_locator(mdates.YearLocator())
    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)
    
    # Second subplot: Actual stock prices
    ax2.plot(googl_data.index, googl_data['Close'], 
             label='Google (GOOGL)', linewidth=2, color='#4285F4')
    ax2.plot(amzn_data.index, amzn_data['Close'], 
             label='Amazon (AMZN)', linewidth=2, color='#FF9900')
    ax2.plot(arm_data.index, arm_data['Close'], 
             label='ARM (ARM)', linewidth=2, color='#00B4D8')
    
    ax2.set_title('Google vs Amazon vs ARM: 5-Year Actual Stock Prices', fontsize=16, fontweight='bold')
    ax2.set_ylabel('Stock Price (USD)', fontsize=12)
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=12)
    
    # Format x-axis dates
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax2.xaxis.set_major_locator(mdates.YearLocator())
    plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)
    
    # Third subplot: ARM individual chart (shorter trading history)
    ax3.plot(arm_data.index, arm_data['Close'], 
             label='ARM (ARM)', linewidth=3, color='#00B4D8')
    
    ax3.set_title('ARM Stock Price Trend (Since IPO)', fontsize=16, fontweight='bold')
    ax3.set_ylabel('Stock Price (USD)', fontsize=12)
    ax3.set_xlabel('Date', fontsize=12)
    ax3.grid(True, alpha=0.3)
    ax3.legend(fontsize=12)
    
    # Format x-axis dates for ARM chart
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax3.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    plt.setp(ax3.xaxis.get_majorticklabels(), rotation=45)
    
    plt.tight_layout()
    
    # Save the chart
    plt.savefig('stock_comparison.png', dpi=300, bbox_inches='tight')
    print("Chart saved as 'stock_comparison.png'")
    
    # Display the chart
    plt.show()
    
    # Print statistics
    print("\n=== Statistics ===")
    print(f"Google starting price: ${googl_data['Close'].iloc[0]:.2f}")
    print(f"Google current price: ${googl_data['Close'].iloc[-1]:.2f}")
    print(f"Google total return: {((googl_data['Close'].iloc[-1] / googl_data['Close'].iloc[0]) - 1) * 100:.2f}%")
    
    print(f"\nAmazon starting price: ${amzn_data['Close'].iloc[0]:.2f}")
    print(f"Amazon current price: ${amzn_data['Close'].iloc[-1]:.2f}")
    print(f"Amazon total return: {((amzn_data['Close'].iloc[-1] / amzn_data['Close'].iloc[0]) - 1) * 100:.2f}%")
    
    print(f"\nARM starting price: ${arm_data['Close'].iloc[0]:.2f}")
    print(f"ARM current price: ${arm_data['Close'].iloc[-1]:.2f}")
    print(f"ARM total return: {((arm_data['Close'].iloc[-1] / arm_data['Close'].iloc[0]) - 1) * 100:.2f}%")
    
    # Calculate relative performance
    print(f"\n=== Relative Performance Comparison ===")
    googl_return = ((googl_data['Close'].iloc[-1] / googl_data['Close'].iloc[0]) - 1) * 100
    amzn_return = ((amzn_data['Close'].iloc[-1] / amzn_data['Close'].iloc[0]) - 1) * 100
    arm_return = ((arm_data['Close'].iloc[-1] / arm_data['Close'].iloc[0]) - 1) * 100
    
    print(f"Google vs Amazon: {googl_return - amzn_return:.2f}%")
    print(f"Google vs ARM: {googl_return - arm_return:.2f}%")
    print(f"Amazon vs ARM: {amzn_return - arm_return:.2f}%")

if __name__ == "__main__":
    try:
        create_comparison_chart()
    except Exception as e:
        print(f"Error occurred: {e}")
        print("Please ensure required libraries are installed: pip install yfinance matplotlib pandas") 