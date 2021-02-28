import numpy as np
import random
from keras.models import Sequential, load_model
from keras.layers import Dense


X, Y, logx, logy, logc = [], [], [], [], []

for i in range(2000):
    X.append([random.randint(1, 100), random.randint(1, 100)])
    Y.append(X[i][0] * X[i][1])
    logx.append([np.log(X[i][0]), np.log(X[i][1])])
    logy.append([logx[i][0] + logx[i][1]])
    # logc.append(np.exp(logy[i]))
    # print("X: {} Y: {} = {}".format(X[i], Y[i], logc[i]))


logx = np.array(logx)
logy = np.array(logy).reshape(-1, 1)

model = Sequential()
model.add(Dense(4, input_dim=2))
model.add(Dense(4))
model.add(Dense(2))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(logx, logy, epochs=20, batch_size=2, verbose=1, validation_split=0.2)


# model.save('mul_model')

# test = np.array([np.log(2), np.log(15)]).reshape(-1, 1).T
# pred = model.predict(test)
# pred = np.exp(pred)
# print(round(pred))
