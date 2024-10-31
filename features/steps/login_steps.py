from behave import given, when, then
from selenium.webdriver.common.by import By
import time

@given('que o usuário está na página de login')
def step_user_on_login_page(context):
    context.driver.get('https://the-internet.herokuapp.com/login')
    time.sleep(2)  # Espera carregar a página

@when('o usuário preenche o campo username com "{username}" e o campo password com "{password}"')
def step_user_enters_credentials(context, username, password):
    # Localiza e preenche os campos de username e password
    context.driver.find_element(By.ID, 'username').send_keys(username)
    context.driver.find_element(By.ID, 'password').send_keys(password)

@when('o usuário clica no botão de login')
def step_user_clicks_login_button(context):
    context.driver.find_element(By.CSS_SELECTOR, 'button.radius').click()  # Clica no botão de login
    time.sleep(2)  # Aguarda a resposta do servidor

@then('uma mensagem de sucesso "{mensagem}" deve ser exibida')
def step_success_message_displayed(context, mensagem):
    # Verifica se a mensagem de sucesso é exibida
    success_message = context.driver.find_element(By.ID, 'flash').text
    assert mensagem in success_message, f'Mensagem esperada: "{mensagem}", mas foi exibido: "{success_message}"'

@then('uma mensagem de erro "{mensagem}" deve ser exibida')
def step_error_message_displayed(context, mensagem):
    # Verifica se a mensagem de erro é exibida
    error_message = context.driver.find_element(By.ID, 'flash').text
    assert mensagem in error_message, f'Mensagem esperada: "{mensagem}", mas foi exibido: "{error_message}"'
