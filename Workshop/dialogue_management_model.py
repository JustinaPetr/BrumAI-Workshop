from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging

from builtins import str


from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RasaNLUInterpreter, RegexInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RegexInterpreter	
from rasa_core.interpreter import RasaNLUInterpreter

logger = logging.getLogger(__name__)

class WeatherPolicy(KerasPolicy):
    def model_architecture(self, num_features, num_actions, max_history_len):
        """Build a Keras model and return a compiled model."""
        from keras.layers import LSTM, Activation, Masking, Dense
        from keras.models import Sequential

        n_hidden = 32  # size of hidden layer in LSTM
        # Build Model
        batch_shape = (None, max_history_len, num_features)

        model = Sequential()
        model.add(Masking(-1, batch_input_shape=batch_shape))
        model.add(LSTM(n_hidden, batch_input_shape=batch_shape))
        model.add(Dense(input_dim=n_hidden, output_dim=num_actions))
        model.add(Activation('softmax'))

        model.compile(loss='categorical_crossentropy',
                      optimizer='adam',
                      metrics=['accuracy'])

        logger.debug(model.summary())
        return model
		
		
def train_dialogue(domain_file='weather_domain.yml',
                   model_path='./models/dialogue',
                   training_data_file='./data/stories.md'):
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(), WeatherPolicy()])

    agent.train(#TODO set the model parameters
                training_data_file,
                max_history = ,
                epochs = ,
                batch_size = ,
                augmentation_factor = ,
                validation_split = 
    )

    agent.persist(model_path)
    return agent	

	
	
def run_weather_bot(serve_forever=True):
	#TODO: Load an interpreter and the agent
    #TODO: start listening to incoming messages
    pass

if __name__ == '__main__':
	#TODO: train the model and test it
