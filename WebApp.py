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
    
    # def build(self):
    #     # # use a (r, g, b, a) tuple
    #     # btn = Button(text ="Back",
    #     #            font_size ="20sp",
    #     #            background_color =(1, 1, 1, 1),
    #     #            color =(1, 1, 1, 1),
    #     #            size =(32, 32),
    #     #            size_hint =(.2, .2),
    #     #            pos =(300, 250))
 
    #     # # bind() use to bind the button to function callback
    #     # btn.bind(on_press = self.callback)
    #     # return btn
    
	pass

class WindowManager(ScreenManager):
	pass



# Designate Our .kv design file 
kv = Builder.load_file('awesome.kv')


class AwesomeApp(App):
#  	def build(self):
#         return FirstWindow()
# 		return kv
    def build(self):
        return FirstWindow()
        return kv
       # root = RootWidget()
        # c = CustomLayout()
        # self.theme_cls.primary_palette = "Red"
        # self.theme_cls.primary_hue = "300"

       # root.add_widget(c)
       

if __name__ == '__main__':
    
	AwesomeApp().run()