
import random
        
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt","r")
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    
    numero = random.randrange(0,len(palavras) - 1) 
    palavra_secreta  = palavras[numero]
    
    palavra_auxiliar = []
    
    for i in range(len(palavra_secreta)):
        if palavra_secreta[i] != " ": 
            palavra_auxiliar.append("_")
        else:
            palavra_auxiliar.append(" ")
    
    
    jogo_terminou = False
    jogador_ganhou = False
    contador_acertos = 0
    contador_erros = 0
    
    mostrar_tentativas(contador_erros)


        
    while(not jogo_terminou):
        
        chute_letra = input("Digite a letra:")
        chute_letra =  chute_letra.strip().lower()
        
        if ((( chute_letra.upper() )in palavra_secreta) and (( chute_letra.upper() ) not in palavra_auxiliar) or (( chute_letra.lower() )in palavra_secreta) and (( chute_letra.lower() ) not in palavra_auxiliar)) and len(chute_letra) == 1:
            print("Você encontrou uma letra :D !")
            j = 0
            for i in range(len(palavra_auxiliar)):
                if (palavra_secreta[i].lower() or palavra_secreta[i].upper() ) == chute_letra :
                    palavra_auxiliar[j] = palavra_secreta[i]
                    contador_acertos = contador_acertos + 1
                j = j + 1
            
        elif chute_letra in palavra_auxiliar:
            print("A letra ja foi usada!")

        else:
            contador_erros = contador_erros + 1
            print("Não foi dessa vez!, essa letra não está presente na palavra") 
            desenha_forca(contador_erros)    
                 
       # mostrar_tentativas(contador_erros)
        mostra_letras_encontradas(len(palavra_auxiliar),palavra_auxiliar)
        

            
        
        if contador_acertos == len(palavra_secreta.replace(" ","")):
            jogo_terminou = True
            jogador_ganhou = True
            
        if contador_erros >= 6:
            jogo_terminou = True
            jogador_ganhou = False
        
        
    if jogador_ganhou == True:
        print("Parabéns você decifrou a palavra !!!")
    else:
        print("Não foi dessa vez, tente novamente :)")
        print("A palavra era: {}".format(palavra_secreta))


    print("Fim do jogo")
    
    
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")


    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def mostra_letras_encontradas(tamanho_palavra,palavra):
    print("\n*********************************") 
    print("Resultados:\n")
    for i in range(tamanho_palavra):
        if palavra[i] != "_" and palavra[i] != " ":
            print(palavra[i],end=' ' )
            
        elif palavra[i] == " ":
            print(" ",end=' ')
        else:
            print("_ ", end=' ')

    print("\n")
    print("*********************************") 
        
def mostrar_tentativas(erros):
    print("\n*********************************") 
    print("Você tem {} tentativas restantes**".format(6 - erros))
    print("*********************************\n") 


        
        
if(__name__ == "__main__"):
    jogar()
