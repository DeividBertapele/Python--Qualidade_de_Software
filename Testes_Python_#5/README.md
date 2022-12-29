# Testes de mutação -> mutpy

- Teste de mutação
    - É uma técnica baseada em defeitos, para trocar operadores, assignment e vai modificar o seu código e seus testes para ver como eles reagem a isso.

    - Tem uma técnica chama AOR (arithmetic operator replacement) ou 
    Substituição de operador aritmético

    - Objetivo é ajudar nos escrever código melhor , testes melhres e vai apontar as falhas no 
    desenvolvimento baseado nos testes de escrevemos. Isso se usarmos técnicas de mutação misturadas e
    vamos ter um grande campo de correções e "defeitos"



- Tipos de mutação (Aritméticas)
    - AOD (arithmetic operator deletion)
    - AOR (arithmetic operator replacement)


Link - Mutpy
    - https://pypi.org/project/MutPy/0.3.0/

===========================================================
Comandos básicos no terminal no mesmo diretório:

--> mut.py --target calculator --unit-test test_calculator -m


=====================================================================================

- --target- após este sinalizador devemos passar o módulo que queremos mutar.
- --unit-test- este sinalizador aponta para o nosso módulo de testes de unidade.

======================================================================================

# List of MutPy mutation operators:

AOD - arithmetic operator deletion
AOR - arithmetic operator replacement
ASR - assignment operator replacement
BCR - break continue replacement
COD - conditional operator deletion
COI - conditional operator insertion
CRP - constant replacement
DDL - decorator deletion
EHD - exception handler deletion
EXS - exception swallowing
IHD - hiding variable deletion
IOD - overriding method deletion
IOP - overridden method calling position change
LCR - logical connector replacement
LOD - logical operator deletion
LOR - logical operator replacement
ROR - relational operator replacement
SCD - super calling deletion
SCI - super calling insert
SIR - slice index remove
Experimental mutation operators:

CDI - classmethod decorator insertion
OIL - one iteration loop
RIL - reverse iteration loop
SDI - staticmethod decorator insertion
SDL - statement deletion
SVD - self variable deletion
ZIL - zero iteration loop