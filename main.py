import kivy
from kivy.app import App

kivy.require("2.1.0")
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.button import ButtonBehavior
from kivy.core.window import Window
import sqlite3 as sql


# Create the widget class
class textinp(Widget):
    TextInput.multiline = False
    Window.clearcolor = (0, 0, 0.2, 1) # Main screen background colour.
    pass


# Create button Class
class buttons(ButtonBehavior):
    pass


class MainApp(App):
    def build(self):
        self.icon = "PNGs/FoodIcon-32.png"
        return textinp()

    def add_data(self):  # Adds data input from textbox's to database
        text1 = self.root.ids.input1.text
        text2 = self.root.ids.input2.text
        text3 = self.root.ids.input3.text
        text4 = self.root.ids.input4.text
        con = sql.connect("macrosdb")
        cur = con.cursor()
        cur.execute(
            """INSERT INTO Kcal (Kcals,Fats,Carbs,Proteins) VALUES (?,?,?,?)""",
            (text4, text3, text2, text1),
        )
        con.commit()
        cur.execute("select * from Kcal")
        db_check = cur.fetchall()
        print(db_check)
        con.close()

    def remove_last_data(self):  # rowid important here
        con = sql.connect("macrosdb")
        cur = con.cursor()
        cur.execute("""DELETE FROM Kcal WHERE rowid = (SELECT MAX(rowid) FROM Kcal);""")
        con.commit()
        con.close()
        print(" DB ROW DELETED")

    def clear_data(self):  # Clears data from database to start new day of tracking
        con = sql.connect("macrosdb")
        cur = con.cursor()
        cur.execute("""DELETE FROM Kcal;""")
        con.commit()
        con.close()
        print(" ALL DATA DELETED")

    def clear_text_boxes(self):  # Clears text inputs after button pressed
        self.root.ids.input1.text = ""
        self.root.ids.input2.text = ""
        self.root.ids.input3.text = ""
        self.root.ids.input4.text = ""

    def totalsbuttonKcal(
        self,
    ):  # TotalButton for loops, only 1 button for 4 total displays
        con = sql.connect("macrosdb")
        cur = con.cursor()
        cur.execute("SELECT SUM (Kcals) FROM Kcal;")
        Total = cur.fetchall()
        output = "NONE"
        for number in Total:
            try:
                output = f"{round(number[0],1)} {'Kcals'}"
                self.root.ids.outputKcals.text = f"{output}"
            except:
                TypeError
            self.root.ids.outputKcals.text = f"{output}"
        print(Total)
        cur.execute("SELECT SUM (Carbs) FROM Kcal;")
        Total = cur.fetchall()
        for number in Total:
            try:
                output = f"{round(number[0],1)} {'Carbs'}"
                self.root.ids.TOTcbButton.text = f"{output}"
            except:
                TypeError
            self.root.ids.TOTcbButton.text = f"{output}"
        print(Total)
        cur.execute("SELECT SUM (Fats) FROM Kcal;")
        Total = cur.fetchall()
        for number in Total:
            try:
                output = f"{round(number[0],1)} {'Fats'}"
                self.root.ids.TOTfButton.text = f"{output}"
            except:
                TypeError
            self.root.ids.TOTfButton.text = f"{output}"
        print(Total)
        cur.execute("SELECT SUM (Proteins) FROM Kcal;")
        Total = cur.fetchall()
        for number in Total:
            try:
                output = f"{round(number[0],1)} {'Protein'}"
                self.root.ids.TOTpButton.text = f"{output}"
            except:
                TypeError
            self.root.ids.TOTpButton.text = f"{output}"
        print(Total)


if __name__ == "__main__":
    MainApp().run()
