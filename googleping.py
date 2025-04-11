import subprocess
from logger import logging

def ping_google():
    try:
        comando = 'ping google.com -n 1'
        output = subprocess.check_output(comando, shell=True, encoding='cp850')
        output = output.lower()
        logging.debug(output)
    except:
        output = "noconn"
        pass
    if 'unreachable' in output:
        return 'nointernet'
    elif 'time' in output:
        return 'successful'
    else:
        return 'noconn'

#by Riccardo Luongo, 18/08/2023