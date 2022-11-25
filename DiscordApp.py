# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 14:38:28 2022

@author: hanna
"""

#From Discord
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


# logic
class FirstWindow(Screen):
    pass


# Like Page
class SecondWindow(Screen):
    pass


# Like Storage Page
class ThirdWindow(Screen):
    pass


# More Information Page
class FourthWindow(Screen):
    pass



class AwesomeApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstWindow(name='main'))
        sm.add_widget(SecondWindow(name='like'))
        #future , adding screens to like based on the object I am getting from emil/rohith
        #for i in range(0,5)
            #adding the new window
            # sm.add_widget(SecondWindow(name='like'))
            # #adding a mini preview to the storage page
            # sm.add_widget(ThirdWindow)
        sm.add_widget(ThirdWindow(name='storage'))
        sm.add_widget(FourthWindow(name='info'))
        sm.current = 'main'
        return sm


if __name__ == "__main__":
    AwesomeApp().run()