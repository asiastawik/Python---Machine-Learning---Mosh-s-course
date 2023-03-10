import pandas as pd

from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score

import joblib

from sklearn import tree

 

#model training

music_data = pd.read_csv('music.csv')

X = music_data.drop(columns=['genre'])

y = music_data['genre']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#20% for testing, 80% for training

 

model = DecisionTreeClassifier()

model.fit(X_train, y_train)

 

#save already trained model

joblib.dump(model, 'music_recommender.joblib')

 

#loading already trained model

model = joblib.load('music_recommender.joblib')

 

#predictions = model.predict([ [21, 1], [22, 0] ])

#male - 1

#female - 0

predictions = model.predict(X_test)

 

#accuracy score of the model

score = accuracy_score(y_test, predictions)

score

 

#visualizing how model make predictions - .dot file

tree.export_graphviz(model, out_file='music-recommender.dot',

                    feature_names=['age', 'gender'],

                    class_names=sorted(y.unique()),

                    label='all',

                    rounded=True,

                    filled=True)
