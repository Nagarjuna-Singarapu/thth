import pandas as pd
from scipy.stats import pearsonr
df = pd.read_scv("Auto.csv")
list1 = df['weight']
list2 = df['mpg']
corr, _ = pearsonr(list1, list2)
print('pearsons correlation: %.3f' % corr)