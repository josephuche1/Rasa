# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


# Custom Actions for RASA Chatbot
# This file contains Python classes that implement custom actions for the chatbot

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests
import os
from datetime import datetime

class ActionGetWeather(Action):
    """
    Custom action to get weather information.
    This action is triggered when the user asks about the weather.
    It uses the OpenWeatherMap API to fetch weather data.
    """
    def name(self) -> Text:
        return "action_get_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Get the location from the latest message
        location = next(tracker.get_latest_entity_values("location"), None)
        
        if not location:
            dispatcher.utter_message(text="I need to know which location you want the weather for. Please specify a city.")
            return []
        
        try:
            # Get API key from environment variable
            api_key = os.getenv("OPENWEATHER_API_KEY")
            if not api_key:
                dispatcher.utter_message(text="I'm sorry, but I'm not properly configured to check the weather. Please ask my administrator to set up the weather service.")
                return []

            # Make API request to OpenWeatherMap
            base_url = "http://api.openweathermap.org/data/2.5/weather"
            params = {
                "q": location,
                "appid": api_key,
                "units": "metric"  # Use metric units (Celsius)
            }
            
            response = requests.get(base_url, params=params)
            data = response.json()

            if response.status_code == 200:
                # Extract weather information
                weather_desc = data["weather"][0]["description"]
                temp = data["main"]["temp"]
                humidity = data["main"]["humidity"]
                wind_speed = data["wind"]["speed"]
                
                # Format the response
                message = (
                    f"The weather in {location} is currently {weather_desc}. "
                    f"The temperature is {temp}°C with {humidity}% humidity. "
                    f"Wind speed is {wind_speed} m/s."
                )
                
                dispatcher.utter_message(text=message)
            else:
                dispatcher.utter_message(text=f"I'm sorry, I couldn't find weather information for {location}. Please check if the city name is correct.")
        
        except Exception as e:
            dispatcher.utter_message(text="I'm sorry, I encountered an error while fetching the weather information. Please try again later.")
            print(f"Error fetching weather: {e}")
        
        return [] 