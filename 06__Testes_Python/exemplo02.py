""" 
Exemplo 02
    Como escrever o log de um arquivo
"""

import logging

logging.basicConfig(filename="exemplo02.log",
                    filemode='w',  #append ou write
                    level=logging.DEBUG)  

# logging.debug("Ola, temos arquivos...")
# logging.info("Ola, temos arquivos...")
# logging.warning("Ola, temos arquivos...")
# logging.critical("Ola, temos arquivos...")
# logging.error("Ola, temos arquivos...")
logging.log(45,"Ola, temos arquivos...")
