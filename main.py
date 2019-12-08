
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder
from kivy.config import Config
Config.set('graphics', 'multisamples', '0')
# Config.set('graphics', 'width', '640')
# Config.set('graphics', 'height', '480')


class RootWidget(ScreenManager):
    pass
        
class Testwidget(Screen):
    text  = StringProperty()
    label1 = ObjectProperty()

    def __init__(self, **kwargs):
        super(Testwidget, self).__init__(**kwargs)
        self.text = 'start'

    def buttonClicked(self):
        self.text = 'U'

    def buttonClicked2(self):
        self.text = 'got'

    def buttonClicked3(self):
        pass
    
class SecSc(Screen):
    l0 = ObjectProperty(None)
    t0 = ObjectProperty(None)

    def txtmodify(self):
        self.ids.l0.text = self.ids.t0.text

kv = Builder.load_file("test.kv")

class TestApp(App):
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = "Testing..."

    def build(self):
        return kv

if __name__ == "__main__":
    TestApp().run()
