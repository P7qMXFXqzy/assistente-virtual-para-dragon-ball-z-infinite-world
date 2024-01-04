from pyautogui import pixel
from tocarAudio import funcaoTocarAudio
#é feito 2 escaneamentos para garantir que o escaneamento seja executado eficientemente
#Checar a vida do alvo escolhido (jogador ou oponente), tocar uma mensagem caso a condição da vida tenha mudado.
def checarVidas(alvo, valorInserido):
    valorAtual = valorInserido
    mensagem = None
    localVida = None
    #definir qual barra de vida será escaneada
    if(alvo == "jogador"): localVida = [203, 62]        
    else: localVida = [1162, 62]
    #salvar os números de azul e verde do pixel escolhido
    pixelRgbAzul = pixel(localVida[0], localVida[1])[2]
    pixelRgbVerde = pixel(localVida[0], localVida[1])[1]
    #vida branca (alta)
    if((pixelRgbAzul >= 176 and pixelRgbAzul <= 186) and (pixelRgbVerde >= 175 and pixelRgbVerde <= 185)): valorAtual = "alta"
    #vida verde (média)
    elif((pixelRgbAzul >= 19 and pixelRgbAzul <= 29) and (pixelRgbVerde >= 175 and pixelRgbVerde <= 185)): valorAtual = "média"
    #vida laranja (baixa)
    elif((pixelRgbAzul >= 0 and pixelRgbAzul <= 5) and (pixelRgbVerde >= 97 and pixelRgbVerde <= 107)): valorAtual = "baixa"
    #tocar uma mensagem caso a vida tenha diminuído ou aumentado (ou seja, diferente do valor anterior)
    if(valorAtual != valorInserido):
        if(valorAtual == "alta"):
            if(alvo == "jogador"): mensagem = "Sua vida está alta, ataque agressivamente."
            else: mensagem = "A vida do seu oponente está cheia novamente."
        elif(valorAtual == "média"):
            if(alvo == "jogador"): mensagem = "Sua vida está média, Espere o oponente abrir a defesa para atacar."
            else: mensagem = "A vida do seu oponente está média, mantenha-se na estratégia atual."
        else:
            if(alvo == "jogador"): mensagem = "Sua vida está baixa, fique na defensiva e ataque apenas com aura burn, use uma capsula de restauração de vida se possível."    
            else: mensagem = "Seu oponente está com a vida baixa, ative o aura burn assim que possível e ataque agressivamente."
        funcaoTocarAudio(mensagem)
    return valorAtual
#checar a quantidade de ki dos jogadores
def checarKi(alvo, valorInserido):
    valorAtual = valorInserido
    mensagem = None
    localKi = None 
    if(alvo == "jogador"): localKi = [192, 101]
    else: localKi = [1174, 101]
    #salvar valores rgb vermelho e verde do pixel analisado
    pixelRgbVermelho = pixel(localKi[0], localKi[1])[0]
    pixelRgbVerde = pixel(localKi[0], localKi[1])[1]
    #escanear ki baixo
    if((pixelRgbVermelho >= 245 and pixelRgbVermelho <= 255) and (pixelRgbVerde >= 0 and pixelRgbVerde <= 9)): valorAtual = "baixo"
    #escanear ki máximo
    elif((pixelRgbVermelho >= 111 and pixelRgbVermelho <= 121) and (pixelRgbVerde >= 129 and pixelRgbVerde <= 139)): valorAtual = "máximo"
    #tocar uma mensagem caso o valor tenha alterado
    if(valorAtual != valorInserido):
        if(valorAtual == "baixo"): 
            if(alvo == "jogador"): mensagem = "Seu ki está baixo, evite atacar até ter pelo menos duas barras."
            else: mensagem = "O ki do seu oponente está baixo, aproveite para atacar."
        else: 
            if(alvo == "jogador"): mensagem = "Seu ki está no máximo, ative o aura burn e ataque agressivamente."
            else: mensagem = "O ki do seu oponente está no máximo evite atacar por enquanto."
        funcaoTocarAudio(mensagem)
    return valorAtual
#checar stamina dos personagens
def checarStamina(alvo, valorInserido):
    localStamina = None
    valorAtual = valorInserido
    mensagem = None
    if(alvo == "jogador"): localStamina = [59, 120]
    else: localStamina = [1310, 120]
    #salvar valores rgb vermelho e verde do píxel
    pixelRgbVermelho = pixel(localStamina[0], localStamina[1])[0]
    pixelRgbVerde = pixel(localStamina[0], localStamina[1])[1]
    if((pixelRgbVermelho >= 22 and pixelRgbVermelho <= 32) and (pixelRgbVerde >= 37 and pixelRgbVerde <= 47)): valorAtual = "não"
    elif((pixelRgbVermelho >= 133 and pixelRgbVermelho <= 152) and (pixelRgbVerde >= 78 and pixelRgbVerde <= 90)): valorAtual = "sim"
    if(valorAtual != valorInserido):
        if(valorAtual == "não"):
            if(alvo == "jogador"): mensagem = "Seu personagem não está mais cansado."
            else: mensagem = "Seu oponente não está mais cansado."
        else:
            if(alvo == "jogador"): mensagem = "Você está ficando cansado, fique mais na defensiva."
            else: mensagem = "Seu oponente está ficando cansado, mantenha seu ki o mais alto possível para soltar o ataque mais poderoso quando o oponente ficar tonto."
        funcaoTocarAudio(mensagem)
    return valorAtual