
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
  
class MainApp(App):
    
    
    def build(self):

        self.icon = 'PNGs/FoodIcon-32.png'

        def database(self): # commented out lines as only needed to first create DB
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

    def process(self):  # Defined global variable
        global text1,text2,text3,text4    
        text1 = self.root.ids.input1.text
        text2 = self.root.ids.input2.text 
        text3 = self.root.ids.input3.text
        text4 = self.root.ids.input4.text

    def add_data(self): # Defined text variables again here as kept erroring without this , unsure why.
        text1 = self.root.ids.input1.text
        text2 = self.root.ids.input2.text 
        text3 = self.root.ids.input3.text
        text4 = self.root.ids.input4.text
        con = sql.connect('macrosdb')
        cur = con.cursor()
        cur.execute("""INSERT INTO Kcal (Kcals,Fats,Carbs,Proteins) VALUES (?,?,?,?)""",
        (text4,text3,text2,text1))
        con.commit()
        cur.execute('select * from Kcal')
        db_check = cur.fetchall()
        print(db_check)
        con.close()
  
    def remove_last_data(self):# rowid important here
        con = sql.connect('macrosdb')
        cur = con.cursor()
        cur.execute("""DELETE FROM Kcal WHERE rowid = (SELECT MAX(rowid) FROM Kcal);""") 
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

    def clear_text_boxes(self):
        self.root.ids.input1.text = ''
        self.root.ids.input2.text = ''
        self.root.ids.input3.text = ''
        self.root.ids.input4.text = ''         

    def totalsbuttonKcal(self): # TotalButton for loops, only 1 button for 4 total displays
        con = sql.connect('macrosdb')
        cur = con.cursor()   
        cur.execute('SELECT SUM (Kcals) FROM Kcal;')
        Total = cur.fetchall()
        global output
        output = 'NONE'
        for number in Total: 
            try:                   
                output = f"{round(number[0],1)} {'Kcals'}"
                self.root.ids.outputKcals.text = f'{output}'
            except: TypeError
            self.root.ids.outputKcals.text = f'{output}'
        print(Total)
        cur.execute('SELECT SUM (Carbs) FROM Kcal;')
        Total = cur.fetchall()
        for number in Total:
            try:                    
                output = f"{round(number[0],1)} {'Carbs'}"
                self.root.ids.TOTcbButton.text = f'{output}'
            except: TypeError
            self.root.ids.TOTcbButton.text = f'{output}'
        print(Total)
        cur.execute('SELECT SUM (Fats) FROM Kcal;')
        Total = cur.fetchall()
        for number in Total:
            try:                  
                output = f"{round(number[0],1)} {'Fats'}"
                self.root.ids.TOTfButton.text = f'{output}'
            except: TypeError
            self.root.ids.TOTfButton.text = f'{output}'    
        print(Total)
        cur.execute('SELECT SUM (Proteins) FROM Kcal;')
        Total = cur.fetchall()
        for number in Total:                   
            try:
                output = f"{round(number[0],1)} {'Protein'}"
                self.root.ids.TOTpButton.text = f'{output}'
            except:TypeError
            self.root.ids.TOTpButton.text = f'{output}'
        print(Total)      


if __name__ == "__main__":
    MainApp().run()