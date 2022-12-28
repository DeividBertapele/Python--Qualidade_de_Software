# language:pt


Funcionalidade: Cadastro
    Cenário: Efetuar cadastro com sucesso
    Dado que o usuario esteja na pagina "http://localhost:8080"
    Quando inserir o "nome" "Python"
    E inserir o "sobrenome" "Rossum"
    E inserir o "usuario" "PythonRossum"
    E inserir o "sexo" "Masculino"
    E inserir o "senha" "123"
    E inserir o "email" "python@teste.com.br"
    E inserir o "nascimento" "20/02/1991"
    Então clicar no botão "Enviar"
    E a mensagem deverá ser exibida
    """
    Bem vindo Python
    Usuário: PythonRossum
    Senha: 123
    """


    Cenário: Efetuar cadastro com senha inválida
    Dado que o usuario esteja na pagina "http://localhost:8080"
    Quando inserir o "nome" "Python"
    E inserir o "sobrenome" "Rossum"
    E inserir o "usuario" "PythonRossum"
    E inserir o "sexo" "Masculino"
    E inserir o "senha" "123"
    E inserir o "email" "python@teste.com.br"
    E inserir o "nascimento" "20/02/1991"
    Então clicar no botão "Enviar"
    E a mensagem deverá ser exibida
    """
    Senha inválida, use ao menos 6 caracteres
    """