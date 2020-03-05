import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

data = pd.read_csv('pulsar_stars.csv')
#print(data)
data2 = pd.DataFrame(data,columns=data.columns[:-1])
#print(data2.columns)
X_train, X_test, y_train, y_test = train_test_split(data2, data['target_class'], test_size=0.3)
knn = KNeighborsClassifier(n_neighbors=15)
knn.fit(X_train, y_train)
pred = knn.predict(X_test)

print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))

#error_rate = []
#for i in range(1,40):
#    knn = KNeighborsClassifier(n_neighbors=i)
#    knn.fit(X_train, y_train)
#    pred_i = knn.predict(X_test) 
#    error_rate.append(np.mean(pred_i != y_test))

#plt.plot(range(1,40), error_rate, marker='o')
#plt.xlabel('K')
#plt.ylabel('Error Rate')
#plt.show
#input("Press Enter to continue...")