from binance import Client
import os
import datetime

# Clear screen
os.system('cls')

# Get client Keys form system enviroment (Leave # at the beggining for the one you don't want to use)
#client = Client(os.environ.get('API_KEY'), os.environ.get('API_SKEY')) #General
client = Client(os.environ.get('TEST_API'), os.environ.get('TEST_SAPI'), testnet=True) #Testnet


# Display server time and status
def get_BIserver_status():
    server_status = client.get_system_status()
    server_status = server_status["msg"]

    return server_status

def get_BIserver_time():
    server_time = client.get_server_time()
    server_time = server_time["serverTime"]
    server_time = datetime.datetime.fromtimestamp(server_time/1000)
    server_time = server_time.replace(second=0, microsecond=0)
    server_time = server_time.strftime("%H:%M %d-%m-%Y")

    return server_time

print(get_BIserver_time())