import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout

# Configuration files #
import logging
import etc.config as conf

class PiDioGrid(Screen):
    def Radio(self):
        print('RadioScreen')

    def Bluetooth(self):
        print('BluetoothScreen')

    def AndIoPlay(self):
        print('Android/Auto/IOS')

    def Settings(self):
        print('SettingsScreen')

    def Auxillary(self):
        print('Aux Cable')

    def USB(self):
        print('USB Screen')

class RadioScreen(Screen):
    def __init__(self, **kwargs):
        super(RadioScreen, self).__init__(**kwargs)
        Config = conf.Config()
        rad = Config.ch_load()
        #logger.debug(f'Loading Radio Info: {rad}')
        self.ids.ch_one.text = rad['stat_one']
        self.ids.ch_two.text = rad['stat_two']
        self.ids.ch_three.text = rad['stat_three']
        self.ids.ch_four.text = rad['stat_four']
        self.ids.ch_five.text = rad['stat_five']
        self.ids.ch_six.text = rad['stat_six']
        self.ids.cur_stat.text = rad['cur_stat']

    def change_ch(self, station):
        self.ids.cur_stat.text = station.text
        

class PiDio(App):        

    def build(self):

        """ PiDio Main Entry Point
            Creating Logging Information with information level.

            TODO: 
            Create 'DEBUG' options, currently hardcoded in.
        """

        ''' Setup logging information

        Set up logging level and create instance of pilog.log.
        Setup log formmater as: %(asctime)s - %(name)s - %(Levelname)s - 
                %(message)s
            Formatting kept for readability and brevity.

        TODO: Setup Debugging option in gui window, currently hardcoded as
        debug level.
        '''
        logger = logging.getLogger('PiDioApp')
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler('pilog.log')
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('''%(asctime)s - %(name)s - %(levelname)s - 
                %(message)s''')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        logger.debug('Created logging information at pilog.log')

        ''' Screen Managment

        Screen Manager code, add here for more screens.
        '''
        scr_manage = ScreenManager()
        scr_manage.add_widget(PiDioGrid(name='pidio_screen'))
        scr_manage.add_widget(RadioScreen(name='radio_screen'))
        return scr_manage

if __name__ == '__main__':
    PiDio().run()