from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen,ScreenManager,NoTransition
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyScreenManager(ScreenManager):
    def __init__(self,**kwargs):
        super(MyScreenManager,self).__init__(**kwargs)
        self.transition=NoTransition()

class MainMenu(Screen):
    pass

class MainMenuLayout(RelativeLayout):
    pass

class GameBoard(Screen):
    def __init__(self, **kwargs):
        super(GameBoard, self).__init__(**kwargs)
        self.build_board()
    def build_board(self):
        layout=GridLayout(cols=7,rows=7,spacing=10)
        for i in range(6):
            for j in range (7):
                label=Label(text="_",background_color=[1,1,1,1])
                layout.add_widget(label)
        for i in range (7):
            button_text=str(i+1)
            button=Button(text=button_text)
            layout.add_widget(button)
        self.add_widget(layout)

class ConnectFourApp(App):
    def build(self):
        screen_manager=MyScreenManager()
        screen_manager.add_widget(MainMenu(name='main'))
        screen_manager.add_widget(GameBoard(name='gameboard'))
        return screen_manager

if __name__=="__main__":
    ConnectFourApp().run()