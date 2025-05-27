#Ejercicio kivyMD
 
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MyApp(MDApp):
    def build(self):
        return MDLabel (text="QUE PASE LO QUE PASE", halign="center")

if __name__ =='__main__':
    MyApp().run()