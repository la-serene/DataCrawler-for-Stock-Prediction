import yfinance as yf

def collect_financial_data(start_date, end_date):
    # Define the tickers for the required indices
    tickers = {
        "Nasdaq": "^IXIC",
        "Dow Jones": "^DJI",
        "Dollar Index": "DX-Y.NYB",
        "US 30": "^DJI",  # Dow Jones Industrial Average
        "US 500": "^GSPC"  # S&P 500
    }

    # Fetch sample_data for each ticker
    data = {}
    for name, ticker in tickers.items():
        stock = yf.Ticker(ticker)
        hist = stock.history(start=start_date, end=end_date)
        if not hist.empty:
            data[name] = hist

    return data


def save_to_csv(data):
    for index, df in data.items():
        filename = f"sample_data/{index.replace(' ', '_').lower()}_data.csv"
        df.to_csv(filename)
        print(f"Saved {index} sample_data to {filename}")


if __name__ == "__main__":
    start_date = input("Enter start date (yy-mm-dd):")
    if start_date == "\n":
        start_date = "2020-01-01"

    end_date = input("Enter end date (yy-mm-dd): ")
    if end_date == "\n":
        end_date = "2024-12-31"

    data = collect_financial_data(start_date, end_date)
    save_to_csv(data)
    print("Data collection complete.")
