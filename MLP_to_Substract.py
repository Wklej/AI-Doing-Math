import numpy as np
import random
from keras.models import Sequential, load_model
from keras.layers import Dense
import matplotlib.pyplot as plt


X, Y = [], []

for i in range(2000):
    X.append([random.randint(1, 100), random.randint(1, 100)])
    Y.append(X[i][0] - X[i][1])


X = np.array(X)
Y = np.array(Y).reshape(-1, 1)

model = Sequential()
model.add(Dense(4, input_dim=2))
model.add(Dense(4))
model.add(Dense(2))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(X, Y, epochs=7, batch_size=2, verbose=1)


# model.save('sub_model')

# test = np.array([np.log(2), np.log(15)]).reshape(-1, 1).T
# pred = model.predict(test)
# pred = np.exp(pred)
# print(round(pred))
