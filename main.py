import questionary, time, os, random
from colorama import Back, Style, init
print("BEM VINDO AO COLORSEEK")

r = questionary.select('Escolha uma opção:', choices=[
        'Jogar',
        'Sair',
    ]).ask()


if r == "Jogar":
    init()
    cores = {
        "azul": Back.BLUE, 
        "vermelho": Back.RED, 
        "verde": Back.GREEN, 
        "amarelo": Back.YELLOW
    }

    sequencia = []
    nivel = 1

    while True:
        for i in range(nivel):
            sequencia.append(random.choice(["azul", "vermelho", "verde", "amarelo"]))
            os.system("cls" if os.name == "nt" else "clear")
            print(cores[sequencia[-1]]+ "        " + Style.RESET_ALL)
            time.sleep(2)
            os.system("cls" if os.name == "nt" else "clear")
            time.sleep(1)

        for i in range(nivel):
            resposta = questionary.select("", choices=[
                "azul",
                "vermelho",
                "verde",
                "amarelo"
            ]).ask()

            if resposta != sequencia[i]:
                print("errou")
                print("Seu nível final foi: {} pontos".format(nivel))
                exit()
        
        nivel += 1
        print("Voce passou para o nível {}".format(nivel))
        time.sleep(2)
else:
    print('Jogo finalizado')

