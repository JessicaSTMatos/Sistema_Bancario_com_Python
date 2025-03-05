# 💰 Sistema Bancário

Este é um sistema bancário simples desenvolvido em Python. O projeto permite a criação de usuários, abertura de contas bancárias, realização de depósitos, saques e exibição de extratos.

## 📌 Funcionalidades

- 👤 **Cadastro de Usuários**: Registra usuários no sistema com nome, CPF e endereço.
- 🏦 **Criação de Contas**: Cada usuário pode ter uma conta associada.
- 💰 **Depósitos**: Adiciona saldo à conta do usuário.
- 💸 **Saques**: Permite a retirada de dinheiro, respeitando limites estabelecidos.
- 📜 **Extrato**: Exibe um histórico das transações da conta.
- 📝 **Listagem de Contas**: Mostra todas as contas cadastradas.

## 🛠️ Tecnologias Utilizadas

- 🐍 Python 3
- 📅 datetime (para registros de transações)
- 📝 textwrap (para formatar a saída do menu)

## 🚀 Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/JessicaSTMatos/Sistema_Bancario_com_Python.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd sistema-bancario
   ```
3. Execute o script principal:
   ```bash
   python sistema_bancario.py
   ```

## 🏦 Fluxo do Sistema

1. O sistema exibe um menu com as opções disponíveis.
2. O usuário escolhe a opção desejada digitando o número correspondente.
3. Para criar uma conta, é necessário ter um usuário cadastrado previamente.
4. Os depósitos e saques devem respeitar os limites diários.
5. O extrato pode ser visualizado a qualquer momento.

## 📌 Menu de Opções

```
===== MENU =====
[0] Depositar 💰
[1] Sacar 💸
[2] Extrato 📜
[3] Novo usuário 👤
[4] Nova conta 🏦
[5] Listar contas 📋
[6] Sair 🚪
```

## 🔍 Exemplo de Uso

```bash
Informe o CPF (somente números): 12345678900
Informe o nome: João Silva
Informe a data de nascimento (DD/MM/AAAA): 15/06/1985
Informe o logradouro do endereço: Rua das Flores
Informe o número do endereço: 123
Informe o bairro: Centro
Informe a cidade: São Paulo
Informe o estado UF: SP

✅ Usuário cadastrado com sucesso!
```

## 📜 Licença

Este projeto é de uso livre para estudos e aprimoramento. 😊

