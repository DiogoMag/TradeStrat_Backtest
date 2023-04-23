import requests
import pandas as pd

apiKey= 'ACMVNCSoI3ogen2BGdapzXlsU8Or5g58'

url = "https://api.apilayer.com/currency_data/change?start_date={start_date}&end_date={end_date}"

payload = {}
headers= {
  "apikey": "ACMVNCSoI3ogen2BGdapzXlsU8Or5g58"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code

if status_code == 200:
    data = response.json()
    df = pd.DataFrame.from_dict(data['prices'])
    print(df)
else:
    print('API request failed with status code', status_code)
