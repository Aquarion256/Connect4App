from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen,ScreenManager,NoTransition
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder

class MyScreenManager(ScreenManager):
    def __init__(self,**kwargs):
        super(MyScreenManager,self).__init__(**kwargs)
        self.transition=NoTransition()

class MainMenu(Screen):
    pass

class WinScreen1(Screen):
    def playagain(self,instance):
        App.get_running_app().stop()
        ConnectFourApp().run()
    
    def endapp(self,instance):
        App.get_running_app().stop()

class WinScreen2(Screen):
    def playagain(self,instance):
        App.get_running_app().stop()
        ConnectFourApp().run()
    
    def endapp(self,instance):
        App.get_running_app().stop()

class DrawScreen(Screen):
    def playagain(self,instance):
        App.get_running_app().stop()
        ConnectFourApp().run()
    
    def endapp(self,instance):
        App.get_running_app().stop()

class MainMenuLayout(RelativeLayout):
    def endapp(self,instance):
        App.get_running_app().stop()



class GameBoard(Screen):
    player=1
    r_check=-1
    c_check=-1
    p1_tok='X'
    p2_tok='O'
    def __init__(self, **kwargs):
        super(GameBoard, self).__init__(**kwargs)
        self.build_board()
    def build_board(self):
        self.label_list=[[],[],[],[],[],[],[]]
        self.button_list=[]
        self.pointer=[5,5,5,5,5,5,5]
        self.layout=GridLayout(cols=7,spacing=10,padding=10)
        for i in range(6):
            for j in range (7):
                self.label_text="[size=40][b]_[/b][/size]"
                label=Label(markup=True,text=self.label_text)
                self.layout.add_widget(label)
                self.label_list[j].append(label)
        for i in range (7):
            button_text=str(i+1)
            button=Button(background_normal='',
                      background_color=(0.7,1,0,1),
                      font_size='25sp',
                      color=(0,0,0,1),
                      bold=True,
                      markup=True,
                      text=f"{button_text}")
            button.bind(on_press=lambda instance:self.play_move(instance))
            self.button_list.append(button)
            self.layout.add_widget(button)
        
        self.player_label=Label(markup=True,text="Current Player is [b][color=#FF0000]X[/color][/b]")
        self.layout.add_widget(self.player_label)

        label=Label(text=" ")
        self.layout.add_widget(label)

        self.last_move_label=Label(text="Last Move Played: nil")
        self.layout.add_widget(self.last_move_label)
        self.add_widget(self.layout)

        label=Label(text=" ")
        self.layout.add_widget(label)
    
    def play_move(self,instance):
        i=int(instance.text)-1
        self.last_move_label.text=f"Last Move Played: {instance.text}"
        label=self.label_list[i]
        positon=self.pointer[i]
        if self.player==1 and label[positon].text==self.label_text:
            label[positon].text=self.p1_tok
            label[positon].color=(1,0,0,1)
            label[positon].bold=True
            label[positon].font_size=50
            self.player=2
            self.player_label.text="Current Player is [b][color=#FFFF00]O[/color][/b]"
        elif self.player==2 and label[positon].text==self.label_text:
            label[positon].text=self.p2_tok
            label[positon].color=(1,1,0,1)
            label[positon].bold=True
            label[positon].font_size=50
            self.player=1
            self.player_label.text="Current Player is [b][color=#FF0000]X[/color][/b]"
        if(self.pointer[i]==-1):
            pass
        else:
            r_check=positon
            c_check=i
            self.pointer[i]-=1
            self.check_win(r_check,c_check,self.player)
        
    def check_win(self,r,c,p):
        if(p==2):
            tok='X'
        else:
            tok='O'
        #horizontal
        t_col=c+1
        count=0
        while t_col<7 and self.label_list[t_col][r].text==tok:
            count+=1
            t_col+=1
        t_col=c-1
        while t_col>=0 and self.label_list[t_col][r].text==tok:
            count+=1
            t_col-=1
        if(count>=3):
            self.WinnerCheck(tok)
        
        #vertical 
        t_row=r+1
        count=0
        while t_row<6 and self.label_list[c][t_row].text==tok:
            count+=1
            t_row+=1
        t_row=r-1
        while t_row>=0 and self.label_list[c][t_row].text==tok:
            count+=1
            t_row-=1
        if(count>=3):
            self.WinnerCheck(tok)

        #first_diagonal
        t_row=r+1
        t_col=c+1
        count=0
        while t_row<6 and t_col<7 and self.label_list[t_col][t_row].text==tok:
            count+=1
            t_row+=1
            t_col+=1
        t_row=r-1
        t_col=c-1
        while t_row>=0 and t_col>=0 and self.label_list[t_col][t_row].text==tok:
            count+=1
            t_row-=1
            t_col-=1
        if(count>=3):
            self.WinnerCheck(tok)

        #second_diagonal
        t_row=r-1
        t_col=c+1
        count=0
        while t_row>=0 and t_col<7 and self.label_list[t_col][t_row].text==tok:
            count+=1
            t_row-=1
            t_col+=1
        t_row=r+1
        t_col=c-1
        while t_row<6 and t_col>=0 and self.label_list[t_col][t_row].text==tok:
            count+=1
            t_row+=1
            t_col-=1
        if(count>=3):
            self.WinnerCheck(tok)

        count=0
        for i in range(6):
            for j in range(7):
                if(self.label_list[j][i].text==self.label_text):
                    return
                else:
                    count+=1
                    print(count,)
        if(count==42):
            self.WinnerCheck('Y')

    def WinnerCheck(self,tok):
        for button in self.button_list:
            self.layout.remove_widget(button)
        button=Button(background_normal='',
                      background_color=(.7,1,0,1),
                      markup=True,
                      text="[b][size=20][color=#000000]Continue?[/color][/size][/b]")
        button.bind(on_press=lambda instance: self.winner_screener(instance,tok))
        self.layout.add_widget(button)

    def winner_screener(self,instance,tok):
        app=App.get_running_app()
        if(tok=='X'):
            app.root.current='winner1'
        elif(tok=='O'):
            app.root.current='winner2'
        else:
            app.root.current='drawscreen'


class ConnectFourApp(App):
    def build(self):
        Builder.load_file('ConnectFour.kv')
        self.icon="logo.png"
        screen_manager=MyScreenManager()
        screen_manager.add_widget(MainMenu(name='main'))
        screen_manager.add_widget(GameBoard(name='gameboard'))
        screen_manager.add_widget(WinScreen1(name='winner1'))
        screen_manager.add_widget(WinScreen2(name='winner2'))
        screen_manager.add_widget(DrawScreen(name='drawscreen'))
        return screen_manager

if __name__=="__main__":
    ConnectFourApp().run()
