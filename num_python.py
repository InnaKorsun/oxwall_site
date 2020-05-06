import numpy as np
a = np.array([1, 2, 3,4, 5, 6], float)
print(a)
b=a.reshape(2, 3)
print(b)
b.transpose()
print(b)
a = np.array([2, 1, 9], float)
print(a.mean())
print(a.var())
import pandas as pd
#df = pd.read_csv('../../data/telecom_churn.csv')
print("Hello world")