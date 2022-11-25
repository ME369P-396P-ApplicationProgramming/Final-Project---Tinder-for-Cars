from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage





#logic

class FirstWindow(Screen):
    
	pass

#Like Page
class SecondWindow(Screen):
	pass

#Like Storage Page
class ThirdWindow(Screen):
    
    pass

#More Information Page
class FourthWindow(Screen):
    

	pass

class WindowManager(ScreenManager):
	pass



# Designate Our .kv design file 
kv = Builder.load_file('awesome.kv')


class AwesomeApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstWindow(name='main'))
        sm.add_widget(SecondWindow(name='like'))
        sm.add_widget(ThirdWindow(name='storage'))
        sm.add_widget(FourthWindow(name='info'))
        sm.current = 'main'
        return sm
        # return kv


if __name__ == '__main__':
    
	AwesomeApp().run()