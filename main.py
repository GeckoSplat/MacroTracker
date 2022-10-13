
# Program to Show how to use textinput 
# (UX widget) in kivy using .kv file

import kivy  
from kivy.app import App 
kivy.require('2.1.0')
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput 
from kivy.uix.relativelayout import RelativeLayout
  
# Create the widget class
class textinp(Widget):

    pass
  
class MainApp(App):
    
    
    def build(self):

        return textinp()
    
    def process(self):
        text1 = self.root.ids.input1.text
        print(text1)
        text2 = self.root.ids.input2.text
        print(text2) 
        text3 = self.root.ids.input3.text
        print(text3)
        text4 = self.root.ids.input4.text
        print(text4)
        
        #print(text1,text2,text3,text4)  # this works !!


  

if __name__ == "__main__":
    MainApp().run()