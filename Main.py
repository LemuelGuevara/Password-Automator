from kivy.graphics import Color
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.graphics import Canvas
from kivy.graphics import Rectangle
from Randomator import *

class MyFrame(Widget):
	username = StringProperty()
	password = StringProperty()
	fontSize = 20
	outLine_color = 66,82,103

	def __init__(self, **kwargs):
		super(MyFrame, self).__init__(**kwargs)

	def generate(self):
		self.username = f"{auto.makeUsername()}"
		self.password = f"{auto.makePass()}"
		
class MyApp(App):
	title = "Username and Password Automator"
	Window.set_title(title)
	Window.clearcolor = (51,51,51,2)

	def build(self):
		return MyFrame()

if __name__ == "__main__":
    MyApp().run()
