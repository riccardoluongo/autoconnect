#AutoConnect 1.1.3

import subprocess
from time import sleep
from os import system
from googleping import ping_google
from autologin import autologin
from logger import *

logging.info('Avvio del programma.')

print("AutoConnect 1.1.3 by Riccardo Luongo. \nAvvio in corso...")

sleep(1)

while True:
    ping = ping_google()

    if ping =='successful':
        print (f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")} - INF0 - Connesso ad Internet.')
        logging.info('Ping eseguito con successo.')
    
    elif ping == 'noconn':
        print(f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")} - WARNING - Nessuna connessione ad Internet. Riavvio WiFi in corso...')
        logging.warning('Nessuna connessione ad Internet. Riavvio WiFi in corso...')

        try:
            output_conn = subprocess.check_output('netsh wlan connect name=WIFI4EU', shell=True, encoding='cp850').lower()
            logging.debug(output_conn)
        except Exception as e:
            print(f'{str(e)} \nIl sistema sarà riavviato.')
            logging.fatal(f'{str(e)} \nIl sistema sarà riavviato.')
            system('shutdown -r')
            sleep(1)
            quit()

    elif ping == 'nointernet':
        print(f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")} - INFO - Login richiesto, avvio autologin...')
        logging.info('Login richiesto, avvio autologin...')
        autologin()
                
    sleep(10)

#by Riccardo Luongo, 26/08/2023