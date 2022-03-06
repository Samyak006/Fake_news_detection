import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout,LSTM
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# getting the input from csv files.
u = pd.read_csv('train.csv')
df = pd.DataFrame(u)
X_train = np.array(df.drop(['label'],1))
y_train = np.array(df['label'])

#preprocessing the input 
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train)

v = pd.read_csv('test.csv')
dft = pd.DataFrame(v)
X_test = np.array(df.drop(['label'],1))
y_test = np.array(df['label'])
# w = pd.read_csv('submit.csv')
# X_test = np.array(v)
# y_test = np.array(w)

# print(y_test)


model = Sequential()

model.add(LSTM(128,input_shape = (X_train.shape[1:]),activation ='relu',return_sequence = True))
model.add(Dropout(0.2))

model.add(LSTM(128,activation = "relu"))
model.add(Dropout(0.2))

model.add(Dense(32,activation = 'relu'))
model.add(Dropout(0.2))

model.add(Dense(10,activation = 'softmax'))
opt = tf.keras.optimizers.Adam(lr = 1e-3,decay = 1e-5)
model.compile(loss = 'sparse_categorical_crossentropy',optimizer=opt,metrics=['accuracy'])

model.fit(X_train,y_train,epoch = 3,validation_data = (X_test,y_test))
