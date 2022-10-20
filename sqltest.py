

import kivy  
from kivy.app import App 
kivy.require('2.1.0')
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput 
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import ButtonBehavior 
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
import sqlite3 as sql



 #Create the widget class
class textinp(Widget):
    TextInput.multiline = False
    pass 

# Create button Class 
class buttons(ButtonBehavior):
    pass    


# Main  
class MainApp(App):
    
    
    def build(self):

        def database(self):
            con = sql.connect('macrosdb')
            cur = con.cursor()
           # cur.execute(""" CREATE TABLE Kcal(
           # Kcals , Fats , Carbs , Proteins )    
           # """)        
            con.commit()
            con.close()
            print(' DB DONE' )
        database(self)       
        return textinp()

    
    def add_data(self):
        con = sql.connect('macrosdb')
        cur = con.cursor()
        cur.execute("""INSERT INTO Kcal (Kcals,Fats,Carbs,Proteins) VALUES (?,?,?,?)""",
        (text4,text3,text2,text1))
        con.commit()
        cur.execute('select * from Kcal')
        db_check = cur.fetchall()
        print(db_check)
        con.close()
        print(' DB DONE')    

    def remove_last_data(self):
        con = sql.connect('macrosdb')
        cur = con.cursor()
        cur.execute("""DELETE FROM Kcal WHERE rowid = (SELECT MAX(rowid) FROM Kcal);""") # rowid important here
        con.commit()
        con.close()
        print(' DB ROW DELETED')

    def clear_data(self):
        con = sql.connect('macrosdb')
        cur = con.cursor()   
        cur.execute("""DELETE FROM Kcal;""")
        con.commit()
        con.close()
        print(' ALL DATA DELETED')
      
    def process(self):
        global text1,text2,text3,text4    
        text1 = self.root.ids.input1.text
        print(text1)
        text2 = self.root.ids.input2.text
        print(text2) 
        text3 = self.root.ids.input3.text
        print(text3)
        text4 = self.root.ids.input4.text
        print(text4)


    def totalsbuttonKcal(self):
        con = sql.connect('macrosdb')
        cur = con.cursor()   
        cur.execute('SELECT SUM (Kcals) FROM Kcal;')
        Total = cur.fetchall()
        for number in Total:                    # This loop works
            output = f"{number[0]} {'Kcals'}"
            self.root.ids.outputKcals.text = f'{output}'


        print(Total)




    

         
if __name__ == "__main__":
    MainApp().run()
    




# Have total call it back AND ADD IT TOGETHER FROM DB, last 3 buttons TO DO
# Clear text field when button pressed
# compile after making pretty


