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
        api_key = '0348f304ef804ad9826142149180201'
        client = ApixuClient(api_key)
        
        #TODO: retrieve the slot value and make an api call
        loc = tracker.get_slot('location')
        current = client.getCurrentWeather(q=loc)
        
        country = current['location']['country']
        city = current['location']['name']
        condition = current['current']['condition']['text']
        temperature_c = current['current']['temp_c']
        temperature_f = current['current']['temp_f']
        humidity = current['current']['humidity']
        wind_mph = current['current']['wind_mph']
        
        #TODO: create a response message and dispatch it to the output channel
        response = 'It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.'.format(condition, city, temperature_c, humidity, wind_mph)
        dispatcher.utter_message(response)
        return [SlotSet("location", loc)]