from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('ChatBot.kv')

class MyLayout(Widget):
    def press(self):

        name = self.ids.name_input.text
        # update the label
        self.ids.name_input.text = ''

        self.ids.name_label.text =f'Hello {name}! Do you have nickname ?'
        ans = self.ids.name_input.text

        self.ids.name_input.text = ''

class AwesomeApp(App):

    def build(self): 
        return MyLayout()

if __name__ == '__main__':
    AwesomeApp().run()