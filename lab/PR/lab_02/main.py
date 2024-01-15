from tensorflow.keras.datasets import boston_housing
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

(x_train, y_train), (x_test, y_test) = boston_housing.load_data()

train_min = x_train.min(axis=0)
train_max = x_train.max(axis=0)

x_train -= 0.5 * (train_max + train_min)
x_train /= 0.5 * (train_max - train_min)

x_test -= 0.5 * (train_max + train_min)
x_test /= 0.5 * (train_max - train_min)

model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(x_train.shape[1],)))
model.add(Dense(10))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse', metrics=['mae'])
model.fit(x_train, y_train, epochs=100, batch_size=10)

pred = model.predict(x_test)
print("Predicted price:", pred[1][0], "correct price:", y_test[1])
