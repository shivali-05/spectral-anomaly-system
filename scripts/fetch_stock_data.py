import yfinance as yf
from sqlalchemy import create_engine

from dotenv import load_dotenv
import os

load_dotenv()

password = os.getenv("MYSQL_PASSWORD")

engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost/spectral_db"
)

ticker = "AAPL"

data = yf.download(
    ticker,
    start="2023-01-01",
    end="2025-01-01"
)

data.reset_index(inplace=True)

data["ticker"] = ticker

data = data[
    ["ticker", "Date", "Open", "High", "Low", "Close", "Volume"]
]

data.columns = [
    "ticker",
    "date",
    "open",
    "high",
    "low",
    "close",
    "volume"
]

data.to_sql(
    "stock_prices",
    engine,
    if_exists="append",
    index=False
)

print(f"{len(data)} rows inserted.")