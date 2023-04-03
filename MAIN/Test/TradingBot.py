from binance import Client
import os
import pandas as pd
import pandas_ta as ta
import datetime

# Clear screen
os.system('cls')

# Get client Keys form system enviroment (Leave # at the beggining for the one you don't want to use)
#client = Client(os.environ.get('API_KEY'), os.environ.get('API_SKEY')) #General
client = Client(os.environ.get('TEST_API'), os.environ.get('TEST_SAPI'), testnet=True) #Testnet


# Display server time and status
server_status = client.get_system_status()
server_status = server_status["msg"]
server_time = client.get_server_time()
server_time = server_time["serverTime"]
server_time = datetime.datetime.fromtimestamp(server_time/1000)
server_time = server_time.replace(second=0, microsecond=0)
server_time = server_time.strftime("%H:%M %d-%m-%Y")
print("Server status is " + server_status)
print("Server Time is " + server_time)
print("")
print("")


#Account wallet
account_wallet = client.get_account()
account_wallet = pd.DataFrame(account_wallet['balances'], columns=['asset', 'free', 'locked'])
account_wallet.columns = ["Asset","Free","Locked"]
account_wallet[["Free","Locked"]] = account_wallet[["Free","Locked"]].astype(float)
account_wallet[['Free', 'Locked']] = account_wallet[['Free', 'Locked']].round(3)
pd.set_option('display.float_format', '{:.4f}'.format)

print(account_wallet)
print("")
print("")


os.system ('pause')

#print("Select your symbol/PAR:")
print("Select your symbol/PAR:")
symbol = input()
symbol = symbol.upper()

# Get historical klines data from Binance API
def klines (symbol):
    frame = pd.DataFrame(client.get_historical_klines(symbol,"1h", "1000 hours ago UTC"))
    frame = frame.iloc[:,:5]
    frame.columns = ["time", "open", "high", "low", "close"]
    frame[["open", "high", "low", "close"]] = frame[["open", "high", "low", "close"]].astype(float)
    frame['time'] = pd.to_datetime(frame['time'], unit='ms')
    frame['time'] = frame['time'].dt.strftime('%H:%M %d-%m-%Y')
    frame.set_index("time", inplace=True)

    return frame

df = klines(symbol)

rsi = ta.rsi(df["close"])
df["RSI"] = rsi

supertrend = pd.DataFrame (ta.supertrend(df["high"], df["low"], df["close"], length=5, multiplier=3))
df["Supertrend"] = supertrend["SUPERT_5_3.0"]
df["Direction"] = supertrend["SUPERTd_5_3.0"]
df["ST Long"] = supertrend["SUPERTl_5_3.0"]
df["ST Short"] = supertrend["SUPERTs_5_3.0"]

print(df)



            