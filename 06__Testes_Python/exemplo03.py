"""
Exemplo 3.
Como personalizar o log
"""
import logging

log_format = '%(asctime)s:%(filename)s:%(levelname)s:%(message)s'

logging.basicConfig(filename='exemplo_3.log',
                    level=logging.DEBUG,
                    format=log_format)

logger = logging.getLogger()

logger.info('Ola Python')
logger.debug('Hoje a noite')
logger.critical('com vinho...')