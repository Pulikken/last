import requests
import time
from tkinter import Tk, Label

# Define your API key and the symbols of the stocks you want to track
API_KEY = "your_api_key"
symbols = ["TSLA", "MSFT", "IBM"]

# Create the Tkinter window
window = Tk()
window.configure(bg='green')

# Create the heading label
heading = Label(window, text="Mathew Kay", font=("Arial", 24), bg="green", fg="white")
heading.pack(pady=20)

# Create the labels for displaying stock prices
stock_labels = []
for symbol in symbols:
    stock_label = Label(window, text=f"{symbol}: ", font=("Arial", 18), bg="green", fg="white")
    stock_label.pack()
    stock_labels.append(stock_label)

# Function to update stock prices
def update_stock_prices():
    for i, symbol in enumerate(symbols):
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
        response = requests.get(url)
        data = response.json()

        # Extract the share price from the response
        share_price = data["Global Quote"]["05. price"]
        
        # Update the stock price labels
        stock_labels[i].config(text=f"{symbol}: {share_price}")

# Function to update stock prices every minute
def update_loop():
    update_stock_prices()
    window.after(60000, update_loop)

# Start the update loop
update_loop()

# Run the Tkinter event loop
window.mainloop()
