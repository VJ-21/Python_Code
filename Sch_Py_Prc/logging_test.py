

import logging 

logging.basicConfig(filename='test.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s') 
#specifiying the file name prints the data to the log file 


logger=logging.getLogger(__name__)


handler=logging.FileHandler('login.txt')

format=logging.Formatter('%(asctime)s:%(levelname)s:%(message)s' )

handler.setFormatter(format)
logger.addHandler(handler)

logger.info("I am writing this line so that it will add the log file")
