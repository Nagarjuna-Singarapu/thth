import pandas as pd
import scipy.stats
x = [15,18,21, 15, 21]
y = [25,25,27,27,27]
def spearmans_rank_correlation(x, y):	
	xranks = pd.Series(x).rank()
	print("Rankings of X:")
	print(xranks)
	yranks = pd.Series(y).rank()
	print("Rankings of Y:")
	print(yranks)
	print("Spearman's Rank correlation:",scipy.stats.pearsonr(xranks, yranks)[0])
spearmans_rank_correlation(x, y)

