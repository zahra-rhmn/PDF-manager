from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserListView
from os.path import sep, expanduser, isdir, dirname
from kivy.garden.filebrowser import FileBrowser
from kivy.uix.screenmanager import ScreenManager, Screen
from functools import partial

class BrowseLayout(Screen):
    def __init__(self, **kwargs):
        super (BrowseLayout, self).__init__(**kwargs)
        user_path = dirname(expanduser('~')) + sep + 'Documents'
        
        
        browser = FileBrowser(select_string='Select',
                              favorites=[(user_path, 'Documents')])
        browser.bind(
                    on_success=self._fbrowser_success,
                    on_canceled=self._fbrowser_canceled)
        
        self.add_widget(browser)
        
    def _fbrowser_canceled(self, instance):
        print 'cancelled, Close self.'
        sm.current = 'thisMain'
        

    def _fbrowser_success(self, instance):
        print instance.selection[0]
        sm.get_screen('thisMain').glayout.addressTXTField.textField.text = instance.selection[0]
        sm.current = 'thisMain'

class GridField (BoxLayout):
    def __init__(self, **kwargs):
        super (GridField, self).__init__(**kwargs)
        self.orientation='horizontal'
        self.spacing = 3
        self.textField = TextInput(multiline=False, size_hint=(1, 1))
        self.add_widget(self.textField)
        self.browse = Button(text = "...", size_hint=(0.2, 1))
        self.add_widget(self.browse)

class NewPDFLayout (GridLayout):
        
    def __init__(self, **kwargs):

        super (NewPDFLayout, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Name: ",size_hint_x=0.2))
        self.nameTXTField = TextInput(multiline=False, size_hint_x=0.8)
        self.add_widget(self.nameTXTField)

        self.add_widget(Label(text="Address: ",size_hint_x=0.2))
        self.addressTXTField = GridField()
        self.addressTXTField.browse.bind(on_release=load)
        self.addressTXTField.size_hint_x = 0.8
        self.add_widget(self.addressTXTField)
        
        self.add_widget(Label(text="Subjects: ",size_hint_x=0.2))
        self.subjectsTXTField = GridField()
        self.subjectsTXTField.browse.bind(on_release=helloworld)
        self.subjectsTXTField.size_hint_x = 0.8
        self.add_widget(self.subjectsTXTField)

        self.add_widget(Label(text="Tags: ",size_hint_x=0.2))
        self.tagsTXTField = GridField()
        self.tagsTXTField.browse.bind(on_release=helloworld)
        self.tagsTXTField.size_hint_x = 0.8
        self.add_widget(self.tagsTXTField)

        self.add_widget(Label(text="",size_hint=(0.2,0.8)))
        self.Buttons = BoxLayout(orientation='horizontal',spacing = 3,size_hint=(0.8,0.8))
        self.Buttons.add_widget(Label(size_hint=(0.5,0.8)))
        self.Buttons.okButton = Button(text = "OK", size_hint=(0.2,0.8))
        self.Buttons.okButton.bind(on_release=helloworld)
        self.Buttons.CancelButton = Button(text = "Cancel", size_hint=(0.2,0.8))
        self.Buttons.CancelButton.bind(on_release=helloworld)
        self.Buttons.add_widget(self.Buttons.CancelButton)
        self.Buttons.add_widget(self.Buttons.okButton)
        self.add_widget(self.Buttons)

class NewPDFScreen(Screen):
    def __init__(self, **kwargs):
        super (NewPDFScreen, self).__init__(**kwargs)
        self.glayout = NewPDFLayout()
        self.add_widget(self.glayout)

def helloworld(instance):
    print ("helloworld")

def load(ins):
    sm.current = 'browse'

def newPDFMain():
    global sm
    sm = ScreenManager()
    brs = BrowseLayout(name='browse')
    sm.add_widget(brs)
    thisMain = NewPDFScreen(name='thisMain')
    sm.add_widget(thisMain)

    sm.current = "thisMain"
        
class NewPDFApp(App):
    title = 'Add New PDF'
    newPDFMain()
    def build (self):
        return sm

if __name__ == '__main__':
    NewPDFApp().run()

