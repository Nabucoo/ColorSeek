import questionary, time, os, random
from colorama import Back, Fore, Style, init

cores = {
    "azul": [Back.BLUE, Fore.BLUE], 
    "vermelho": [Back.RED, Fore.RED], 
    "verde": [Back.GREEN, Fore.GREEN], 
    "amarelo": [Back.YELLOW, Fore.YELLOW]
}
msg = "BEM VINDO AO COLORSEEK"
for char in msg:
    print(cores[random.choice(["azul", "vermelho", "verde", "amarelo"])][1] + char, end="")


r = questionary.select('Escolha uma opção:', choices=[
        'Jogar',
        'Sair',
    ]).ask()


if r == "Jogar":
    init(autoreset=True)

 
    sequencia = []
    nivel = 1

    while True:
        for e in range (len(sequencia)):
            os.system("cls" if os.name == "nt" else "clear")
            for _ in range(4):
                print(cores[sequencia[e]][0]+ "        " + Style.RESET_ALL)
            time.sleep(0.5) 
            os.system("cls" if os.name == "nt" else "clear")
            time.sleep(0.5)
                

        sequencia.append(random.choice(["azul", "vermelho", "verde", "amarelo"]))
        os.system("cls" if os.name == "nt" else "clear")
        for _ in range(4):
            print(cores[sequencia[-1]][0]+ "        " + Style.RESET_ALL)
        time.sleep(0.5)
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(0.5)

        for i in range(nivel):
            resposta = questionary.select("", choices=[
                "azul",
                "vermelho",
                "verde",
                "amarelo"
            ]).ask()

            if resposta != sequencia[i]:
                print(sequencia[-1] + " 😢 Errou")
                print("Seu nível final foi: {} pontos".format(nivel))
                exit()
        
        nivel += 1
        print(cores[sequencia[-1]][1] + "✔️ Correto! Voce passou para o nível {}".format(nivel))
        time.sleep(0.8)
else:
    print('Jogo finalizado')



