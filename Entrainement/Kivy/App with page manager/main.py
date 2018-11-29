import kivy.utils
import calendar
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.uix.screenmanager import FadeTransition, ScreenManager, Screen
#####################################################################

Builder.load_string("""
<Hello_screen>:
    canvas.before:
        Color:
            rgba: 0,0.5,0.5,1
        Rectangle:
            size: root.size
    GridLayout:
        rows : 2
        cols : 1
        padding: [50,50,50,50]
        Label:
            text: 'Hello !'
            size_hint_x: None
            width: root.width / 3
            height: root.height / 3
            font_size: 50
            color: [1,0,0,1]
        Button:
            text: 'Go to calendar'
            size_hint_x: None
            width: root.width * 2 / 3
            height: root.height * 2 / 3
            font_size: 80
            on_press: root.manager.current = 'Calendar'

<Calendar_screen>:
    canvas.before:
        Color:
            rgba: 0,0.1,0.8,0.66
        Rectangle:
            size: root.size
    GridLayout:
        rows : 2
        cols : 1
        Label:
            text: 'Calendar'
            font_size: '50sp'
            color: [0,1,0,1]
        Button:
            text: 'Back to hello'
            on_press: root.manager.current = 'Hello'
""")

class Hello_screen(Screen):
    pass

class Calendar_screen(Screen):
    pass

sm = ScreenManager(transition=FadeTransition())

hello_screen = Hello_screen(name="Hello")
calendar_screen = Calendar_screen(name="Calendar")

sm.add_widget(hello_screen)
sm.add_widget(calendar_screen)

class AnimeApp(App):
    
    def build(self):
        #Set main window title
        self.title = "My App"
        return sm

if __name__ == '__main__':
    AnimeApp().run()
