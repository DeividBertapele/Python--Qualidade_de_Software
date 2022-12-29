"""
Exemplo 4.
Logger 
"""

import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s:%(filename)s:%(levelname)s:%(lineno)s:%(levelname)s:%(message)s'
    
)


# Console Handler

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)

# Console Handler
fh = logging.FileHandler("exemplo04.log")
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)


logger.addHandler(ch)
logger.addHandler(fh)


logger.debug("Ola Python")