from selenium import webdriver

def before_all(context):
    context.web =  webdriver.Chrome()
   
    
def after_setp(context, step):
    pass


def after_all(context):
    context.web.quit()
    