import os
import seaborn as sns
import pandas as pd
import matplotlib as plt

os.system('cls')

## Create data frame to save results for plotting
df = pd.DataFrame({'Trades': [], 'Capital': []})

## ______________________________________________________________________________________________ DEFINE FUNCTIONS

## add row to dataframe function
def append_todf(tradesX, capitalX):

    global df
    
    # Create a new row as a dictionary
    new_row = {'Trades': tradesX, 'Capital': capitalX}

    # Append the new row to the DataFrame with ignore_index=True
    df = df.append(new_row, ignore_index=True)

    # Print the updated DataFrame
    print(df)

## show graph function
def plot_outcome():   
    sns.lineplot(data=df)

## _______________________________________________________________________________________________________________

## CAPITAL
print("what's your starting capital ?")
capital = int(input())
print()

## RISK
print("what's your risk % ?")
risk = int(input())
print()

## ENTRY
entry = capital * (risk/100)        
entry = round(entry, 2)

print(f'Initial entry will be of £{entry}')
print()
lostTrades = 0
wonTrades = 0
winRate = None

## PnL
PnL = float()

print('Press any key to continue.')
print()
input()

while True:
    print('____________________________________________')
    print()
    print(f'                           {lostTrades + wonTrades} Trades taken')
    print(f'Previous P&L >   {round(PnL,2)} $')
    print()
    print(f'Balance >   {round(capital,2)} $')
    print(f'Next entry >   {round(entry,2)} $')

    if lostTrades == 0 and wonTrades > 0:
        winRate = 100
    elif lostTrades > 0 and wonTrades == 0:
        winRate = 0
    elif lostTrades > 0 and wonTrades > 0:
        winRate = (round(float(wonTrades),1) / round((float(lostTrades)+float(wonTrades)),1)) * 100
    print()
    print('    ____________________________________    ')
    print()
    print('          --- WIN RATE = ' + str(winRate) + '% --')
    print('WINS - ' + str(wonTrades) + '                        ' + 'LOSSES - ' + str(lostTrades))
    print('____________________________________________')
    print()
    print('w / l ?')
    outcome = str(input())
    if outcome == 'w':
        print()
        print('% ?')
        Wcent = (float(input()) / 100 )

        iniCapital= capital

        entry = entry  * Wcent

        capital = capital + entry

        entry = capital * (risk/100)

        
        ## Update values

        # Counters
        wonTrades += 1

        # PnL
        PnL = capital - iniCapital



    elif outcome == 'l':
        print()
        print('% ?')
        Lcent = (float(input()) / 100 )

        iniCapital= capital

        entry = entry  * Lcent

        capital = capital - entry

        entry = capital * (risk/100)
        
        ## Counters
        lostTrades += 1

        # PnL
        PnL = capital - iniCapital

    else:
        plot_outcome()









