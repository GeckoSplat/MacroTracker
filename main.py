
# Program to Show how to use textinput 
# (UX widget) in kivy using .kv file

import kivy  
from kivy.app import App 
kivy.require('2.1.0')
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput 
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import ButtonBehavior 
  
# Create the widget class
class textinp(Widget):
    TextInput.multiline = False
    pass
# Create button Class 
class buttons(ButtonBehavior):
    pass      

  
class MainApp(App):
    
    
    def build(self):

        return textinp()
    # prints to test. should retain input until ADD/SUB/CLEAR
    def process(self):
        text1 = self.root.ids.input1.text
        print(text1)
        text2 = self.root.ids.input2.text
        print(text2) 
        text3 = self.root.ids.input3.text
        print(text3)
        text4 = self.root.ids.input4.text
        print(text4)

    def plusbutton(self): 
        print('ADD button pressed')      

    def subbutton(self):
        print ('SUB button pressed')

    def totalsbutton(self):
        print ('TOTALS button pressed')    

    def clearbutton(self):
        print ('CLEAR button pressed')


if __name__ == "__main__":
    MainApp().run()
    

