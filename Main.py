from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import StringProperty
from Randomator import *


# class MyLabel(Label):


class MyGrid(Widget):
	username = StringProperty()
	password = StringProperty()

	def __init__(self, **kwargs):
		super(MyGrid, self).__init__(**kwargs)

	def generate(self):
		self.username = f"{auto.makeUsername()}"
		self.password = f"{auto.makePass()}"
		

class MyApp(App):
	
	def build(self):
		return MyGrid()
    


if __name__ == "__main__":
    MyApp().run()
