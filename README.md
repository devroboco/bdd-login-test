# Projeto de Testes Automatizados com BDD

## Contexto

Este projeto tem como objetivo testar a funcionalidade de login de uma aplicação web. O foco é garantir que usuários possam acessar áreas restritas com credenciais válidas e que erros sejam tratados adequadamente ao tentarem acessar com credenciais inválidas.

## Cenários de Teste

### Funcionalidade: Login

- **Cenário 1: Login com credenciais válidas**

  - **Dado** que o usuário está na página de login
  - **Quando** o usuário insere "tomsmith" como username e "SuperSecretPassword!" como password
  - **Então** uma mensagem de sucesso "You logged into a secure area!" deve ser exibida

- **Cenário 2: Login com credenciais inválidas**
  - **Dado** que o usuário está na página de login
  - **Quando** o usuário insere "invalid_user" e "invalid_password"
  - **Então** uma mensagem de erro "Your username is invalid!" deve ser exibida

## Importância do BDD

O uso de Behavior-Driven Development (BDD) é crucial neste contexto, pois:

1. **Alinha as expectativas**: BDD facilita a comunicação entre desenvolvedores, testadores e stakeholders, garantindo que todos compreendam os requisitos do sistema.

2. **Documentação acessível**: Os cenários de teste funcionam como uma documentação clara e viva, refletindo o comportamento esperado da aplicação.

3. **Melhoria contínua**: O BDD promove um ciclo de feedback rápido, permitindo ajustes ágeis e aumentando a qualidade do software.

## Conclusão

Implementar BDD em testes de login não só melhora a qualidade do sistema, mas também assegura que as necessidades dos usuários sejam atendidas de maneira eficaz.
