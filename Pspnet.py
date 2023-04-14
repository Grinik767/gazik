from keras.models import Model
from keras.layers import Input, concatenate, MaxPooling2D, Conv2D, BatchNormalization, \
    UpSampling2D
from keras.optimizers import Adam
from Unet import dice_coef


def pspnet(num_classes, input_shape):
    img_input = Input(input_shape)

    input = Conv2D(64, (3, 3), padding='same', activation='relu')(img_input)
    input = BatchNormalization()(input)

    # Block 1
    block1 = MaxPooling2D((2, 2))(input)
    block1 = Conv2D(16, (2, 2), padding='same', activation='relu')(block1)
    block1 = BatchNormalization()(block1)

    block1 = Conv2D(16, (2, 2), padding='same', activation='relu')(block1)
    block1 = BatchNormalization()(block1)

    block1 = Conv2D(16, (2, 2), padding='same', activation='relu')(block1)
    block1 = BatchNormalization()(block1)

    block1 = UpSampling2D((2, 2))(block1)

    # Block 2
    block2 = MaxPooling2D((4, 4))(input)
    block2 = Conv2D(32, (4, 4), padding='same', activation='relu')(block2)
    block2 = BatchNormalization()(block2)

    block2 = Conv2D(32, (4, 4), padding='same', activation='relu')(block2)
    block2 = BatchNormalization()(block2)

    block2 = Conv2D(32, (4, 4), padding='same', activation='relu')(block2)
    block2 = BatchNormalization()(block2)

    block2 = UpSampling2D((4, 4))(block2)

    # Block 3
    block3 = MaxPooling2D((8, 8))(input)
    block3 = Conv2D(64, (3, 3), padding='same', activation='relu')(block3)
    block3 = BatchNormalization()(block3)

    block3 = Conv2D(64, (3, 3), padding='same', activation='relu')(block3)
    block3 = BatchNormalization()(block3)

    block3 = Conv2D(64, (3, 3), padding='same', activation='relu')(block3)
    block3 = BatchNormalization()(block3)

    block3 = UpSampling2D((8, 8))(block3)

    # #Block 4
    block4 = MaxPooling2D((16, 16))(input)
    block4 = Conv2D(128, (3, 3), padding='same', activation='relu')(block4)
    block4 = BatchNormalization()(block4)

    block4 = Conv2D(128, (3, 3), padding='same', activation='relu')(block4)
    block4 = BatchNormalization()(block4)

    block4 = Conv2D(128, (3, 3), padding='same', activation='relu')(block4)
    block4 = BatchNormalization()(block4)

    block4 = UpSampling2D((16, 16))(block4)
    block4 = Conv2D(128, (3, 3), padding='same', activation='relu')(block4)

    output = concatenate([input, block1, block2, block3, block4])
    output = Conv2D(128, 3, activation='relu', padding='same')(output)
    output = Conv2D(2, 3, activation='softmax', padding='same')(output)

    model = Model(img_input, output)

    model.compile(optimizer=Adam(),
                  loss='categorical_crossentropy',
                  metrics=[dice_coef])
    return model
