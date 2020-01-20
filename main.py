import pandas as pd
import matplotlib.pyplot as plt

"""
requires a csv with money and date columns

What do we want to know?
biggest stock movement day
what does my money movement look like without paychecks
what is just growth per day without "paycheck growth" in dollars
what is just growth per day without "paycheck growth" in percents
must take into account days where we lose in the stock market enough to offset the 4000 dollar paycheck addition

do percent diffs
ignore diffs depending on days which were pay check daysG
"""

if __name__ == '__main__':
    moneyData  = pd.read_csv("personalValue.csv")
    moneyData  = moneyData.iloc[::-1]
    moneyData = moneyData.reset_index()
    moneyData = pd.DataFrame({ 'money': moneyData['money'], 'date': moneyData['date'] })


"""
gets percent change compared to yesterday for today
filters percent change by days that are not paycheck days
"""
def growthNonPaycheck():
    moneyDiffs = moneyData['money'].rolling(2).apply(lambda r: (r[1]-r[0])/r[0])
    isNotPaycheckDay = moneyData['money'].rolling(2).apply(lambda r: (r[1] - r[0]) < 3000) == 1.0
    moneyGrowth = moneyData['money'][isNotPaycheckDay].rolling(37).apply(lambda r: (r[36] - r[0])/r[0])
    diffs = pd.DataFrame({
        'moneyGrowth': moneyGrowth,
        'date': moneyData['date'][isNotPaycheckDay],
        'growth': moneyDiffs[isNotPaycheckDay]
        })
    plt.plot('date', 'moneyGrowth', data=diffs, color='black')
    plt.plot('date', 'growth', data=diffs, color='blue')
    plt.legend()
    plt.show()
