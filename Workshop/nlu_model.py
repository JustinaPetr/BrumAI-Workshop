from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter


def train_nlu(data, config, model_dir):
	training_data = load_data(data)
	trainer = Trainer(RasaNLUConfig(config))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir)
	

def run_nlu():
	#TODO: load the interpreter and test in on input message
	#interpreter = 
	#print(interpreter.parse(u""))
    pass
	
if __name__ == '__main__':
	#TODO: train the model and test in on input messages