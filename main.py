import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout  # one of many layout structures
from kivy.uix.textinput import TextInput  # allow for ...text input.
from kivy.uix.image import Image, AsyncImage
from kivy.core.window import Window
from kivy.graphics import Color
from kivy.lang import Builder
kivy.require("1.11.1")
Builder.load_string('''
<GridLayout>
    canvas.before:
        Color:
            rgba: 1, 0, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size
''')

# An actual app is likely to consist of many different
# "pages" or "screens." Inherit from GridLayout

class ConnectPage(GridLayout):
    # runs on initialization
    def __init__(self, **kwargs):
        # we want to run __init__ of both ConnectPage AAAAND GridLayout
        super().__init__(**kwargs)
        
        self.cols =6# used for our grid
        
        self.row_force_default=True
        self.row_default_height=40

        # widgets added in order, so mind the order.
        self.add_widget(Label(text="Patient's Name:"))  # widget #1, top left
        self.pname = TextInput(multiline=False)  # defining self.ip...
        self.add_widget(self.pname) # widget #2, top right

        self.add_widget(Label(text="Patient ID:"))
        self.pid=TextInput(multiline=True)
        self.add_widget(self.pid)

        self.add_widget(Label(text="Age:"))
        self.age= TextInput(multiline=False)
        self.add_widget(self.age)

        self.add_widget(Label(text="Date of Birth:"))
        self.dob=TextInput(multiline=False)
        self.add_widget(self.dob)

        self.add_widget(Label(text='Temperature:'))
        self.temp= TextInput(multiline=False)
        self.add_widget(self.temp)

        self.add_widget(Label(text="Gender:"))
        self.gender=TextInput(multiline=False)
        self.add_widget(self.gender)

        self.add_widget(Label(text="Date: "))
        self.date=TextInput(multiline=False)
        self.add_widget(self.date)

        self.add_widget(Label(text="Health Description:"))
        self.description=TextInput(multiline=True)
        self.add_widget(self.description)
class NuviApp(App):
    def build(self):
        return ConnectPage()



if __name__ == "__main__":
    NuviApp().run()