from binance import Client
import pandas as pd
import os


## Clear screen
os.system('cls')

## Connect to binance client
test_api_key = os.environ.get('TEST_API')
test_api_secret = os.environ.get('TEST_SAPI')
client = Client(test_api_key, test_api_secret, testnet=True)


def getAccount_balance(symbol):
    if symbol == 'all':
        #Account wallet
        account_wallet = client.get_account()
        account_wallet = pd.DataFrame(account_wallet['balances'], columns=['asset', 'free', 'locked'])
        account_wallet.columns = ["Asset","Free","Locked"]
        account_wallet[["Free","Locked"]] = account_wallet[["Free","Locked"]].astype(float)
        account_wallet[['Free', 'Locked']] = account_wallet[['Free', 'Locked']].round(4)
        pd.set_option('display.float_format', '{:.4f}'.format)

        return account_wallet

    else:
        account_wallet = getAccount_balance('all') # Get account wallet
        if symbol in account_wallet['Asset'].values:
            # Get balance for the specified asset
            balance = client.get_asset_balance(asset=symbol)
            balanceFree = balance['free']
            balanceLocked = balance['locked']

            return balance
        else:
            print('--')
            print('You do not hold such asset.')
            print('--')
            print()




## test function
print(getAccount_balance('CACA'))
print(getAccount_balance('all'))