from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.label = Label(text='Texto original')
        self.button = Button(text='Cambiar texto')
        self.button.bind(on_press=self.change_text)
        
        self.add_widget(self.label)
        self.add_widget(self.button)
    
    def change_text(self, instance):
        self.label.text = 'Texto cambiado'

class TestApp(App):
    def build(self):
        return MyBoxLayout()        

if __name__ == '__main__':
    TestApp().run()