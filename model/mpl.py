import keras
from keras import layers, Model
from .base_model import BaseModel
from utils import Config

class MPLModel(BaseModel):

    @classmethod
    def create_model(cls, input_shape, num_actions, config) -> Model:
        # hidden_layers, other = cls.get_config(config)
        # other, inexistant, hidden_layers = cls.get_config_vars(config, 'another_param', 'inexistant', 'hidden_layers')
        default_dense_layers = [64, 64]
        dense_layers = Config.get_layers_config(config, default_dense_layers)

        inputs = keras.Input(shape=input_shape)
        x = inputs
        for layer_config in dense_layers:
            x = layers.Dense(**layer_config)(x)
        
        outputs = layers.Dense(num_actions, activation="linear", kernel_initializer='he_uniform')(x)
        model = Model(inputs=inputs, outputs=outputs,)
        return model