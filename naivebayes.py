from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
import numpy as np
import pandas as pd


data = pd.read_csv('german_credit_data.csv')

age = data[0]

Y = np.array([0,0,0,1,1,1])

model = MultinomialNB()
model.fit(X,Y)
lbl = model.predict([[110,85]])
print("Predicted label is ",lbl)

