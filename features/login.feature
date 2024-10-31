# language: pt
Funcionalidade: Login
    Como usuário
    Quero fazer login na aplicação
    Para que eu possa acessar áreas seguras

Cenário: Login com credenciais válidas
    Dado que o usuário está na página de login
    Quando o usuário preenche o campo username com "tomsmith" e o campo password com "SuperSecretPassword!"
    E o usuário clica no botão de login
    Então uma mensagem de sucesso "You logged into a secure area!" deve ser exibida

Cenário: Login com credenciais inválidas
    Dado que o usuário está na página de login
    Quando o usuário preenche o campo username com "invalid_user" e o campo password com "invalid_password"
    E o usuário clica no botão de login
    Então uma mensagem de erro "Your username is invalid!" deve ser exibida
