VERMELHOS = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
PRETOS = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
NUMEROS_IMPARES = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
NUMEROS_PARES = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
NUMEROS_ALTOS = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
NUMEROS_BAIXOS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
DUZIA_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
DUZIA_2 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
DUZIA_3 = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
COLUNA_1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
COLUNA_2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
COLUNA_3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]



def encontrarEstrategia(bola, estrategias):

        if bola in VERMELHOS:
            estrategias[0] += 1
       
        if bola in PRETOS:
            estrategias[1]  += 1

     #   if (ODD_NUMBERS.contains(ball)) {
     #       strategies.add(RouletteStrategy.ODD_BALL)
     #   } else if (EVEN_NUMBERS.contains(ball)) {
     #       strategies.add(RouletteStrategy.EVEN_BALL)
     #   }

      #  if (HIGH_NUMBERS.contains(ball)) {
      #      strategies.add(RouletteStrategy.HIGH_BALL)
      #  } else if (LOW_NUMBERS.contains(ball)) {
      #      strategies.add(RouletteStrategy.LOW_BALL)
      #  }

     #   if (DOZEN_01_NUMBERS.contains(ball)) {
     #       strategies.add(RouletteStrategy.DOZEN_01_BALL)
     #   } else if (DOZEN_02_NUMBERS.contains(ball)) {
     #       strategies.add(RouletteStrategy.DOZEN_02_BALL)
     #   } else if (DOZEN_03_NUMBERS.contains(ball)) {
     #       strategies.add(RouletteStrategy.DOZEN_03_BALL)
     #   }

 #       if (COLUMN_01_NUMBERS.contains(ball)) {
#            strategies.add(RouletteStrategy.COLUMN_01_BALL)
 #       } else if (COLUMN_02_NUMBERS.contains(ball)) {
  #          strategies.add(RouletteStrategy.COLUMN_02_BALL)
   #     } else if (COLUMN_03_NUMBERS.contains(ball)) {
    #        strategies.add(RouletteStrategy.COLUMN_03_BALL)
    #    }

        return estrategias
    

def repeticaoVermelho(bolas,estrategias):
    
    resultado = []
    encontrou = False;

    # Verifica todas estrategias
    for estrategia in estrategias:

        # Verifica se alguma estrategia ja foi encontrada
        if encontrou == False:

            # Pega a estrategia
            cor = estrategia['estrategia'].split('-')[1]
            if cor == 'v' :
                
                contador = 0 # Contagem de repeticoes
                pararContagem = False # Caso precise parar a contagem da sequencia esse indicador muda para cancelar a estrategia

                #Contar sequencia
                for bola in bolas:
                    
                    if pararContagem == False:

                        if VERMELHOS.__contains__(int(bola['numero'])):
                            contador = contador + 1
                            
                            if estrategia['analise'] == contador:
                                pararContagem = True
                                encontrou = True
                                resultado.append(estrategia)

                        else:
                            pararContagem = True
                      


             
            



    
    return resultado
        



def analisaConfirmacao(estrategia,sinais):
    # Referencia global
    # 0 - ChatID  1 - MessageID  2 - Sinal  3 - Roleta
    # 4 - Gale 5 - confirma 6 - Entrada confirmada
    green = False
    entradaConfirmada = False
    apagarMensagem = False
    pararContagem = False
    contador = 0
    emMartinGale = False
    valorGale = 0
    if( estrategia[7] == 1):
        emMartinGale = True    
    
    ## Repeticao vermelho ==================================================================
    if estrategia[2] == 'r-v':
        
        for bola in sinais:

            if pararContagem == False:
                
                if VERMELHOS.__contains__(int(bola['numero'])):
                    contador = contador + 1

                    if estrategia[5] == contador and emMartinGale == False:
                        pararContagem = True
                        entradaConfirmada = True

                    if estrategia[5] < contador and emMartinGale == True:
                        green = True
                        pararContagem = True
                        
                else: 
                    ## o valor encontrado nao e o esperado
                    if(contador == 0): 
                        # ja foi dado entrada e a operacao esta em gale ?
                        if(emMartinGale):
                            # o valor de gale atual tem que ser menor que 3
                            if(valorGale < 3):
                                valorGale = valorGale + 1
                           
                            else:
                                # LOSS
                                apagarMensagem = True  
                                pararContagem = True                                  
                        else:
                            # Cancelar analise do sinal
                            apagarMensagem = True
                            pararContagem = True


    return entradaConfirmada,apagarMensagem,green
