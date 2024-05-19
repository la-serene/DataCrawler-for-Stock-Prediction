from vnstock3 import *
import os


if "ACCEPT_TC" not in os.environ:
    os.environ["ACCEPT_TC"] = "tôi đồng ý"

stock = Vnstock().stock(symbol='MBS', source='VCI')
print(stock.quote.history(start='2023-01-01', end='2024-01-31', interval='1D'))
