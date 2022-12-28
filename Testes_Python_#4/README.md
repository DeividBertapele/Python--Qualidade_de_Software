# Análise estática de código (linters)

    - O que são linters?
        - É uma ferramenta de análise de código estática. Ele é realizado para sinalizar erros de programação, erros estilísticos, bugs e construções suspeitas que possam prejudicar ou causar o baixo desempenho ao código da aplicação.

    - Com tantas opções, o que fazer?
        - Pylama (junção de linters todos juntos e misturados) -> 1x por semana para usar esta ferramenta

    - Modo texto ou real time?
        - para qualquer editores que tem plugins de lintagem, você pode instalar eles no seu editor e o
        código vai ficar colorido e apontar os erros.


    - Ferramentas....
        - Pylama - pip install pylama==1.4.0 (https://pypi.org/project/pylama/1.4.0/)
        - Pylint - pip install pylint (https://pypi.org/project/pylint/)
        - pycodestyle - pip install pycodestyle (https://pypi.org/project/pycodestyle/)
        - pydocstyle - pip install pydocstyle (http://www.pydocstyle.org/en/stable/)


    - Codes:
       - PEP-8
       - PEP-257

=================================================================

Comandos Básicos => se tiver instalado (pydocstyle)

 - pydocstyle teste.py

 - 


---------------------------------------------------------------------------

- Para conhecer os erros:
    - Errors do pycodestyles:
        - https://pycodestyle.pycqa.org/en/latest/intro.html#error-codes
        
    - Errors do pydocstyles:
        - http://www.pydocstyle.org/en/stable/error_codes.html