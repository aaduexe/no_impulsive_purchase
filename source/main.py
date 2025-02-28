import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

kivy.require('1.9.0')

class CanICallItAnything(BoxLayout):
    def __init__(self):
        super(CanICallItAnything, self).__init__() # What is the point of these 2 lines?
    def ask_question(self):
        self.questionLabel.text = "Working?"

class NoImpulse(App):
    def build(self):
        return CanICallItAnything()


""" noimpulse = NoImpulse()
noimpulse.run() #why this and not this:
 """
NoImpulse().run()