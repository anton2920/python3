from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, MaxPooling1D, Conv1D, Flatten, Dropout
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from tensorflow.keras import utils
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

max_words = 10000
maxlen = 200

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_words)

x_train = pad_sequences(x_train, maxlen=maxlen)
x_test = pad_sequences(x_test, maxlen=maxlen)

model = Sequential()
model.add(Embedding(max_words, 128, input_length=maxlen))
model.add(Conv1D(100, 5, activation='relu'))
model.add(Conv1D(100, 5, activation='relu'))
model.add(Dropout(0.15))
model.add(MaxPooling1D(pool_size=2))
model.add(Conv1D(200, 5, activation='relu'))
model.add(Conv1D(200, 5, activation='relu'))
model.add(Dropout(0.15))
model.add(MaxPooling1D(pool_size=2))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
# model.add(Dense(10))
model.add(Dropout(0.15))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

earlyStopping = EarlyStopping(patience=10, verbose=0, monitor='val_loss', mode='min')
mcp_save = ModelCheckpoint('.mdl_wts.hdf5', save_best_only=True, monitor='val_loss', mode='min')
reduce_lr_loss = ReduceLROnPlateau(factor=0.1, patience=5, verbose=1, epsilon=1e-4, monitor='val_loss', mode='min')
history = model.fit(x_train, y_train,
                    epochs=100,
                    batch_size=32,
                    validation_split=0.1,
                    callbacks=[earlyStopping, mcp_save, reduce_lr_loss])
model.load_weights('.mdl_wts.hdf5')

scores = model.evaluate(x_test, y_test, verbose=1)
print('Точность на тестовых данных: %.2f%%' % (scores[1] * 100))
