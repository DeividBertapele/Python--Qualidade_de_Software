from behave import given, when, then
from selenium.webdriver.common.by import By


@given(u'que acesso a pagina do Google')
def step_impl(context):
    context.web.get("https://www.google.com.br/")


@when(u'realizo uma pesquisa')
def step_impl(context):
    context.element = context.web.find_element(By.NAME,"q")
    context.element.click()
    context.element.send_keys("Python")
    context.element.submit()


@when(u'pesquisa e realiza')
def step_impl(context):
    assert context.web.title == "Python - Pesquisa Google"


@then(u'o titulo da pagina deve ser validado')
def step_impl(context):
    pass