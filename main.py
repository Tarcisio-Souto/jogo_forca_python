
def bonecoForca():

    kbca = ''
    for i in range(1,3,1):
        kbca = kbca + ' ' * 50 + '*' * 20 + '\n'

    for i in range(1,3,1):
        kbca = kbca + ' ' * 50 + '*' * 2 + ' ' * 16 + '*' * 2 + '\n'

    contAst1 = 2
    contEsp1 = 16
    for i in range(1,3,1):
        kbca = kbca + ' ' * 50 + '*' * 2 + ' ' * contEsp1 + '*' * contAst1 + '\n'
        contAst1 += 4
        contEsp1 -= 2

    contAst2 = 6
    contEsp2 = 14
    for i in range(1,3,1):
        kbca = kbca + ' ' * 50 + '*' * 2 + ' ' * contEsp2 + '*' * contAst2 + '\n'
        contAst2 -= 4
        contEsp2 += 2
    
    #fim kbca (metade da forca mais a cabeça)
    
    kbca2 = kbca
    for i in range(1,7,1):
        kbca2 = kbca2 + ' ' * 50 + '*' * 2 + '\n'
    
    #fim kbca2 (forca completa mais cabeça)
    
###################################################################################################
    
    tronco = kbca
    for i in range(1,5,1):
        tronco = tronco + ' ' * 50 + '*' * 2 + ' ' * 16 + '*' * 2 + '\n'

    #fim TRONCO (forca incompleta mais cabeça e tronco)

    tronco2 = tronco
    for i in range(1,3,1):
        tronco2 = tronco2 + ' ' * 50 + '*' * 2 + '\n'

    #fim TRONCO2 (forca completa mais cabeça e tronco)
    
##########################################################################################################

    bracoDir = kbca
    contEsp3 = 14
    contEsp4 = 0
    for i in range(1,4,1):
        bracoDir = bracoDir + ' ' * 50 + '*' * 2 + ' ' * contEsp3 + '*' * 2 + ' ' * contEsp4 + '*' * 2 + '\n'
        contEsp3 -= 1
        contEsp4 += 1

    for i in range(1,2,1):
        bracoDir = bracoDir + ' ' * 50 + '*' * 2 + ' ' * 16 + '*' * 2 + '\n'

    # fim bracoDIR (forca incompleta mais cabeça, tronco e braco direito)

    bracoDir2 = bracoDir
    for i in range(1,5,1):
        bracoDir2 = bracoDir2 + ' ' * 50 + '*' * 2 + '\n'

    # fim bracoDIR2 (forca completa mais cabeça, tronco e braco direito)

##########################################################################################################

    bracos = kbca
    contEsp5 = 14
    contEsp6 = 0
    for i in range(1,4,1):
        bracos = bracos + ' ' * 50 + '*' * 2 + ' ' * contEsp5 + '*' * 2 + ' ' * contEsp6 + '*' * 2 + ' ' * contEsp6 + '*' * 2 + '\n'
        contEsp5 -= 1
        contEsp6 += 1

    for i in range(1,2,1):
        bracos = bracos + ' ' * 50 + '*' * 2 + ' ' * 16 + '*' * 2 + '\n'
    
    # fim bracoS (forca incompleta mais cabeça, tronco e bracos)

    bracos2 = bracos
    for i in range(1,5,1):
        bracos2 = bracos2 + ' ' * 50 + '*' * 2 + '\n'

    # fim bracoS2 (forca completa mais cabeça, tronco e bracos)

##################################################################################################################################

    pernaDir = bracoDir
    contEsp7 = 14
    for i in range(1,4,1):
        pernaDir = pernaDir + ' ' * 50 + '*' * 2 + ' ' * contEsp7 + '*' * 2 + '\n'
        contEsp7 -= 1

    # fim PERNADIR (forca incompleta mais cabeça, tronco, bracos e perna direita)

    pernaDir2 = pernaDir
    for i in range(1,3,1):
        pernaDir2 = pernaDir2 + ' ' * 50 + '*' * 2 + '\n'

    # fim PERNADIR2 (forca completa mais cabeça, tronco, bracos e perna direita)

###################################################################################################################################
    
    bonecoCompl = bracos
    contEsp8 = 14
    contEsp9 = 2
    for i in range(1,3,1):
        bonecoCompl = bonecoCompl + ' ' * 50 + '*' * 2 + ' ' * contEsp8 + '*' * 2 + ' ' * contEsp9 + '*' * 2 + '\n'
        contEsp8 -= 1
        contEsp9 += 2

    for i in range(1,3,1):
        bonecoCompl = bonecoCompl + ' ' * 50 + '*' * 2 + '\n'
    
    return kbca2, tronco2, bracoDir2, bracos2, pernaDir2, bonecoCompl

def main():

    import random

    arq1 = open('objetoMFac.txt','rt')
    arq1b = open('objetoFacil.txt','rt')
    arq1c = open('objetoNormal.txt','rt')
    arq1d = open('objetoDificil.txt','rt')
    arq1e = open('objetoMDif.txt','rt')
    arq2 = open('animalMFac.txt','rt')
    arq2b = open('animalFacil.txt','rt')
    arq2c = open('animalNormal.txt','rt')
    arq2d = open('animalDificil.txt','rt')
    arq2e = open('animalMDif.txt','rt')
    arq3 = open('paísesMFac.txt','rt')
    arq3b = open('paísesFacil.txt','rt')
    arq3c = open('paísesNormal.txt','rt')
    arq3d = open('paísesDificil.txt','rt')
    arq3e = open('paísesMDif.txt','rt')
        
    option = int(input("Digite 1 para jogar ou 2 para sair:   "))
    print()
    while option == 1:
        print("ESCOLHA QUAL A CATEGORIA DE PALAVRAS:   \n")
        choice = int(input("DIGITE 1 PARA OBJETO\nDIGITE 2 PARA ANIMAL\nDIGITE 3 PARA PAÍSES\n\nESCOLHA:   "))
        print()
        novo = ''
        ##########################################  INÍCIO OBJETO  ################################################
        
        if choice == 1:
            print("A DICA É OBJETO!\n")
            print("ESCOLHA O NÍVEL DO JOGO:   \n")
            grauDif = int(input("DIGITE 1 PARA MUITO FÁCIL\nDIGITE 2 PARA FÁCIL\nDIGITE 3 PARA NORMAL\nDIGITE 4 PARA DIFÍCIL\nDIGITE 5 PARA MUITO DIFÍCIL\n\nESCOLHA:   ")) 
            if grauDif == 1:
                palavras = arq1.readline() # Muito fácil
                while palavras != '':
                    novo = novo + palavras.strip().lower() # Foi preciso criar este comando para corrigir um erro do IDLE. OBS.: espaço ao saltar linha.
                    palavras = arq1.readline()
            if grauDif == 2:
                palavras = arq1b.readline() # Fácil
                while palavras != '':
                    novo = novo + palavras.strip().lower() # Foi preciso criar este comando para corrigir um erro do IDLE. OBS.: espaço ao saltar linha.
                    palavras = arq1b.readline()
            if grauDif == 3:
                palavras = arq1c.readline() # Normal
                while palavras != '':
                    novo = novo + palavras.strip().lower() # Foi preciso criar este comando para corrigir um erro do IDLE. OBS.: espaço ao saltar linha.
                    palavras = arq1c.readline()
            if grauDif == 4:
                palavras = arq1d.readline() # Difícil
                while palavras != '':
                    novo = novo + palavras.strip().lower() # Foi preciso criar este comando para corrigir um erro do IDLE. OBS.: espaço ao saltar linha.
                    palavras = arq1d.readline()
            if grauDif == 3:
                palavras = arq1e.readline() # Muito difícil
                while palavras != '':
                    novo = novo + palavras.strip().lower() # Foi preciso criar este comando para corrigir um erro do IDLE. OBS.: espaço ao saltar linha.
                    palavras = arq1e.readline()
                    
        ##########################################  FIM OBJETO  #####################################################
                    
        ##########################################  INÍCIO ANIMAL  ##################################################
                    
        elif choice == 2:
            print("A DICA É ANIMAL!\n")
            print("ESCOLHA O NÍVEL DO JOGO:   \n")
            grauDif = int(input("DIGITE 1 PARA MUITO FÁCIL\nDIGITE 2 PARA FÁCIL\nDIGITE 3 PARA NORMAL\nDIGITE 4 PARA DIFÍCIL\nDIGITE 5 PARA MUITO DIFÍCIL\n\nESCOLHA:   ")) 
            if grauDif == 1:
                palavras = arq2.readline() # Muito fácil
                while palavras != '':
                    novo = novo + palavras.strip().lower() # Foi preciso criar este comando para corrigir um erro do IDLE. OBS.: espaço ao saltar linha.
                    palavras = arq2.readline()
            if grauDif == 2:
                palavras = arq2b.readline() # Fácil
                while palavras != '':
                    novo = novo + palavras.strip().lower() # Foi preciso criar este comando para corrigir um erro do IDLE. OBS.: espaço ao saltar linha.
                    palavras = arq2b.readline()
            if grauDif == 3:
                palavras = arq2c.readline() # Normal
                while palavras != '':
                    novo = novo + palavras.strip().lower() # Foi preciso criar este comando para corrigir um erro do IDLE. OBS.: espaço ao saltar linha.
                    palavras = arq2c.readline()
            if grauDif == 4:
                palavras = arq2d.readline() # Difícil
                while palavras != '':
                    novo = novo + palavras.strip().lower() # Foi preciso criar este comando para corrigir um erro do IDLE. OBS.: espaço ao saltar linha.
                    palavras = arq2d.readline()
            if grauDif == 5:
                palavras = arq2e.readline() # Muito Difícil
                while palavras != '':
                    novo = novo + palavras.strip().lower() # Foi preciso criar este comando para corrigir um erro do IDLE. OBS.: espaço ao saltar linha.
                    palavras = arq2e.readline()
                    
        ##########################################  FIM ANIMAL  ##################################################

        ##########################################  INÍCIO PAÍSES  ##################################################
                    
        elif choice == 3:
            print("A DICA É PAÍS!\n")
            print("ESCOLHA O NÍVEL DO JOGO:   \n")
            grauDif = int(input("DIGITE 1 PARA MUITO FÁCIL\nDIGITE 2 PARA FÁCIL\nDIGITE 3 PARA NORMAL\nDIGITE 4 PARA DIFÍCIL\nDIGITE 5 PARA MUITO DIFÍCIL\n\nESCOLHA:   "))
            if grauDif == 1:
                palavras = arq3.readline() # Muito fácil
                while palavras != '':
                    novo = novo + palavras.strip().lower() # Foi preciso criar este comando para corrigir um erro do IDLE. OBS.: espaço ao saltar linha.
                    palavras = arq3.readline()
            if grauDif == 2:
                palavras = arq3b.readline() # Fácil
                while palavras != '':
                    novo = novo + palavras.strip().lower() # Foi preciso criar este comando para corrigir um erro do IDLE. OBS.: espaço ao saltar linha.
                    palavras = arq3b.readline()
            if grauDif == 3:
                palavras = arq3c.readline() # Normal
                while palavras != '':
                    novo = novo + palavras.strip().lower() # Foi preciso criar este comando para corrigir um erro do IDLE. OBS.: espaço ao saltar linha.
                    palavras = arq3c.readline()
            if grauDif == 4:
                palavras = arq3d.readline() # Difícil
                while palavras != '':
                    novo = novo + palavras.strip().lower() # Foi preciso criar este comando para corrigir um erro do IDLE. OBS.: espaço ao saltar linha.
                    palavras = arq3d.readline()
            if grauDif == 5:
                palavras = arq3e.readline() # Muito difícil
                while palavras != '':
                    novo = novo + palavras.strip().lower() # Foi preciso criar este comando para corrigir um erro do IDLE. OBS.: espaço ao saltar linha.
                    palavras = arq3e.readline()
            
        ##########################################  FIM PAÍSES  ##################################################
                    
        strPalavras = ''
        for i in novo:
            if i.isalpha() or i == '-' or i == ',':
                strPalavras = strPalavras + i
            else:
                strPalavras = strPalavras + ' '
    
        lstPalavras = strPalavras.split(',')
        
        encontrar = random.choice(lstPalavras)
        encontrarFat = []
        for i in encontrar:
            encontrarFat = encontrarFat + [i]
            
        aux = []
        for i in encontrarFat:
            aux.append(i)

        letras = ['_'] * len(encontrar)
        posHifen = 0
        posEsp = 0
        for i in encontrarFat:
            if i == '-':
                posHifen = encontrar.index(i)
                letras[posHifen] = '-'
            if i == ' ':
                posEsp = encontrar.index(i)
                letras[posEsp] = '   '
                print("ATENÇÃO! PALAVRA COMPOSTA!")
        print()
        print(letras)
        print()
        contErros = 0
        lstPalsDigi = []
        while contErros != 6 or letras != aux:    
            word = input("DIGITE UMA LETRA:   ")
            while word in lstPalsDigi:
                word = input("NÃO DIGITE LETRAS REPETIDAS! DIGITE OUTRA LETRA:   ")
            lstPalsDigi.append(word)
            for i in encontrarFat:
                if word == 'a' and i == 'á':
                    word = 'á'
                elif word == 'a' and i == 'ã':
                    word = 'ã'
                elif word == 'a' and i == 'â':
                    word = 'â'
                elif word == 'e' and i == 'é':
                    word = 'é'
                elif word == 'e' and word == 'ê':
                    word == 'ê'
                elif word == 'í' and i == 'i':
                    word = 'í'
                elif word == 'o' and i == 'ó':
                    word = 'ó'
                elif word == 'o' and i == 'õ':
                    word = 'õ'
                elif word == 'u' and i == 'ú':
                    word = 'ú'
                    
            if word in encontrarFat:
                pos = encontrarFat.index(word)
                letras[pos] = word
                encontrarFat[pos] = '*'
            else:
                contErros += 1
                print()
                print(contErros,"º ERRO! RESTA(M)",abs(contErros-6),"TENTATIVA(S)!")
                print(bonecoForca()[contErros-1])
                print()
            if letras == aux:
                print("PARABÉNS! A PALAVRA ESTÁ COMPLETA!")
                print()
                break
            if contErros == 6:
                print("QUE PENA, VOCÊ PERDEU =/ ")
                break
            while word in encontrarFat:
                pos = encontrarFat.index(word)
                letras[pos] = word
                encontrarFat[pos] = '*'
            print()
            print("PALAVRAS JÁ ESCOLHIDAS: ", lstPalsDigi)
            print()
            print(letras)
            print()
            print("SE SOUBER A PALAVRA DIGITE-A, CASO ESTEJA ERRADA É GAME OVER!")
            resp = input("SABE QUAL É A PALAVRA (s/n)?   ")
            if resp == 's':
                s = ''
                for i in aux:
                    s = s + i
                
                palMisterio = input("DIGITE A PALAVRA:   ")
                if palMisterio == s:
                    print()
                    print(s.upper())
                    print("PARABÉNS! A PALAVRA ESTÁ CORRETA!")
                    break
                else:
                    print("PALAVRA INCORRETA. QUE PENA, VOCÊ PERDEU =/ ")
                    break
        print()    
        option = int(input("Digite 1 para jogar novamente ou 2 para sair:   "))
        print()

    arq1.close()
    arq2.close()
    arq3.close()
    
    return 0

main()
