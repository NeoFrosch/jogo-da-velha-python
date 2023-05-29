import random

continuar = True
posicao1 = '1'
posicao2 = '2'
posicao3 = '3'
posicao4 = '4'
posicao5 = '5'
posicao6 = '6'
posicao7 = '7'
posicao8 = '8'
posicao9 = '9'
opcoes_bloquear = None

# Função que monta a tela
def monta_tela():
    print("{} | {} | {}".format(posicao1,posicao2,posicao3))
    print("{} | {} | {}".format(posicao4,posicao5,posicao6))
    print("{} | {} | {}".format(posicao7,posicao8,posicao9))

# Jogador
def pedir_jogador():
    monta_tela()
    jogador_jogou = False

    while not jogador_jogou:
        posicao = int(input("Digite a posicao que voce deseja jogar \n"))
        if verifica_jogada(posicao):
            faz_jogada(posicao, 'X');
            jogador_jogou = True
    monta_tela()
    print("voce jogou! \n")
    verifica_vitoria('X')

#Computador
def jogada_pc():
    pc_jogou = False

    if bloquear():
        while not pc_jogou:
            posicao = random.choice(opcoes_bloquear)
            if verifica_jogada(posicao) == True:
                faz_jogada(posicao, 'O')
                print("voce foi bloqueado pela IA!")
                pc_jogou = True
    else:
        while not pc_jogou:
            posicao = random.choice(range(1,10))
            if verifica_jogada(posicao):
                faz_jogada(posicao, 'O')
                pc_jogou = True
            
    print("O computador jogou \n")
    verifica_vitoria('O')

# Função que irá retornar True ou False para impedir a vitoria do jogador
def bloquear():
    global opcoes_bloquear
    if (posicao1+posicao2+posicao3).count('X') == 2 and ((posicao1+posicao2+posicao3).count('O') == 0):
        opcoes_bloquear = [1,2,3]
        return True
    elif (posicao4 + posicao5 + posicao6).count('X') == 2 and ((posicao4+posicao5+posicao6).count('O') == 0):
        opcoes_bloquear = [4,5,6]
        return True
    elif (posicao7 + posicao8 + posicao9).count('X') == 2 and ((posicao7+posicao8+posicao9).count('O') == 0):
        opcoes_bloquear = [7,8,9]
        return True
    elif (posicao1 + posicao5 + posicao9).count('X') == 2 and ((posicao1+posicao5+posicao9).count('O') == 0):
        opcoes_bloquear = [1,5,9]
        return True
    elif (posicao1 + posicao4 + posicao7).count('X') == 2 and ((posicao1+posicao4+posicao7).count('O') == 0):
        opcoes_bloquear = [1,4,7]
        return True
    elif (posicao2 + posicao5 + posicao8).count('X') == 2 and ((posicao2+posicao5+posicao8).count('O') == 0):
        opcoes_bloquear = [2,5,8]
        return True
    elif (posicao3 + posicao6 + posicao9).count('X') == 2:
        opcoes_bloquear = [3,6,9]
        return True
    elif (posicao3 + posicao5 + posicao7).count('X') == 2:
        opcoes_bloquear = [3,5,7]
        return True
    else: 
        return False
    
# Função que realizará a jogada se a posição desejada estiver disponível
def faz_jogada(num, quem_jogou):
    global posicao1, posicao2, posicao3,posicao4,posicao5, posicao6,posicao7,posicao8,posicao9

    if (num == 1):
        posicao1 = quem_jogou
    elif (num == 2):
        posicao2 = quem_jogou
    elif (num == 3):
        posicao3 = quem_jogou
    elif (num == 4):
        posicao4 = quem_jogou
    elif (num == 5):
        posicao5 = quem_jogou
    elif (num == 6):
        posicao6 = quem_jogou
    elif (num == 7):
        posicao7 = quem_jogou
    elif (num == 8):
        posicao8 = quem_jogou
    elif (num == 9):
        posicao9 = quem_jogou
        

# Função que vai verificar se a posição desejada está disponível, compara 'num' que é a posição desejada com as variaveis de cada posição
def verifica_jogada(num):
    global posicao1, posicao2, posicao3,posicao4,posicao5, posicao6,posicao7,posicao8,posicao9

    if (num == 1) and (posicao1 == '1'):
        return True
    elif (num == 2) and (posicao2 == '2'):
        return True
    elif (num == 3) and (posicao3 == '3'):
        return True
    elif (num == 4) and (posicao4 == '4'):
        return True
    elif (num == 5) and (posicao5 == '5'):
        return True
    elif (num == 6) and (posicao6 == '6'):
        return True
    elif (num == 7) and (posicao7 == '7'):
        return True
    elif (num == 8) and (posicao8 == '8'):
        return True
    elif (num == 9) and (posicao9 == '9'):
        return True
    else:
        return False

# Função que vai verificar cada combinação de vitória, sendo o argumento passado, a condição de vitória, 'XXX' (jogador) e 'OOO' (pc)
def verifica_vitoria(quem):
    global continuar, bloquear
    if posicao1+posicao2+posicao3 == quem*3:
        print("vitoria")
        continuar = False
    elif posicao4 + posicao5 + posicao6 == quem*3:
        print("vitoria")
        continuar = False
    elif posicao7 + posicao8 + posicao9 == quem*3:
        print("vitoria")
        continuar = False
    elif posicao1 + posicao5 + posicao9 == quem*3:
        print("vitoria")
        continuar = False
    elif posicao1 + posicao4 + posicao7 == quem*3:
        print("vitoria")
        continuar = False
    elif posicao2 + posicao5 + posicao8 == quem*3:
        print("vitoria")
        continuar = False
    elif posicao3 + posicao6 + posicao9 == quem*3:
        print("vitoria")
        continuar = False
    elif posicao3 + posicao5 + posicao7 == quem*3:
        print("vitoria")
        continuar = False
    else:
        verifica_empate()

# Função que irá verificar empate, caso todas as posições estiverem preenchidas (atribuidas outros valores diferentes das iniciais)
def verifica_empate():
    global continuar
    if (posicao1 != '1') and (posicao2 != '2') and (posicao3 != '3') and (posicao4 != '4') and (posicao5 != '5') and (
            posicao6 != '6') and (posicao7 != '7') and (posicao8 != '8') and (posicao9 != '9'):
        print("empate")
        continuar = False

while continuar:
    pedir_jogador()
    jogada_pc()
