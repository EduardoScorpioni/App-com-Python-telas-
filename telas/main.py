from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, FadeTransition, WipeTransition
from kivy.lang import Builder


Builder.load_file('telas.kv')


class Tela1(Screen):
    def ir_tela2(self):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'tela2'


class Tela2(Screen):
    def voltar_tela1(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'tela1'

    def ir_tela3(self):
        self.manager.transition = FadeTransition()
        self.manager.current = 'tela3'


class Tela3(Screen):
    def voltar_tela1(self):
        self.manager.transition = WipeTransition()
        self.manager.current = 'tela1'


class GerenciadorTelas(ScreenManager):
    pass


class MeuApp(App):
    def build(self):
        return GerenciadorTelas()


if __name__ == '__main__':
    MeuApp().run()
