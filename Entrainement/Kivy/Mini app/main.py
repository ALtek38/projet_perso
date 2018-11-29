import kivy.utils
import calendar
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color

#Check ScreenManager et Kivy Garden (pour des "addons")
# Inspire toi de KivyCalendar et le module natif calendar pour le canlendrier
class Main_Window(Widget):
    w = Window
    #Defintion couleurs
    grey = kivy.utils.get_color_from_hex('#a6a9ad')
    red = Color(1,0,0)
    #Set bacground color for main window
    w.clearcolor = grey

    #Definiton du layout
    lay = GridLayout(rows=3, cols=2)
    w.add_widget(lay)

    #layout secondaire
    lay2 = GridLayout(rows=5, cols=3)
    lay.add_widget(lay2)
    lay2.add_widget(Label(text="Hello World", font_size = "20sp"))
    lay2.add_widget(Label(text="Hello World", font_size = "20sp"))
    lay2.add_widget(Label(text="Hello World", font_size = "20sp"))
    lay2.add_widget(Label(text="Hello World", font_size = "20sp"))
    lay2.add_widget(Label(text="Hello World", font_size = "20sp"))
    lay2.add_widget(Label(text="Hello World", font_size = "20sp"))
    lay2.add_widget(Label(text="Hello World", font_size = "20sp"))
    lay2.add_widget(Label(text="Hello World", font_size = "20sp"))
    lay2.add_widget(Label(text="Hello World", font_size = "20sp"))
    lay2.add_widget(Label(text="Hello World", font_size = "20sp"))
    lay2.add_widget(Label(text="Hello World", font_size = "20sp"))

    #Add labels
    message = Label(text="Hello World", font_size = "50sp")
    lay.add_widget(message)
    message2 = Label(text="[color=ff0000]Hello World 2[/color]", font_size = "50sp", markup=True)
    lay.add_widget(message2)

    calendrier = calendar.TextCalendar(calendar.SUNDAY)
    stri = calendrier.formatmonth(2018,11)
    print (stri)
    lay.add_widget(Label(text=stri))

    #Add button for popup
    def display_popup(self):
        popup = Popup(title="Popup",
                        content=Label(text="La souris est bloquee"),
                        size=(100,100))
        popup.open()

    popup_button = Button(text="Popup", font_size=50)
    popup_button.bind(on_press=display_popup)
    lay.add_widget(popup_button)



class Application(App):
    
    def build(self):
        app = Main_Window()
        #Set main window title
        self.title = "Mini App"
        return app

if __name__ == '__main__':
    Application().run()
