import numpy as np
import random
from keras.models import Sequential, load_model
from keras.layers import Dense
import matplotlib.pyplot as plt


X, logx, logy = [], [], []

for i in range(5000):
    X.append([random.randint(1, 100), random.randint(1, 100)])
    logx.append([np.log(X[i][0]), np.log(X[i][1])])
    logy.append([logx[i][0] - logx[i][1]])


logx = np.array(logx)
logy = np.array(logy).reshape(-1, 1) #check without reshape

model = Sequential()
model.add(Dense(4, input_dim=2))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(logx, logy, epochs=10, batch_size=4, verbose=1)


# model.save('div_model')

# test = np.array([np.log(5), np.log(3)]).reshape(-1, 1).T
# pred = model.predict(test)
# print(np.exp(pred))
