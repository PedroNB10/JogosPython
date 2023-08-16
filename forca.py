
def mostra_letras_encontradas(tamanho_palavra,palavra):
    print("\n*********************************") 
    print("Resultados:\n")
    for i in range(tamanho_palavra):
        if palavra[i] != "_":
            print(palavra[i],end=' ' )
        else:
            print("_ ", end=' ')

    print("\n")
    print("*********************************") 
        
def mostrar_tentativas(erros):
    print("\n*********************************") 
    print("Você tem {} tentativas restantes**".format(6 - erros))
    print("*********************************\n") 
    


    
        
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    palavra_auxiliar = list("______")
    jogo_terminou = False
    jogador_ganhou = False
    contador_acertos = 0
    contador_erros = 0
    

    
    while(not jogo_terminou):
        
        chute_letra = input("Digite a letra:")
        
        if (chute_letra in palavra_secreta) and (chute_letra not in palavra_auxiliar) :
            print("Você encontrou uma letra :D !")
            index = palavra_secreta.find(chute_letra)
            j = 0
            for i in range(len(palavra_auxiliar)):
                if palavra_secreta[i] == chute_letra:
                    palavra_auxiliar[j] = chute_letra
                    contador_acertos = contador_acertos + 1
                j = j + 1
            
        elif chute_letra in palavra_auxiliar:
            print("A letra ja foi usada!")

        else:
            contador_erros = contador_erros + 1
            print("Não foi dessa vez!, essa letra não está presente na palavra")     
                 
        mostrar_tentativas(contador_erros)
        mostra_letras_encontradas(len(palavra_auxiliar),palavra_auxiliar)
        

            
        
        if(contador_acertos == len(palavra_secreta)):
            jogo_terminou = True
            jogador_ganhou = True
            
        if contador_erros >= 6:
            jogo_terminou = True
            jogador_ganhou = False
        
        
    if jogador_ganhou == True:
        print("Parabéns você decifrou a palavra !!!")
    else:
        print("Não foi dessa vez, tente novamente :)")


print("Fim do jogo")



        
        
if(__name__ == "__main__"):
    jogar()
