import kivy.utils
import calendar
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
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
<Calendar>:
    GridLayout:
        rows: 5
        cols: 7
        Button:
            text: 'Retour'
            color: [1,0,0,1]
            on_press: root.manager.current = "Dashboard"
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        Button:
            text: 'Jour'
        
<Dashboard>:
    FloatLayout:
        size: root.size
        Header:
            id: dashboard_header
            size_hint: (1, 0.15)
            pos_hint:{'x':0, 'y':0.85}
        Body:
            id: dashboard_body
            size_hint: (0.65, 0.85)
            pos_hint:{'x':0, 'y':0} 
            #On place le bouton ici car c'est le dashboard aui est lie au screen manager
            Button:
                text: "BODY"
                on_press: root.manager.current = "Calendar"
        Right_menu:
            id: dashboard_Right_menu
            size_hint: (0.35, 0.85)
            pos_hint:{'x':0.65, 'y':0} 
        
<Header>:
    GridLayout:
        cols : 2
        Label:
            text: 'Header'
            size_hint_x: None
            width: root.width / 3
            color: [1,0,0,1]
        Button:
            text: 'IMAGE'
            color: [0,1,0,1]

<Body>:
    GridLayout:
        cols: 1

<Right_menu>:
    GridLayout:
        cols: 1
        Button:
            text: "RIGHT MENU"

""")
class Calendar(Screen):
    pass

class Dashboard(Screen):
    pass

class Header(Screen):
    pass

class Right_menu(Screen):
    pass

class Body(Screen):
    pass

#Gestion du screen manager
sm = ScreenManager(transition=FadeTransition())
dashboard = Dashboard(name="Dashboard")
calendar = Calendar(name="Calendar")

sm.add_widget(dashboard)
sm.add_widget(calendar)

class AnimeApp(App):
    
    def build(self):
        #Set main window title
        self.title = "Anime"
        return sm

if __name__ == '__main__':
    AnimeApp().run()
