import os
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

os.system('cls')

## Create data frame to save results for plotting
df = pd.DataFrame({'Trades': [], 'Capital': []})

## ______________________________________________________________________________________________ DEFINE FUNCTIONS

## add row to dataframe function
def append_todf(tradesX, capitalX):

    global df

    df.loc[len(df)] = {'Trades': tradesX, 'Capital': capitalX}

## show graph function sns
def plot_outcome():   
    sns.lineplot(x='Trades', y='Capital', data=df)
    plt.show()

def plot_outcome():
    plt.plot(df['Trades'], df['Capital'])
    plt.xlabel('Trades')
    plt.ylabel('Capital')
    plt.show()

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

print(f'Initial entry  -->  £{entry}')
print()
lostTrades = 0
wonTrades = 0
winRate = int()

## PnL
PnL = float()

print("Press any 'ENTER' to START.")
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
    print(f'          --- WIN RATE = {int(winRate)}% --')
    print('WINS - ' + str(wonTrades) + '                        ' + 'LOSSES - ' + str(lostTrades))
    print('____________________________________________')
    print()
    print('ACTION  -  w / l / plot / tbl / save ?')
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
        trades = wonTrades + lostTrades

        # PnL
        PnL = capital - iniCapital

        append_todf(trades, capital)



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
        trades = wonTrades + lostTrades


        # PnL
        PnL = capital - iniCapital

        append_todf(trades, capital)


    elif outcome == 'plot':
        plot_outcome()

    elif outcome == 'tbl':
        print(df)

    else:
        print('XXXXXXXXXXXXXXXXXXXXXxxxxxxxxxx   wrong entry   xxxxxxxxxxXXXXXXXXXXXXXXXXXXXXX')









