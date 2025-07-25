# 📈 MINI STOCK PRICE TRACKER using Python .This program fetches the stock prices in last 30 days for a given ticker. 

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import time
import os

# Welcome message

print("-" * 50)
print("Welcome to the Mini Stock Price Tracker!")
print("Track the live performance of any stock over the last 30 days.")
print()

# Ask user for stock symbol
ticker = input(" Please enter a stock ticker symbol (e.g., TCS.NS, AAPL): ").upper().strip()

#stock data function
def stock_data(ticker):
    print("\n Fetching stock data, please wait...")
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1mo")  # fetching data for last 30 days
        
        if hist.empty:
            print(" No data found for this ticker. Please check and try again.")
            return None
        return hist
    except Exception as e:
        print(" Error occurred while fetching data:", e)
        return None

#  Display current stock price

def show_current_price(hist, ticker):
    latest_price = hist['Close'][-1]
    print(f"\nThe current closing price of {ticker} is {latest_price:.2f} Rs.")

# plotting the graph
def plot_stock_graph(hist, ticker):
    print("Generating price chart...")
    plt.figure(figsize=(12, 6))
    plt.plot(hist.index, hist['Close'], label='Closing Price', color='blue', linewidth=2, marker='o')
    plt.title(f"{ticker} - Stock Price (Last 30 Days)", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Price (₹)", fontsize=12)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Save data to CSV
def save_to_csv(hist, ticker):
    filename = f"{ticker}_30days_data.csv"
    hist.to_csv(filename)
    print(f"Data saved successfully to: {filename}")

# Run the program
data = stock_data(ticker)

if data is not None:
    time.sleep(1)
    show_current_price(data, ticker)

    time.sleep(1)
    plot_stock_graph(data, ticker)

    # Ask user if they want to save data
    choice = input("\nDo you want to save this data to a CSV file? (y/n): ").lower().strip()
    if choice == 'y':
        save_to_csv(data, ticker)
    else:
        print("Alright, data not saved.")

else:
    print("Ticker not found or data unavailable. Please try again with a valid ticker.")

print("\n Thank you for using the Mini Stock Price Tracker! Have a great day!")
