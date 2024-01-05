from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from tensorflow.keras import utils
import numpy as np

import os
import sys
import shutil

sys.tracebacklimit = 0

model_file = "model.bin"
params_file = "params.txt"

if not os.path.exists(model_file):
    np.random.seed(6585)

    (x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

    x_train = x_train.reshape(60000, 784)
    x_test = x_test.reshape(10000, 784)
    x_train = x_train / 255
    x_test = x_test / 255

    y_train = utils.to_categorical(y_train, 10)
    y_test = utils.to_categorical(y_test, 10)

    max_score = 0
    max_params = ()

    for nepochs in [10, 20, 30]:
        for input_n in [400, 800, 1200]:
            for hidden_n in [200, 400, 800]:
                batch_size = 10
                # for batch_size in [10, 50, 100, 500]:
                for nlayers in range(3):
                    params = (nepochs, input_n, hidden_n, batch_size, nlayers)
                    print("Trying to learn with " + str(params) + "... ", end='')
                    model = Sequential()
                    model.add(Dense(input_n, input_dim=784, activation="relu"))
                    for i in range(nlayers):
                        model.add(Dense(hidden_n))
                    model.add(Dense(10, activation="softmax"))
                    model.compile(loss="categorical_crossentropy", optimizer="SGD", metrics=["accuracy"])
                    try:
                        model.fit(x_train, y_train, batch_size=batch_size, epochs=nepochs, validation_split=0.2,
                                  verbose=0)
                    except ValueError as e:
                        print("FAIL: " + str(e))
                    else:
                        scores = model.evaluate(x_test, y_test, verbose=0)
                        score = round(scores[1] * 100, 4)
                        print("OK (" + str(score) + "%)", end='')
                        if score > max_score:
                            max_score = score
                            max_params = params
                            print(": new best params are: " + str(params), end='')

                            shutil.rmtree(model_file, ignore_errors=True)
                            try:
                                model.save(model_file)
                            except PermissionError:
                                pass
                            with open(params_file, "w") as f:
                                print(params, file=f)
                        print()

model = load_model(model_file)
print(model.summary())
