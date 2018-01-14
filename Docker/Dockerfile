# Docker image for Brum AI workshop Jan 2018

FROM python

LABEL maintainer="rob@styles.to"

#Install Python dependencies
RUN git clone https://github.com/JustinaPetr/BrumAI-Workshop.git
RUN cd BrumAI-Workshop && pip install -r requirements.txt
RUN python -m spacy download en
RUN pip install rasa_core
RUN git clone https://github.com/apixu/apixu-python
RUN cd apixu-python && python setup.py install

#Install node
RUN apt-get update
RUN apt-get -y install curl
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash
RUN apt-get install -y nodejs

#Install rasa_nlu data visualisation tool
RUN npm i -g rasa-nlu-trainer

CMD ["/bin/bash"]