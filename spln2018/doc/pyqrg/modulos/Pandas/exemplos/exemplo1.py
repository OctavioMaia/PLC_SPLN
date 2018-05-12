#!/usr/bin/python3
"""
criar um dataframe
spln2018
"""

import pandas as pd

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]} #criar o objeto
df = pd.DataFrame(data) #criar o dataframe

print(df)

"""
   Age   Name
0   28    Tom
1   34   Jack
2   29  Steve
3   42  Ricky
"""
