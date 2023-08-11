class Conta():
    def __init__(self, nome, agencia, contabancaria, usuario, senha):
        self.__nome = nome
        self.agencia = agencia
        self.contabancaria = contabancaria
        self.__saldo = 50
        self.usuario = usuario
        self.senha = senha

    def transfere(self, valor, contadestino):
        if self.__saldo < valor:
            print("Valor insuficiente")
        else:
            self.__saldo -= valor
            contadestino.__saldo += valor
            print(f"Valor depositado para o {contadestino.__nome.capitalize()} foi de R${valor:,.2f}")

    def saca(self, valor):
        if self.__saldo < valor:
            print("Valor insuficiente")
        else:
            self.__saldo -= valor
            print(f"Valor sacado foi de {valor:,.2f}")

    def dep(self, valor_novo):
        self.__saldo = + valor_novo

    def extrato(self):
        return f"O valor existente na conta do {self.__nome.capitalize()} é R$ {self.__saldo:,.2f}"

    def nome(self):
        return self.__nome


conta01 = Conta("joão", 1, 1, 'jjbrabo', '123')
conta02 = Conta("Roberto", 1, 2, "robertobrabo", "123")

contas = [conta01, conta02]
login = False

while True:
    # Criar conta ou logar
    print("""-------------------------------------------
        Olá seja bem vindo ao banco Deft
        Deseja fazer o login ou realizar o cadastro?
        01 - Criar conta
        02 - Logar
        03 - Sair
        -------------------------------------------""")
    rsplogin = str(input("--> "))

    if rsplogin == '1':

        print("Seja bem vindo(a), vamos precisar de algumas informações para a criação da sua conta")
        newcontanome = str(input("Digite seu nome e sobrenome:  "))
        newcontadatanc = str(input("Digite sua data de nascimento:  "))
        newcontadaus = str(input("Digite seu login:  "))
        newcontadasenha = str(input("Digite sua senha:  "))
        newcont = Conta(newcontanome, 1, 3, newcontadaus, newcontadasenha)  # implementar valor index
        contas.append(newcont)

    elif rsplogin == "2":

        logar_usuario = str(input("Digite seu login:  "))
        logar_senha = str(input("Digite sua senha:  "))
        for i in contas:
            if i.usuario == logar_usuario and i.senha == logar_senha:
                print('Login Realizado com sucesso!!')
                Contaprincipal = i  # Use the logged-in user as Contaprincipal
                login = True
                break
        else:
            print("Usuário ou senha incorreta")
    elif rsplogin == "3":
        break
    else:
        print("Opção inválida")

    # Programa ativo após login
    while login:
        print("-------------------------------------------")
        print(f"Bem-vindo(a), Sr(a) {Contaprincipal.nome()}")
        print("O que deseja fazer?")
        print("01 - Extrato bancário")
        print("02 - Transferir dinheiro")
        print("03 - Depositar dinheiro")
        print("04 - Sair")
        print("-------------------------------------------")

        rsp = str(input("--> "))

        if rsp == '1':
            print(Contaprincipal.extrato())
        elif rsp == '2':
            print("Para quem você deseja transferir?")
            for idx, conta in enumerate(contas):
                if conta != Contaprincipal:
                    print(f"{idx + 1} - {conta.nome()}")
            dest_idx = int(input("Digite o número da conta de destino: ")) - 1
            if dest_idx < 0 or dest_idx >= len(contas) or contas[dest_idx] == Contaprincipal:
                print("Conta de destino inválida.")
                continue

            dest_conta = contas[dest_idx]
            valor_transferencia = float(input("Digite o valor da transferência: "))
            Contaprincipal.transfere(valor_transferencia, dest_conta)
        elif rsp == '3':
            valor_deposito = float(input("Digite o valor a ser depositado: "))
            Contaprincipal.dep(valor_deposito)
        elif rsp == '4':
            print("Saindo da conta...")
            login = False

        elif rsp == '5':
            for cn in contas:
                print(cn.extrato())

        else:
            print("Opção inválida")

print("Obrigado por utilizar o banco Deft. Volte sempre!")

print("Hello, Welcome to Deft bank")
print("Olá, seja bem vindo ao banco do deft")
print(" 01 - PT-br / 02 - EN")

lang = int(input("--> "))

if lang == "1":
    Pt_br()
else:
    print("idioma não configurado")
