from datetime import datetime  

def dataHora():
    day = int(input("Digite o dia: "))
    month = int(input("Digite o mês: "))
    year = int(input("Digite o ano: "))
    hour = int(input("Digite a hora (formato 24 horas): "))
    minute = int(input("Digite o minuto: "))
    return datetime(year, month, day, hour, minute)

def alugarBicicleta(userCredits, bikeValue, userSelectedCredits):
    if userCredits >= bikeValue:
        userCredits -= userSelectedCredits
        print("Bicicleta alugada com sucesso!")
        rentTime = dataHora()
        print(f"Data e hora da retirada da bicicleta: {rentTime.strftime('%d/%m/%Y %H:%M')}")
        print(f"Você tem {userSelectedCredits} horas para utilizar essa bicicleta e devolvê-la. (Se você passar do tempo, será cobrado um crédito por hora adicional)")
        return userCredits, rentTime
    else:
        print("Você não tem créditos suficientes para alugar uma bicicleta.")
        return userCredits

def devolverBicicleta(userCredits, rentTime, userSelectedCredits):
    if rentTime != 0:
        returnTime = dataHora()
        print("Bicicleta devolvida com sucesso!")
        print(f"Data e hora da devolução da bicicleta: {returnTime.strftime('%d/%m/%Y %H:%M')}")

        tempoUso = (returnTime - rentTime).total_seconds() / 3600
        extraHours = tempoUso - userSelectedCredits

        if extraHours > 0:
            userCredits -= extraHours
            print(f"Você usou a bicicleta por {tempoUso} horas. Como você passou {extraHours} horas do tempo, {extraHours} créditos foram subtraídos. Você agora tem {userCredits} créditos.")
        else:
            print(f"Você usou a bicicleta por {tempoUso} horas e devolveu dentro do prazo.")
    else:
        print("Você não alugou nenhuma bicicleta.")
    return userCredits

userPassword = "senha123"
bikeValue = 5

while True:
    entry = input("Bem-Vindo ao Bikepy. Insira seu login (Apenas seu nome): ")
    if entry.isalpha():
        incorrectAttempts = 0 
        remainingAttempts = 3
        while True:
            password = input("Digite a senha ou 1 para ir à tela inicial:")
            if password == userPassword:
                print(f"Bem-vindo {entry}!")
                userCredits = int(input("Digite a quantidade inicial de créditos (Cada crédito permite o uso da bicicleta por uma hora): "))
                break
            elif password == "1":
                break
            else:
                incorrectAttempts += 1
                remainingAttempts -= 1
                if incorrectAttempts >= 3:
                    print("Você excedeu o número máximo de tentativas. Encerrando o sistema por motivos de segurança, tente novamente mais tarde.")
                    exit()
                print(f"Sua senha é inválida. Você possui mais {remainingAttempts} tentativas, digite a senha correta ou 1 para ir à tela inicial: ")

        if password == userPassword:
            relatório = ["Relatório de ações:"]
            rentTime = 0
            userSelectedCredits = 0 
            while True:
                print("Escolha algumas das opções abaixo:")
                print("1 - Visualizar número de créditos")
                print("2 - Comprar mais créditos")
                print("3 - Alugar bicicleta")
                print("4 - Devolver bicicleta")
                print("5 - Visualizar relatório de ações")
                print("6 - Encerrar o programa")
                optionsMenu = input("Digite a opção desejada: ")

                if optionsMenu == "1":
                    relatório.append(optionsMenu + " - Visualizar número de créditos")
                    print(f"Você possui {userCredits} créditos.")
                    seeMenu= input('Pressione qualquer tecla para ver o menu novamente: ')
                    if seeMenu == '':
                        continue
                elif optionsMenu == "2":
                    relatório.append(optionsMenu + " - Comprar mais créditos")
                    addCredits = int(input("Digite quantos créditos você deseja comprar:"))
                    userCredits += addCredits
                    print('Créditos adicionados com sucesso!')
                    seeMenu= input('Pressione qualquer tecla para ver o menu novamente: ')
                    if seeMenu == '':
                        continue
                elif optionsMenu == "3":
                    if rentTime == 0:
                        userSelectedCredits = int(input("Digite quantos créditos você deseja utilizar para alugar a bicicleta (Você precisa de no mínimo 5 créditos para alugar a bicicleta): "))
                        relatório.append(optionsMenu + " - Alugar bicicleta")
                        userCredits, rentTime = alugarBicicleta(userCredits, bikeValue, userSelectedCredits)
                    else:
                        print("Você já possui uma bicicleta alugada. Devolva a bicicleta antes de alugar outra.")
                    seeMenu= input('Pressione qualquer tecla para ver o menu novamente: ')
                    if seeMenu == '':
                        continue
                elif optionsMenu == "4":
                    relatório.append(optionsMenu + " - Devolver bicicleta")
                    userCredits = devolverBicicleta(userCredits, rentTime, userSelectedCredits)
                    rentTime = 0
                    seeMenu= input('Pressione qualquer tecla para ver o menu novamente: ')
                    if seeMenu == '':
                        continue
                elif optionsMenu == "5":
                    print(relatório)
                    seeMenu= input('Pressione qualquer tecla para ver o menu novamente: ')
                    if seeMenu == '':
                        continue
                elif optionsMenu == "6":
                    print("Encerrando o programa. Volte sempre!")
                    exit()
                else: 
                    print("Opção inválida. Tente novamente.")
                    continue
    else:
        print("Entrada inválida. Tente novamente.")