import numpy as np
import pandas as pd


def long_line():
    print('-------------------')


a0 = np.zeros((3, 2))
print(a0)
long_line()

a = pd.read_csv('closeprice.csv', encoding='GBK')
b = {1: '银行', 2: '房地产', 4: '医药生物', 5: '房地产', 6: '采掘', 7: '休闲服务', 8: '机械设备'}
a['ind'] = a.ticker.map(b)
print(a)
long_line()

data = pd.DataFrame({'group': ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'], 'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
data.sort_values(by=['group', 'ounces'], ascending=[False, True], inplace=True)
print(data)
long_line()

data = pd.DataFrame({'k1': ['one'] * 3 + ['two'] * 4, 'k2': [3, 2, 1, 3, 3, 4, 4]})
print(data)
long_line()

print(data.drop_duplicates())
long_line()

print(data.drop_duplicates(subset=['k1'], keep='last'))
long_line()
