# Google vs Amazon vs ARM Stock Price Comparison

This Python script generates stock price comparison charts for Google (GOOGL), Amazon (AMZN), and ARM (ARM) over the past five years, with all stocks normalized to start at 100% for easy relative performance comparison.

## Features

- 📈 Fetch 5-year stock price data
- 🔄 Normalize starting points to 100% for relative comparison
- 📊 Generate three charts: normalized comparison, actual prices, and ARM individual trend
- 📱 Support for chart display
- 💾 Auto-save high-quality PNG images
- 📋 Display detailed statistics and relative performance comparison

## Installation

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install yfinance matplotlib pandas numpy
```

## Usage

```bash
python stock_comparison.py
```

## Output

The script generates:
1. A chart with three subplots:
   - Top: Normalized stock price comparison (relative price %)
   - Middle: Actual stock price comparison (USD)
   - Bottom: ARM individual stock price trend (since IPO)
2. Saved as `stock_comparison.png` file
3. Console output with statistics (starting price, current price, total return, relative performance comparison)

## Chart Legend

- **Blue line**: Google (GOOGL)
- **Orange line**: Amazon (AMZN)
- **Cyan line**: ARM (ARM)
- Normalized chart shows relative performance for easy investment return comparison
- Actual price chart shows absolute price changes
- ARM individual chart shows detailed trend since its IPO

## Notes

- Requires internet connection to fetch real-time stock data
- Data source: Yahoo Finance
- Charts use company brand colors (Google blue, Amazon orange, ARM cyan)
- ARM went public in September 2023, data starts from IPO date 