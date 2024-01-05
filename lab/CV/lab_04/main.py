from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Flatten, Dropout, Activation
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.applications.vgg16 import VGG16

import os

model_file = 'dogs-vs-cats.bin'
model = None

datagen = ImageDataGenerator(rescale=1. / 255)
batch_size = 16
train_samples = 17500
val_samples = 3750
test_samples = 3750

train_generator = datagen.flow_from_directory('train', target_size=(150, 150), batch_size=batch_size,
                                              class_mode='binary')
val_generator = datagen.flow_from_directory('val', target_size=(150, 150), batch_size=batch_size, class_mode='binary')
test_generator = datagen.flow_from_directory('test', target_size=(150, 150), batch_size=batch_size,
                                             class_mode='binary')

if not os.path.exists(model_file):
    vgg16 = VGG16(
        weights='imagenet',
        include_top=False,
        input_shape=(150, 150, 3))

    vgg16.trainable = False
    vgg16.summary()

    model = Sequential()
    model.add(vgg16)
    model.add(Flatten())
    model.add(Dense(256))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1))
    model.add(Activation('sigmoid'))

    model.compile(
        loss='binary_crossentropy',
        optimizer=Adam(learning_rate=1e-5),
        metrics=['accuracy'])

    model.fit(
        train_generator,
        steps_per_epoch=train_samples // batch_size,
        epochs=5,
        validation_data=val_generator,
        validation_steps=val_samples // batch_size)

    model.save(model_file)
else:
    model = load_model(model_file)

model.summary()
scores = model.evaluate_generator(test_generator, test_samples // batch_size)
print(scores)
