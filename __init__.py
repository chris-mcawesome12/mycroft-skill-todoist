from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

from todoist.api import TodoistAPI
from os.path import dirname, join

__author__ = 'chrismcawesome'

LOGGER = getLogger(__name__)

inbox = 151939893
personal = 151939895
shopping = 151939896
work = 151939897
errands = 151939898
movies = 151939899

api = TodoistAPI('YOUR AIP KEY')

class TodoistSkill1(MycroftSkill):

    def __init__(self):
        super(TodoistSkill1, self).__init__(name="TodoistSkill1")
		
	def initialize(self):
            task_intent = IntentBuilder("TaskIntent").\
                require("TaskKeyword").require("Task").require("Project").build()
            self.register_intent(task_intent, self.handle_task_intent)

        def handle_task_intent(self, message):
            task = message.data["Task"]
            project = message.data["Project"]
            if project == "personal":
                project = personal
                api.sync()
                Task1 = api.items.add(task, project)
                api.commit()
                self.speak("task added")

            else:
                project = shopping
                api.sync()
                Task1 = api.items.add(task, project)
                api.commit()
                self.speak("task added")

	def stop(self):
            pass

def create_skill():
    return TodoistSkill1()
