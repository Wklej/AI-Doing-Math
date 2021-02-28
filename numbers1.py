from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import matplotlib.pyplot as plt
from keras.models import save_model

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

network = models.Sequential()
network.add(layers.Dense(256, activation='sigmoid', input_shape=(28 * 28,)))
network.add(layers.Dense(128, activation='sigmoid', input_shape=(28 * 28,)))
network.add(layers.Dense(128, activation='sigmoid', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation="softmax"))

network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['acc'])

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255


train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

history = network.fit(train_images, train_labels, epochs=7, batch_size=32, validation_data=(test_images, test_labels))

# network.save('AI/Projekt PZII/numbers_model')

test_loss, test_acc = network.evaluate(test_images, test_labels)
print('test_acc: ', test_acc)
print('test_loss: ', test_loss)

acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(len(acc))

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.plot(epochs, loss, 'bo', label='Strata trenowania')
ax1.plot(epochs, val_loss, 'b', label='Strata walidacji')
ax1.set_xlabel("Epoka")
ax1.set_ylabel("Strata")
ax1.legend()
ax2.plot(epochs, acc, 'bo', label='Dokladnosc trenowania')
ax2.plot(epochs, val_acc, 'b', label='Dokladnosc walidacji')
ax2.set_xlabel("Epoka")
ax2.set_ylabel("Skuteczność")
ax2.legend()
plt.show()
