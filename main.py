
import kivy

from kivy.app import App
from kivy.uix.label import Label


kivy.require('1.9.0')

from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen







Builder.load_string(""" 
<ScreenOne>: 
	BoxLayout: 
	    orientation:"vertical"
	    TextInput:
	        id:order
	        hint_text:"enter your command"

		Button: 
			text: "Go to Screen 2"
			on_press: 
				app.calc()
		    

<ScreenTwo>: 



""")

# Create a class for all screens in which you can include
# helpful methods specific to that screen
class ScreenOne(Screen):
    pass


class ScreenTwo(Screen):
    pass



# The ScreenManager controls moving between screens
screen_manager = ScreenManager()

# Add the screens to the manager and then supply a name
# that is used to switch screens
screen_manager.add_widget(ScreenOne(name="screen_one"))
screen_manager.add_widget(ScreenTwo(name="screen_two"))



# Create the App class
class ScreenApp(App):
    fire_url="https://kivy-b934c-default-rtdb.firebaseio.com/.json"
    def build(self):
        return screen_manager

    def calc(self):
       try:
            import requests
            cmd=self.root.get_screen("screen_one").ids.order.text     
            json_data={"name":cmd}
            res=requests.patch(url=self.fire_url,json=json_data)
            self.root.get_screen("screen_one").ids.order.text=""
       except:
            pass

sample_app = ScreenApp()
sample_app.run()
