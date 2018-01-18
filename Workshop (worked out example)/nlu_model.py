from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter


def train_nlu(data, config, model_dir):
	training_data = load_data(data)
	trainer = Trainer(RasaNLUConfig(config))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name = 'weathernlu')
	

def run_nlu():
	#TODO: load the interpreter and test in on input message
    interpreter = Interpreter.load("./models/nlu/default/weathernlu", RasaNLUConfig('config_spacy.json'))
    print(interpreter.parse(u"I am planning my holiday to Barcelona. What is the weather out there at the moment?"))
	
if __name__ == '__main__':
	#TODO: train the model and test in on input messages
    train_nlu('./data/demo_data.json', 'config_spacy.json', './models/nlu')
    run_nlu()