import datetime
from binance import Client


# Display server time and status
server_status = Client.get_system_status()
server_status = server_status["msg"]
server_time = Client.get_server_time()
server_time = server_time["serverTime"]
server_time = datetime.datetime.fromtimestamp(server_time/1000)
server_time = server_time.replace(second=0, microsecond=0)
server_time = server_time.strftime("%H:%M %d-%m-%Y")
print("Server status is " + server_status)
print("Server Time is " + server_time)
print("")
print("")