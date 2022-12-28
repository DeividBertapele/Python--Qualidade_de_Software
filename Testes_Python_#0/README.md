# Introdução a qualidade de software - Python - (Testes de Software)

- Introdução a qualidade de software:

    - Necessidades do desenvolvimento de software
        - Entregas frequentes ( Chrome e Firefox )

    - Garantir o funcionamento básico do software (regressão)
        - Regressão
        - Garantir que tudo está funcionando, permanece funcionando nas novas versões

    - Manter a qualidade da aplicação e do código
        - Fácil de manutenção
        - Fácil de testar
        - Integração contínua

    - Métricas de qualidade do código (análise estática)
        - Débito técnico
            -> Reflete o custo de retrabalho por ter escolhido uma solução fácil
        - Cobertura do código (code coverage) 
            -> É a medida usada para descrever o quanto código fonde de um programa é exercitado, quando é executado nos testes.
            - Statement Coverage 
            - Branch Coverage 
     
        - Acoplamento
            - Grau de dependência (classe, objeto, framework etc)
            - Acoplamento fraco ou baixo
            - Acoplamento forte ou alto
            * Pode dificultar a criação de testes e aumenta o tempo de desenvolvimento de manutenção e novas funcionalidades (Alto acoplamento se torna código dificil de entender)
        
        - Coesão 
            - Princípio de responsabilidade única
            - Baixa coesão signifca que o componente possui responsabilidades
            - Dificuldade em dar manutenção e reuso de componentes


        - Manutenibilidade de software
            - Facilidade e segurança em efetuar correções ou novas implementações no software
            - Linhas de código
            - Custo de correção x custo de desenvolvimento
            - Alto coesão
            - Baixo acoplamento
            - Cobertura de código
            
            - PEP-8 
                - https://peps.python.org/pep-0008/
            
            - PEP-257 
                - https://peps.python.org/pep-0257/


** Qualidade de Software é a capacidade de atender/resolver o problema do cliente de forma a otimizar o trabalho

============================================================================================
- Guias de estilo e padronização de código:

    - PEP-8: 
        - Não importar dois módulos na mesma linda

        - A ordem dois imports importa, SIM
            - Primeiro __future__
            - Depois a bibliotecas padrão
            - Bibliotecas de terceiros
            - Suas bibliotecas

        - Não se deve importar usando wildcard (*)
        - Imports não devem substituir módulos builtin

        - Tamanho de linhas:
            - Toda linha de código deve ter no máximo de 80 caracteres
            - Para PEP, alguns usam 100 caracteres, porém o número de caracteres em comentários será mantido em 72 caracteres (Docstrings e comentários)
        
        - Identação:
            - Todo bloco deve ser definido com 4 espaços
            - Agrupamento como listas, tuplas, dicionários, etc...

        - Espaços em branco
            - Evite espaço em branco de qualquer maneira

    - PEP-3107: Anotações de funções
        - Anotações de funçÕes são completamente opcionais

