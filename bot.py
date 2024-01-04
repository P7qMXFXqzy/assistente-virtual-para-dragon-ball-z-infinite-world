import keyboard
import scans
from tocarAudio import funcaoTocarAudio
vidaJogador = "alta"
vidaOponente = "alta"
kiJogador = "baixo"
kiOponente = "baixo"
cansadoJogador = "não"
cansadoOponente = "não"
lutaAcontecendo = "não"
#voltar os dados da luta para o valor inicial (usado quando é iniciada uma nova luta)
def resetarDados():
    global vidaJogador, vidaOponente, kiJogador, kiOponente, cansadoJogador, cansadoOponente
    vidaJogador = "alta"
    vidaOponente = "alta"
    kiJogador = "baixo"
    kiOponente = "baixo"
    cansadoJogador = "não"
    cansadoOponente = "não"

funcaoTocarAudio("iniciando...Aperte a tecla \"r\" para indicar que a luta está começando, mantenha a tecla \"r\" pressionada quando ela acabar.")
#Não finalizar até que o usuário aperte a tecla "e"
while keyboard.is_pressed("e") != True:
    #iniciar assistente se o usuário apertar a tecla "r"
    if(keyboard.is_pressed("r")):
        lutaAcontecendo = "sim"
        resetarDados()
        funcaoTocarAudio("Luta começando, ativando assistente.")
    while(lutaAcontecendo == "sim"):
        vidaJogador = scans.checarVidas("jogador", vidaJogador)
        kiJogador = scans.checarKi("jogador", kiJogador)
        cansadoJogador = scans.checarStamina("jogador", cansadoJogador)
        vidaOponente = scans.checarVidas("oponente", vidaOponente)
        kiOponente = scans.checarKi("oponente", kiOponente)
        cansadoOponente = scans.checarStamina("oponente", cansadoOponente)
        #finalizar assistente se o usuário apertar a tecla "r" novamente
        if(keyboard.is_pressed("r")):
            lutaAcontecendo = "não"
            funcaoTocarAudio("Encerrando modo assistente, aperte a tecla \"r\" novamente para ativar, aperte a tecla \"e\" para finalizar o programa.")
funcaoTocarAudio("finalizando.")