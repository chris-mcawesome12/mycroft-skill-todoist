from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

from todoist.api import TodoistAPI
from os.path import dirname, join

__author__ = 'chrismcawesome'

LOGGER = getLogger(__name__)

##inbox = 151939893
##personal = 151939895
##shopping = 151939896
##work = 151939897
##errands = 151939898
##movies = 151939899
##homeassistant = 2166275738
##mycroft = 2166275728

api = TodoistAPI('YOUR API KEY')

class TodoistSkill1(MycroftSkill):

    def __init__(self):
        super(TodoistSkill1, self).__init__(name="TodoistSkill1")
		
    def initialize(self):
        task_intent = IntentBuilder("TaskIntent").\
            require("TaskKeyword").build()
        self.register_intent(task_intent, self.handle_task_intent)
		
        shopping_intent = IntentBuilder("ShoppingIntent").\
            require("ShoppingKeyword").build()
        self.register_intent(shopping_intent, self.handle_shopping_intent)

        movie_intent = IntentBuilder("MovieIntent").\
            require("MovieKeyword").build()
        self.register_intent(movie_intent, self.handle_movie_intent)
		
    def handle_task_intent(self, message):
	api.sync()
	taks1 = api.items.add('Task1', 151939895)
	api.commit()
        self.speak("task added to to do list")

    def handle_shopping_intent(self, message):
	api.sync()
	taks1 = api.items.add('Task1', 151939896)
	api.commit()
        self.speak("item added to shopping list")

    def handle_movie_intent(self, message):
	api.sync()
	taks1 = api.items.add('Task1', 151939899)
	api.commit()
        self.speak("movie added to to list")
		
	def stop(self):
        pass

def create_skill():
    return TodoistSkill1()
