import numpy as np
import pandas as pd

# load knn and naive bayes from csv
housing = pd.read_excel('analysis.xlsx')

# convert to numpy

housing = np.array(housing)

print(housing)