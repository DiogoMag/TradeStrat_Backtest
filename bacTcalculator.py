import os
import seaborn as sns
import pandas as pd

os.system('cls')

## Create data frame to save results for plotting
df = pd.DataFrame({'Trades': [], 'Capital': [], 'Profit': []})


print('what is your starting capital')
capital = int(input())

print('what is your risk %')
risk = int(input())

entry = capital * (risk/100)

print(f'Initial entry will be of £{entry}')
print()
LostTrades = 0
wonTrades = 0
winRate = None

print('Press any key to continue.')
input()

while True:
    print('____________________________________________')
    print('Current balance - ' + str(capital))
    if LostTrades == 0 and wonTrades > 0:
        winRate = 100
    elif LostTrades > 0 and wonTrades == 0:
        winRate = 0
    elif LostTrades > 0 and wonTrades > 0:
        winRate = (round(float(wonTrades),1) / round((float(LostTrades)+float(wonTrades)),1)) * 100
    print()
    print('    ____________________________________    ')
    print()
    print('          --- WIN RATE = ' + str(winRate) + '% --')
    print('WINS - ' + str(wonTrades) + '                       ' + 'LOSSES - ' + str(LostTrades))
    print('____________________________________________')
    print()
    print('w / l ?')
    outcome = str(input())
    if outcome == 'w':
        print()
        print('% ?')
        Wcent = (float(input()) / 100 )

        entry = entry  * Wcent
        entry = round(entry, 1)

        capital = capital + entry
        capital = round(capital, 1)

        entry = capital * (risk/100)
        print()
        print('balance after trade - ' + str(capital))
        print()
        
        ## Counters
        wonTrades += 1

    elif outcome == 'l':
        print()
        print('% ?')
        Lcent = (float(input()) / 100 )

        entry = entry  * Lcent
        entry = round(entry, 1)

        capital = capital - entry
        capital = round(capital, 1)

        entry = capital * (risk/100)
        print()
        print('balance after trade - ' + str(capital))
        print()
        
        ## Counters
        LostTrades += 1








