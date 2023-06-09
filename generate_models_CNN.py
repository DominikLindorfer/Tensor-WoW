# Image Augmentation on WoW Icons

import matplotlib.pyplot as plt
import numpy as np
import PIL
import random
from os import walk
import pathlib

import tensorflow as tf
import sklearn.model_selection as sk

print(tf.__version__)

from tensorflow.keras import datasets, layers, models
from tensorflow.keras.models import Sequential, save_model, load_model

print("Num GPUs Available: ", len(tf.config.list_physical_devices("GPU")))
tf.test.is_built_with_cuda()
tf.test.is_gpu_available(cuda_only=False, min_cuda_compute_capability=None)
tf.test.gpu_device_name()

# import tensorflow as tf
# from tensorflow.python.client import device_lib

# print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
# device_lib.list_local_devices()


# Data Augmentation Function
def augment_icons(image, numb_rand=1000):
    pw, ph = 30, 30
    bg_black = PIL.Image.new("RGB", (56 + pw, 56 + ph))

    bg_black.paste(image, (int(pw / 2), int(ph / 2)))
    # bg_black.show()

    # Data Augmentation
    rand_x, rand_y = [], []
    for i in range(numb_rand):
        rand_x.append(round(random.gauss(0, np.sqrt(0.15)) * 8))
        rand_y.append(round(random.gauss(0, np.sqrt(0.15)) * 8))

    data_augmented = []

    for i in range(numb_rand):
        left = 15 + rand_x[i]
        upper = 15 + rand_y[i]
        right = left + 56
        bottom = upper + 56

        im1 = bg_black.crop((left, upper, right, bottom))
        data_augmented.append(np.asarray(im1))

    # for i in range(5):
    #     data_augmented[i].show()

    return data_augmented


# Change up the Class Name here!
class_icons = "DeathKnight/"
mypath = "./WoWIcons/" + class_icons

files = []
for dirpath, dirnames, filenames in walk(mypath):
    files.extend(filenames)
    break

print(len(files))

augmented_icons = []
labels = []

i = 0
for f in files:
    fp = open(mypath + f, "rb")
    image = PIL.Image.open(fp)
    ic1 = augment_icons(image, 3000)
    augmented_icons += ic1

    cur_label = [[i] for j in ic1]
    labels += cur_label
    i += 1

augmented_icons_np = np.asarray(augmented_icons)
augmented_icons_np = augmented_icons_np / 255.0
labels = np.asarray(labels)

train_images, test_images, train_labels, test_labels = sk.train_test_split(
    augmented_icons_np, labels, test_size=0.2, random_state=42
)
# train_images, train_labels = augmented_icons_np, labels

plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i])
    # plt.xlabel(le.inverse_transform([train_labels[i]]))
    plt.xlabel(files[train_labels[i][0]])
plt.show()

# CUDA CNN Models
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation="relu", input_shape=(56, 56, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation="relu"))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation="relu"))

model.add(layers.Flatten())
model.add(layers.Dense(64, activation="relu"))
model.add(layers.Dense(len(files)))

model.summary()
model.compile(
    optimizer="adam",
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=["accuracy"],
)
history = model.fit(
    train_images, train_labels, epochs=10, validation_data=(test_images, test_labels)
)
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print(test_acc)

# Save the model
filepath = "./saved_models/" + class_icons
save_model(model, filepath)

# Load the model
model = load_model(filepath, compile=True)

# use_samples = [0,1,2,3]
use_samples = list(range(15))
samples_to_predict = []

# Generate plots for samples
for sample in use_samples:
    # Generate a plot
    reshaped_image = test_images[sample]
    plt.imshow(reshaped_image)
    plt.show()
    samples_to_predict.append(test_images[sample])

# Convert into Numpy array and Predict some Samples
samples_to_predict = np.array(samples_to_predict)
print(samples_to_predict.shape)
predictions = model.predict(samples_to_predict)

classes = np.argmax(predictions, axis=1)
score = tf.nn.softmax(predictions)

for i in range(len(classes)):
    print(files[classes[i]], np.max(score[i]) * 100)

# Convert the Saved TF Model
converter = tf.lite.TFLiteConverter.from_saved_model(filepath)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()

tflite_model_file = pathlib.Path(filepath + "model.tflite")
tflite_model_file.write_bytes(tflite_model)

# Load and test Model in tensorflowlight_test.py
