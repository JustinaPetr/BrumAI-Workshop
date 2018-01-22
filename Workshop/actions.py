from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet


class ActionWeather(Action):
    def name(self):
        return 'action_weather'

    def run(self, dispatcher, tracker, domain):
        from apixu.client import ApixuClient, ApixuException
        api_key = '' #Provide your apixu Key here
        client = ApixuClient(api_key)
        
        #TODO: retrieve the slot value and make an api call
        loc = 
        current = 
        
        country = current['location']['country']
        city = current['location']['name']
        condition = current['current']['condition']['text']
        temperature_c = current['current']['temp_c']
        temperature_f = current['current']['temp_f']
        humidity = current['current']['humidity']
        wind_mph = current['current']['wind_mph']
        
        #TODO: create a response message and dispatch it to the output channel
        response = 

        return [SlotSet("location", loc)]