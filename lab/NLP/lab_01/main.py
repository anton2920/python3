from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, SimpleRNN
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from tensorflow.keras import utils
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

max_words = 10000

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_words)

maxlen = 200

x_train = pad_sequences(x_train, maxlen=maxlen)
x_test = pad_sequences(x_test, maxlen=maxlen)

model = Sequential()
model.add(Embedding(max_words, 2, input_length=maxlen))
# model.add(SimpleRNN(16, dropout=0.2, recurrent_dropout=0.2))
model.add(SimpleRNN(16, return_sequences=True))
model.add(SimpleRNN(16))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='rmsprop',
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
