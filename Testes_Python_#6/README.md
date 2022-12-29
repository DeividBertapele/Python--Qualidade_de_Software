# LOGS

- Link:   https://docs.python.org/pt-br/3/howto/logging.html

-------------------------------------------------------------------------------------

- O Log é um meio de rastrear eventos que acontecem quando algum software é executado.
- Lembrando a importância quando você quer saber de algo e coloca um monte de prints.
- Fornecem uma explicação simples de algum evento "qualquer no sistema".

- Níveis do logger:
    - Debug
        - Informações detalhadas, quando estamos buscando problemas.
    
    - Info
        - Confirmar que as coisas estão funcionando como esperado.
    
    - Warning
        - Algo inesperado aconteceu e funcionando bem.
    
    - Error
        - Quando algo inesperado ocorre e o programa não consegue executar algo.
    
    - Critical
        - Um erro grave que impediu o sistema de executar algo.

-------------------------------------------------------------------------------------

- Personalizando o log

    - %(asctime)s  -> Mostra a hora do log
    - %(filename)s -> Arquivo que a chamada foi feita
    - %(levelname)s -> Nível do log
    - %(message)s -> Mensagem logada

-------------------------------------------------------------------------------------