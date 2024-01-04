#не забудь импортировать необходимые элементы!
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class MainScr(Screen):
    def __init__(self, name='main'):
        super().__init__(name=name)
        layout = BoxLayout()
        v1 = BoxLayout(orientation='vertical', padding=8, spacing=8)
        txt = Label(text='Выбери экран')
        btn1 = Button(text='1')
        btn1.bind(on_press=self.switch_to_scr1)
        btn2 = Button(text='2')
        btn2.bind(on_press=self.switch_to_scr2)
        btn3 = Button(text='3')
        btn3.bind(on_press=self.switch_to_scr3)
        btn4 = Button(text='4')
        btn4.bind(on_press=self.switch_to_scr4)
        v1.add_widget(btn1)
        v1.add_widget(btn2)
        v1.add_widget(btn3)
        v1.add_widget(btn4)
        layout.add_widget(txt)
        layout.add_widget(v1)

    def switch_to_scr1(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'screen1'
    def switch_to_scr2(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'screen2'
    def switch_to_scr3(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'screen3'
    def switch_to_scr4(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'screen4'

class Screen1(Screen):
    def __init__(self, name='screen1'):
        super().__init__(name=name)
        pass
class Screen2(Screen):
    def __init__(self, name='screen2'):
        super().__init__(name=name)
        pass
class Screen3(Screen):
    def __init__(self, name='screen3'):
        super().__init__(name=name)
        pass
class Screen4(Screen):
    def __init__(self, name='screen4'):
        super().__init__(name=name)
        pass

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr(name = 'main'))
        sm.add_widget(Screen1(name = 'screen1'))
        sm.add_widget(Screen2(name = 'screen2'))
        sm.add_widget(Screen3(name = 'screen3'))
        sm.add_widget(Screen4(name = 'screen4'))
        return sm
MyApp().run()