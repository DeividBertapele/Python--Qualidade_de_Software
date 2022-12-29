import logging
import logging.config


logging.config.fileConfig('simple_loggin.ini')


logger = logging.getLogger('root')


logger.info('oi bb')