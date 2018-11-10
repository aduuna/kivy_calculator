import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class Homescreen(GridLayout):

    def calc(self, user_input):
        try:
            ans = eval(user_input)
            self.entry.text = str(ans)
        except:
            self.display.text = "Math Err"
    
class CalculatorApp(App):

    def build(self):
        return Homescreen()

CalculatorApp().run()