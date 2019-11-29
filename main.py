from kivy.app import App
from kivy.uix.widget import Widget
# エラー出るんだが使えてる…？
from kivy.properties import StringProperty

class TextWidget(Widget):
    tex = StringProperty()

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.tex = "yo"

    def buttonclicked(self):
        self.tex = "Hello"

    def buttonclicked2(self):
        self.tex = "world"

class TestApp(App):
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = "testing"

    def build(self):
        return TextWidget()


if __name__ == '__main__':
    TestApp().run()