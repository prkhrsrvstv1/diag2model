"""
    Implementation of VGG-16 Model Architecture
    Paper: https://arxiv.org/pdf/1409.1556
    Author: Milad Sadeghi DM - EverLookNeverSee@GitHub.com
"""


from tensorflow.keras.models import Model
from tensorflow.keras.activations import relu, softmax
from tensorflow.keras.layers import Input, Conv2D, Dense, Flatten, MaxPooling2D


# Defining the input layer
input_layer = Input(shape=(224, 224, 3))

# Defining first Conv block
conv_1 = Conv2D(filters=64, kernel_size=(3, 3), activation=relu, padding="same")(input_layer)
conv_2 = Conv2D(filters=64, kernel_size=(3, 3), activation=relu, padding="same")(conv_1)
pooling_1 = MaxPooling2D(pool_size=(3, 3), strides=(2, 2))(conv_2)
