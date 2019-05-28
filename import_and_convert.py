import numpy as np
import pandas as pd

# load data from csv
housing = pd.read_excel('analysis.xlsx')

# convert to numpy

housing = np.array(housing)

print(housing)