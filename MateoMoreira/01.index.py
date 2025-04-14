from kivy.app import App
from kivy.uix.label import Label

class myapp(App): 
    def build(self):
        return Label(text="hola pabli")

if __name__ =='___main__--':
    myapp().run()