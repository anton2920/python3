from tensorflow.keras.layers import Dense, Activation, SimpleRNN
from tensorflow.keras.models import Sequential, load_model
import numpy as np

import os

model_file = "alice.bin"

fin = open("alice_in_wonderland.txt", 'rb')
lines = []
for line in fin:  # удаляем лишние пробелы
    line = line.strip().lower()
    line = line.decode("ascii", "ignore")
    if len(line) == 0:
        continue
    lines.append(line)
fin.close()
text = " ".join(lines)

chars = {c for c in text}
nb_chars = len(chars)
char2index = {c: i for i, c in enumerate(sorted(chars))}
index2char = {i: c for i, c in enumerate(sorted(chars))}

S_LEN = 10
model = None

if not os.path.exists(model_file):
    STEP = 1
    input_chars = []
    label_chars = []
    for i in range(0, len(text) - S_LEN, STEP):
        input_chars.append(text[i:i + S_LEN])
        label_chars.append(text[i + S_LEN])

    X = np.zeros((len(input_chars), S_LEN, nb_chars), dtype=bool)
    y = np.zeros((len(input_chars), nb_chars), dtype=bool)
    for i, input_char in enumerate(input_chars):
        for j, ch in enumerate(input_char):
            X[i, j, char2index[ch]] = 1
        y[i, char2index[label_chars[i]]] = 1

    model = Sequential()
    model.add(SimpleRNN(128, input_shape=(S_LEN, nb_chars), unroll=True))
    model.add(Dense(nb_chars))
    model.add(Activation("softmax"))
    model.compile(loss="categorical_crossentropy", optimizer="rmsprop")

    test_chars = None
    for iteration in range(50):
        print("\nIteration: %d" % iteration)

        model.fit(X, y, batch_size=128, epochs=1)

        test_idx = np.random.randint(len(input_chars))
        test_chars = input_chars[test_idx]
        print("Input: %s (%d chars)" % (test_chars, len(test_chars)))
        print("Output: ", test_chars, end="")

        for i in range(50):
            Xtest = np.zeros((1, S_LEN, nb_chars))
            for i, ch in enumerate(test_chars):
                Xtest[0, i, char2index[ch]] = 1
            pred = model.predict(Xtest, verbose=0)[0]
            ypred = index2char[np.argmax(pred)]
            print(ypred, end="")
            test_chars = test_chars[1:] + ypred

    model.save(model_file)
else:
    model = load_model(model_file)

model.summary()

text = input("Type input text: ").lower()
lines = []

while (len(text)) and (len(text) % S_LEN != 0):
    text += ' '

for i in range(len(text) // S_LEN):
    line = text[i * S_LEN:(i + 1) * S_LEN]
    lines.append(line)

print("Output: ", end='')
for line in lines:
    print(line, end='')

    for i in range(100):
        Xtest = np.zeros((1, S_LEN, nb_chars))
        for i, ch in enumerate(line):
            Xtest[0, i, char2index[ch]] = 1
        pred = model.predict(Xtest, verbose=0)[0]
        ypred = index2char[np.argmax(pred)]
        print(ypred, end="")
        line = line[1:] + ypred
print()
