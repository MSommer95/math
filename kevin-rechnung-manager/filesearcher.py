
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

from os import *
import webbrowser


class ConnectPage(GridLayout):
    def _init_(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Monat:"))
        self.monat = TextInput(multiline = False)
        self.add_widget(self.monat)

        self.add_widget(Label(text="Jahr:"))
        self.jahr = TextInput(multiline = False)
        self.add_widget(self.jahr)


class rechnungManager(App):
    def build(self):
        return ConnectPage()


if __name__ == "_main_":
    rechnungManager().run()

    path = 'C:/Users/zonaa/Desktop/Rechnungen'
    direct = listdir(path)

    for file in direct:
        print(file)
        #webbrowser.open_new(r'C:/Users/zonaa/Desktop/Rechnungen/' + file)
