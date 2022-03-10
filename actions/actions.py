# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from random import random
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from actions import course


class ActionCourse(Action):

    def name(self) -> Text:
        return "action_course"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            name = tracker.get_slot("langue")
            print(name)

            if name is not None: 
                print("java qua de")
                if course.get_course(name, "define") is not None:
                    print(name)
                    print(course.get_course(name,"define"))                   
                    dispatcher.utter_message(text=course.get_course(name, "define"))

                else:
                    return []
            else:
                dispatcher.utter_message(template="utter_no_langue",attribute="")
        except Exception as e:
            print(str(e))
        return []
