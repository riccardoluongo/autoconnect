import logging
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")

logging.basicConfig(filename=f'log/{dt_string}.log', filemode='w', format=f'[%(asctime)s] [%(levelname)s] -  %(message)s ', datefmt='%Y-%m-%d %H:%M:%S')
logging.getLogger().setLevel(logging.DEBUG)

#by Riccardo Luongo, 17/08/2023