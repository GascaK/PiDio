import json

import logging

class Config():
    def __init__(self):
        """ Cconfiguration file for misc PiDio objects.

        Loads and saves information to corresponding PiDio modules.
        Including radio, bluetooth, settings, USB data.

        Noteable Variables:
        ------------------------------
        logger 'l' - logging object
        Logging information at location 'PiDioApp.Config' with self.

        Error Codes -
        999: Issue occured but continue to default settings.
        -1: Critical failure, return for debug but quit upon return.
        """
        self.l = logging.getLogger('PiDioApp.Config')

    def ch_load(self):
        ''' radio_load(self)

        Returns save information for radio configuration.

        Noteable Variables:
        ------------------------------
        logger 'l' - logging object
        Logging information at location 'PidioApp.Config' with self.

        def_ch - dict object
        Default channels, used in case unable to locate credentials off file.
        Warning level log with continued application status.
        '''
        l = logging.getLogger('PiDioApp.Config.Ch_Load')
        def_ch = {'stat_one': '98.5', 'stat_two': '98.5', 'stat_three': '98.5',
                  'stat_four': '98.5', 'stat_five': '98.5', 'stat_six': '98.5',
                  'cur_stat': '98.5'}

        try:
            l.debug('Opening data.conf.') 
            # Attempt to load from data.conf file.
            with open('source/etc/data.conf') as creds:
                l.info('Opened data.conf.')
                try:
                    l.debug('Loading from config as Dict.')
                    # Returns 'Radio Info' from data.config.
                    return json.load(creds)['Radio Info']
                except KeyError as e:
                    l.warning('Unable to load or f\
                        ile is corrupted: KeyError in data.conf.')
                    l.debug(f'{e}')
                    return def_ch
        except FileNotFoundError as e:
            l.warning('Unable to locate or file is corrupted: data.conf')
            l.debug(f'{e}')
            return def_ch


if __name__ == '__main__':
    conf = Config()
    conf.ch_load()