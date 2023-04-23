from binance import Client
import pandas as pd
import os

##__________ This script contains the following functions: __________

#       - getAcc_balance()
#               1 parameter, Example: 'all' / 'BTC' / 'ETH' etc

#       - get_openOrders()
#               1 parameter Example: 'all' / 'BTC' / 'ETH' etc

#       - get_allOrders() - gets open, closed and canceled orders
#                no parameters

#       - getAccount_balance

## Clear screen
os.system('cls')

## Connect to binance client
test_api_key = os.environ.get('TEST_API')
test_api_secret = os.environ.get('TEST_SAPI')
client = Client(test_api_key, test_api_secret, testnet=True)

#       - getAccount_balance() - parameter Example: 'all' or 'BTC'
def getAcc_balance(symbol):
    if symbol == 'all':
        account_wallet = client.get_account()
        account_wallet = pd.DataFrame(account_wallet['balances'], columns=['asset', 'free', 'locked'])
        account_wallet.columns = ["Asset","Free","Locked"]
        account_wallet[["Free","Locked"]] = account_wallet[["Free","Locked"]].astype(float)
        account_wallet[['Free', 'Locked']] = account_wallet[['Free', 'Locked']].round(4)
        pd.set_option('display.float_format', '{:.4f}'.format)

        return account_wallet

    else:
        account_wallet = getAcc_balance('all')
        if symbol in account_wallet['Asset'].values:
            balance = client.get_asset_balance(asset=symbol)

            return balance
        else:
            print('--')
            print('You do not hold such asset.')
            print('--')
            print()

            return None




## test function
print('___')
print(getAcc_balance('CACA'))
print('___')
print(getAcc_balance('ETH'))
print('___')
print(getAcc_balance('all'))