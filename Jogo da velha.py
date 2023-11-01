print("Bem vindo ao jogo da velha!")
#Criação do tabuleiro como um matriz de 3x3.
tabuleiro = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#função para imprimir o tabuleiro e o atualizando a cada jogada.
def imprime_tabuleiro(tabuleiro):
    print("#############################")
    print("##      1     2     3      ## ")
    print("##    -----+-----+------   ##")
    print(f"##  1 |  {tabuleiro[0][0]} |  {tabuleiro[0][1]}  |  {tabuleiro[0][2]}  |   ##")
    print("##    -----+-----+------   ##")
    print(f"##  2 |  {tabuleiro[1][0]} |  {tabuleiro[1][1]}  |  {tabuleiro[1][2]}  |   ##")
    print("##    -----+-----+------   ##")
    print(f"##  3 |  {tabuleiro[2][0]} |  {tabuleiro[2][1]}  |  {tabuleiro[2][2]}  |   ##")
    print("#############################")
    

#funções para receber a jogada do primeiro e do segundo jogador   
def jogada_jogador():
    while True:
        coluna = int(input("Jogador 1, qual a coluna da sua jogada?: "))
        linha = int(input("Jogador 1, qual a linha da sua jogada?: "))
        if tabuleiro[linha-1][coluna-1] != 0:
            #se na coordenada escolhida pelo jogador tiver um valor diferente de 0
            #ou seja uma coordenada que ja possuí uma jogada, o loop irá continuar pedindo
            #a coordenada até que ela seja certa
            continue
            coluna = int(input("Jogador 1, qual a coluna da sua jogada?: "))
            linha = int(input("Jogador 1, qual a linha da sua jogada?: "))
        else:
            #quando a jogada é válida o numero correspondente pelo jogador será substituido na matriz.
            tabuleiro[linha-1][coluna-1] = 1
            break

def jogada_jogador2():
    while True:
        coluna = int(input("Jogador 2, qual a coluna da sua jogada?: "))
        linha = int(input("Jogador 2, qual a linha da sua jogada?: "))
        if tabuleiro[linha-1][coluna-1] != 0:

            continue
            coluna = int(input("Jogador 2, qual a coluna da sua jogada?: "))
            linha = int(input("Jogador 2, qual a linha da sua jogada?: "))
        else:
            tabuleiro[linha-1][coluna-1] = 2
            break
            
    
jogadas = 9    

#loop responsável por mostrar na tela as jogadas 
while True:
    #quando o loop atingir o número maximo de jogadas do tabuleiro que é 9
    #vai encerrar e prosseguir para a parte de verificação do ganhador
    imprime_tabuleiro(tabuleiro)
    jogada_jogador()
    jogadas -= 1
    if jogadas <= 0:
        break
    imprime_tabuleiro(tabuleiro)
    jogada_jogador2()
    jogadas -= 1
    if jogadas <= 0:
        break
    

ganhador = 0
#para verificar qual foi o ganhador o programa faz a soma de todas as diagonais e todas linhas e colunas 
#aqui é verificado se algum dos jogadores ganhou por linhas ou colunas
#se a soma de alguma linha ou coluna der o valor de 6 ou de 3
#que é o numero do jogador multiplicado pelo número de casas
#isso indica que ele é o vencedor
#caso haja ganhador por linhas ou colunas o loop irá retornar o numero do ganhador e irá verificar as diagonais
#o que irá acontecer também mesmo se não houver nenhum ganhador ainda
for l in range(3):
    
    soma = tabuleiro[l][0] + tabuleiro[l][1] + tabuleiro[l][2]
    if soma == 3:
        ganhador = 1
    elif soma == 6:
        ganhador = 2
    
for i in range(3):

    soma = tabuleiro[0][i]+tabuleiro[1][i]+tabuleiro[2][i]
    if soma == 3:
        ganhador = 1
    elif soma == 6:
        ganhador = 2

#aqui é feito a verificação das diagonais
diagonal1 = tabuleiro[0][0]+tabuleiro[1][1]+tabuleiro[2][2]
diagonal2 = tabuleiro[0][2]+tabuleiro[1][1]+tabuleiro[2][0]
if diagonal1==3 or diagonal2==3:
    ganhador = 1
    
elif diagonal1==6 or diagonal2 == 6:
    ganhador = 2
    
if ganhador == 1:
    print("Jogador 1 ganhou")
elif ganhador == 2:
    print("Jogador 2 ganhou")
elif ganhador == 0:
    print("Deu velha")
    