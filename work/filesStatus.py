import os
import datetime

files = {}
files ['kcell'] = r'\\kcell.kz\DFS\Workfiles\B2C\BI B2C\Management Reporting Team\Revenue Forecast And TPs KPIs\b2c_kcell_daily\KCELL_DAILY_REVENUE.xlsx'
files ['activ'] = r'\\kcell.kz\DFS\Workfiles\B2C\BI B2C\Management Reporting Team\Revenue Forecast And TPs KPIs\ACTIV_2011-2014_REVENUE_and_FORECAST 2\ACTIV_2011-2019_REVENUE_and_FORECAST.xlsm'
files ['phone'] = r'\\Kcell.kz\dfs\Protected\B2C_Protected\Business intelligence\Analysis_&_Reporting\Daily reports\Phone Sales\Pivot Tables\Sales\Phone Sales and Stocks 2019_2020.xlsm'
files ['Sales&Face'] = r'\\kcell.kz\dfs\Workfiles\B2C\SC B2C\Merchants Report\new_reports\ShareBI\Sales&Facing.xlsx'

os.system('cls')
print('-' * 50)
print('Last date/time of file modification\n')
for i in files:
    try:
        dateChange = datetime.datetime.fromtimestamp(int(os.path.getmtime(files[i])))
        print('{0:50} {1}'.format(os.path.basename(files[i]), dateChange))
    except FileNotFoundError as err:
        print('\n{0}\n'.format(err))
        