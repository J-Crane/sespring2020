from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.actionbar import ActionButton
from kivy.uix.screenmanager import FadeTransition, FallOutTransition
from kivy.graphics import Color, Rectangle, Line
from kivy.uix.widget import Widget
from kivy.uix.slider import Slider
from math import cos, sin, pi
from kivy.clock import Clock
#from KivyCalendar import DatePicker
import datetime


class HomeWin(Screen):
    pass
class InchFootWin(Screen):
    pass
class FootYardWin(Screen):
    pass
class DayHourWin(Screen):
    pass
class WeekDayWin(Screen):
    pass
class ResultWindow(Screen):
    pass

class LengthWin(Screen):
    pass

class TimeWin(Screen):
    pass

class LoginWin(Screen):
    pass

class InterFootInch(Screen):
    # def manipulate(self, slider):
    #     app = App.get_running_app()
    #     self.canvas.rect1.size = int(slider.value)
    #     self.rect2.size = int(slider.value) * 7
    pass

class InterFootYard(Screen):
    pass

class InterDayHour(Screen):
    pass

#class InterWeekDay(Screen):
 #   pass

class scrManager(ScreenManager):
    def FeetToYard(self, userFootYard):
        app = App.get_running_app()
        if (float(userFootYard.text)/3) > 1:
            app.result = f'{float(userFootYard.text)/3:0.2f}' + " Yards"
        else:
            app.result = f'{float(userFootYard.text)/3: 0.2f}' + " Yard"

    def YardToFeet(self, userFootYard):
        app = App.get_running_app()
        if (3 * float(userFootYard.text)) > 1:
            app.result = f'{(3 * float(userFootYard.text)):0.2f}' + " Feet"
        else:
            app.result = f'{(3 * float(userFootYard.text)):0.2f}' + " Foot"

    def FeetToInches(self, userInchFoot):

        app = App.get_running_app()
        if (12 * float(userInchFoot.text)) > 1:
            app.result = f'{(12 * float(userInchFoot.text)):0.2f}' + " Inches"
        else:
            app.result = f'{(12 * float(userInchFoot.text)):0.2f}' + " Inch"


    def InchToFeet(self, userInchFoot):
        #inchData = userSource.text
        #tempData2 = str(int(inchData) / 12)
        app = App.get_running_app()
        if (float(userInchFoot.text)/12) > 1:
            app.result = f'{float(userInchFoot.text)/12:0.2f}' + " Feet"
        else:
            app.result = f'{float(userInchFoot.text) / 12:0.2f}' + " Foot"

    def DayToHour(self, userDayHour):
        app = App.get_running_app()
        if(24 * float(userDayHour.text)) > 1:
            app.result = f'{(24 * float(userDayHour.text)):0.2f}' + " Hours"
        else:
            app.result = f'{(24 * float(userDayHour.text)):0.2f}' + " Hour"

    def HourToDay(self, userDayHour):
        app = App.get_running_app()
        if(float(userDayHour.text)/24) > 1:
            app.result = f'{float(userDayHour.text)/24:0.2f}' + " Days"
        else:
            app.result = f'{float(userDayHour.text)/24:0.2f}' + " Day"

    def WeekToDay(self, userWeekDay):
        app = App.get_running_app()
        if(7 * float(userWeekDay.text)) > 1:
            app.result = f'{(7 * float(userWeekDay.text)):0.2f}' + " Days"
        else:
            app.result = f'{(7 * float(userWeekDay.text)):0.2f}' + " Day"

    def DayToWeek(self, userWeekDay):
        app = App.get_running_app()
        if(float(userWeekDay.text)/7) > 1:
            app.result = f'{float(userWeekDay.text)/7:0.2f}' + " Weeks"
        else:
            app.result = f'{float(userWeekDay.text)/7:0.2f}' + " Week"



#kv = Builder.load_file("multiclockunit.kv")

class Ticks(Widget):
    def __init__(self, **kwargs):
        super(Ticks, self).__init__(**kwargs)
        self.bind(pos=self.update_clock)
        self.bind(size=self.update_clock)
        Clock.schedule_interval(self.update_clock, 1)

    def update_clock(self, *args):
        self.canvas.clear()
        with self.canvas:
            time = datetime.datetime.now()
            Color(0.9, 0.5, 0.2)
            Line(points=[self.center_x, self.center_y, self.center_x+0.8*self.r*sin(pi/30*time.second), self.center_y+0.8*self.r*cos(pi/30*time.second)], width=1, cap="round")
            Color(0.1, 0.6, 0.9)
            Line(points=[self.center_x, self.center_y, self.center_x+0.7*self.r*sin(pi/30*time.minute), self.center_y+0.7*self.r*cos(pi/30*time.minute)], width=2, cap="round")
            Color(0.4, 0.7, 0.4)
            th = time.hour*60 + time.minute
            Line(points=[self.center_x, self.center_y, self.center_x+0.5*self.r*sin(pi/360*th), self.center_y+0.5*self.r*cos(pi/360*th)], width=3, cap="round")

class InterWeekDay(Screen):
    # def Picker(self):
    #     self.laDate = self.datepicker.text
    #     self.datepicked = datetime.datetime.strptime(self.laDate, '%d.%m.%Y').strftime('%d/%m/%Y')
    #     self.myLabel.text = str(self.datepicked)
    pass

class MyTouch(Widget):
    pass



class MyMainApp(App):
    result = StringProperty("initialization")
    #rect1.size = ObjectProperty(0,50)
    # rect2.size = ObjectProperty(0,50)
    def build(self):
        return Builder.load_file("multiclockunit.kv")




if __name__ == "__main__":
    MyMainApp().run()