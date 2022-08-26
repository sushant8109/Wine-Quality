import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier,ExtraTreesClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import pickle

## loading the dataset
df = pd.read_csv("winequality-red.csv")


X = df.drop("quality",axis=1)
Y = df['quality']

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,stratify=df.quality,random_state=42)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


model = RandomForestClassifier(n_estimators=200)
model.fit(X_train,Y_train)
y_pred = model.predict(X_test)
print(accuracy_score(y_pred,Y_test))

pickle.dump(model,open('model.pkl','wb'))
print("########## Model Saved Successfully ###############")
