import abc, numpy as np
from keras import Model

class BaseModel(metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def create_model(cls, input_shape, output_shape, config:dict) -> Model:
        raise NotImplementedError